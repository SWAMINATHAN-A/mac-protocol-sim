import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Pure ALOHA Simulator",
    page_icon="📡",
    layout="wide"
)
st.sidebar.page_link('Home.py', label='Home')
#comment out CSMA/CA page like Pure_Aloha.py page for now, we'll display it later
st.sidebar.page_link('pages/CSMA_CD.py', label='CSMA/CD')
#st.sidebar.page_link('pages/Pure_Aloha.py', label='Pure Aloha')
st.sidebar.page_link('pages/Slotted_Aloha.py', label='Slotted_Aloha')
st.sidebar.markdown("---")

st.divider()
# Navigation Bar
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col1:
    if st.button("Home", use_container_width=True):
        st.switch_page("Home.py")
with col2:
    if st.button("Download", use_container_width=True):
        st.switch_page("pages/Download.py")
with col3:
    if st.button("Help", use_container_width=True):
        st.switch_page("pages/Help.py")
with col4:
    if st.button("Learn", use_container_width=True):
        st.switch_page("pages/Learn.py")
with col5:
    if st.button("Developed by", use_container_width=True):
        st.switch_page("pages/Developed_by.py")

st.divider()

# Title and description
st.title("Pure ALOHA Protocol Simulator")
st.markdown("""
This simulator demonstrates the **Pure ALOHA** protocol, the original random access protocol 
where nodes can transmit at any time without coordination or time slot synchronization.
""")

# Sidebar for input controls
st.sidebar.header("Simulation Parameters")

num_nodes = st.sidebar.slider(
    "Number of Nodes",
    min_value=2,
    max_value=50,
    value=10,
    help="Number of nodes competing for channel access"
)

transmission_prob = st.sidebar.slider(
    "Transmission Probability (p)",
    min_value=0.01,
    max_value=1.0,
    value=0.15,
    step=0.01,
    help="Probability that a node will attempt to transmit in a given time unit"
)

num_time_units = st.sidebar.slider(
    "Number of Time Units",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100,
    help="Total number of time units to simulate"
)

packet_duration = st.sidebar.slider(
    "Packet Transmission Duration",
    min_value=1,
    max_value=5,
    value=2,
    help="Duration (in time units) for transmitting one packet"
)

# Run simulation button
run_simulation = st.sidebar.button("Run Simulation", type="primary")

# Pure ALOHA simulation logic
def simulate_pure_aloha(num_nodes, p, num_time_units, packet_duration):
    """
    Simulate Pure ALOHA protocol
    
    In Pure ALOHA, nodes can transmit at any time. A collision occurs if
    any part of a packet overlaps with another packet.
    
    Returns:
    - time_units_data: List of tuples (time_unit, active_transmissions, status)
    - node_transmissions: Dict tracking transmission periods for each node
    - statistics: Dictionary with overall statistics
    """
    # Track ongoing transmissions: {node_id: end_time}
    active_transmissions = {}
    
    # Track all transmission events
    all_transmissions = []  # (node_id, start_time, end_time, success/collision)
    
    time_units_data = []
    node_transmissions = {i: [] for i in range(num_nodes)}
    
    successful_transmissions = 0
    collisions = 0
    idle_time_units = 0
    
    for t in range(num_time_units):
        # Clean up completed transmissions
        completed_nodes = [node for node, end_time in active_transmissions.items() if end_time <= t]
        for node in completed_nodes:
            del active_transmissions[node]
        
        # Each node decides to transmit with probability p (if not already transmitting)
        for node in range(num_nodes):
            if node not in active_transmissions and np.random.random() < p:
                # Node attempts to transmit
                end_time = t + packet_duration
                active_transmissions[node] = end_time
                all_transmissions.append([node, t, end_time, None])  # Status to be determined
        
        # Check current status
        num_active = len(active_transmissions)
        
        if num_active == 0:
            status = "Idle"
            idle_time_units += 1
        elif num_active == 1:
            status = "Transmitting"
        else:
            status = "Collision"
        
        time_units_data.append((t, num_active, status))
    
    # Determine success/collision for each transmission
    for i, trans_i in enumerate(all_transmissions):
        node_i, start_i, end_i, _ = trans_i
        has_collision = False
        
        # Check overlap with other transmissions
        for j, trans_j in enumerate(all_transmissions):
            if i == j:
                continue
            node_j, start_j, end_j, _ = trans_j
            
            # Check if transmissions overlap
            if not (end_i <= start_j or end_j <= start_i):
                has_collision = True
                break
        
        if has_collision:
            all_transmissions[i][3] = "Collision"
            collisions += 1
        else:
            all_transmissions[i][3] = "Success"
            successful_transmissions += 1
        
        # Record in node_transmissions
        node_transmissions[node_i].append((start_i, end_i, all_transmissions[i][3]))
    
    # Calculate throughput (successful transmissions per time unit)
    throughput = successful_transmissions / num_time_units
    
    # Theoretical maximum throughput for Pure ALOHA is 1/(2e) ≈ 0.184
    theoretical_max = 1 / (2 * np.e)
    
    # Calculate offered load (G = N * p)
    offered_load = num_nodes * p
    
    statistics = {
        "successful": successful_transmissions,
        "collisions": collisions,
        "idle": idle_time_units,
        "throughput": throughput,
        "theoretical_max": theoretical_max,
        "offered_load": offered_load,
        "efficiency": (throughput / theoretical_max) * 100,
        "total_transmissions": len(all_transmissions)
    }
    
    return time_units_data, node_transmissions, statistics, all_transmissions

# Theoretical throughput curve
def get_theoretical_throughput(G_values):
    """Calculate theoretical throughput for Pure ALOHA: S = G * e^(-2G)"""
    return G_values * np.exp(-2 * G_values)

# Plot node-level timeline diagram (Gantt chart)
def plot_node_timeline(node_transmissions, num_time_units_to_show=100):
    """
    Create a Gantt-style timeline showing packet transmission attempts per node
    """
    colors = {'Success': '#2ecc71', 'Collision': '#e74c3c'}
    
    num_nodes = len(node_transmissions)
    
    fig, ax = plt.subplots(figsize=(14, max(6, num_nodes * 0.4)))
    
    for node_id, transmissions in node_transmissions.items():
        for start, end, status in transmissions:
            if start < num_time_units_to_show:
                width = min(end, num_time_units_to_show) - start
                ax.barh(node_id, width, left=start, color=colors.get(status, '#95a5a6'), 
                       height=0.8, edgecolor='white', linewidth=0.5)
    
    ax.set_xlabel('Time Unit', fontsize=12)
    ax.set_ylabel('Node ID', fontsize=12)
    ax.set_title(f'Timeline Diagram: Packet Transmission Attempts (First {num_time_units_to_show} time units)', 
                 fontsize=14, fontweight='bold')
    ax.set_xlim(-0.5, num_time_units_to_show)
    ax.set_ylim(-0.5, num_nodes - 0.5)
    ax.set_yticks(range(num_nodes))
    ax.set_yticklabels([f"Node {i}" for i in range(num_nodes)])
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#2ecc71', label='Success'),
        Patch(facecolor='#e74c3c', label='Collision')
    ]
    ax.legend(handles=legend_elements, loc='upper right', frameon=True, fontsize=10)
    
    plt.tight_layout()
    st.pyplot(fig)

# Main simulation
if run_simulation:
    with st.spinner("Running simulation..."):
        time_units_data, node_transmissions, stats, all_transmissions = simulate_pure_aloha(
            num_nodes, transmission_prob, num_time_units, packet_duration
        )
    
    # Display statistics
    st.header("Simulation Results")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Throughput (S)",
            f"{stats['throughput']:.4f}",
            help="Successful transmissions per time unit"
        )
    
    with col2:
        st.metric(
            "Success Rate",
            f"{(stats['successful']/stats['total_transmissions'])*100:.1f}%" if stats['total_transmissions'] > 0 else "0%"
        )
    
    with col3:
        st.metric(
            "Collision Rate",
            f"{(stats['collisions']/stats['total_transmissions'])*100:.1f}%" if stats['total_transmissions'] > 0 else "0%"
        )
    
    with col4:
        st.metric(
            "Total Attempts",
            f"{stats['total_transmissions']}"
        )
    
    st.divider()
    
    # Transmission events table
    st.subheader("Transmission Events Table")
    st.markdown("Detailed log of all transmission attempts showing start time, duration, and outcome")
    
    # Create DataFrame from transmission events
    df_transmissions = pd.DataFrame(all_transmissions, 
                                   columns=['Node', 'Start Time', 'End Time', 'Status'])
    df_transmissions = df_transmissions.sort_values('Start Time').reset_index(drop=True)
    
    # Display table
    st.dataframe(df_transmissions, use_container_width=True, height=400)
    
    st.divider()
    
    # Timeline diagram showing packet transmission attempts
    st.subheader("Timeline Diagram: Packet Transmission Attempts")
    st.markdown("Gantt chart showing when each node transmitted and whether it was successful or collided")
    plot_node_timeline(node_transmissions, num_time_units_to_show=min(100, num_time_units))
    
    st.divider()
    
    # Throughput calculation and Efficiency graph vs offered load
    st.subheader("Throughput Calculation & Efficiency Graph vs Offered Load")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("**Throughput Calculation:**")
        st.markdown(f"""
        - **Successful Transmissions:** {stats['successful']}
        - **Total Time Units:** {num_time_units}
        - **Throughput (S):** {stats['throughput']:.4f}
        - **Formula:** S = Successful Transmissions / Total Time Units
        - **Calculation:** S = {stats['successful']} / {num_time_units} = {stats['throughput']:.4f}
        """)
        
        st.markdown("**Performance Metrics:**")
        st.markdown(f"""
        - **Offered Load (G):** {stats['offered_load']:.3f}
        - **Efficiency:** {stats['efficiency']:.1f}% of theoretical max
        - **Theoretical Maximum:** {stats['theoretical_max']:.4f}
        - **Total Attempts:** {stats['total_transmissions']}
        - **Collisions:** {stats['collisions']}
        - **Idle Time Units:** {stats['idle']}
        """)
    
    with col_b:
        # Efficiency graph vs offered load
        fig1, ax1 = plt.subplots(figsize=(8, 6))
        
        # Theoretical curve for Pure ALOHA
        G_range = np.linspace(0, 5, 100)
        S_theoretical = get_theoretical_throughput(G_range)
        ax1.plot(G_range, S_theoretical, 'b-', linewidth=2, label='Theoretical (Pure ALOHA)')
        
        # Slotted ALOHA comparison
        S_slotted = G_range * np.exp(-G_range)
        ax1.plot(G_range, S_slotted, 'g--', linewidth=2, alpha=0.5, label='Slotted ALOHA (for comparison)')
        
        # Simulated point
        ax1.plot(stats['offered_load'], stats['throughput'], 'ro', 
                markersize=12, label=f'Simulated (G={stats["offered_load"]:.2f})')
        
        # Mark maximum throughput
        max_G = 0.5
        max_S = 1/(2*np.e)
        ax1.plot(max_G, max_S, 'r*', markersize=15, 
                label=f'Maximum (G=0.5, S={max_S:.3f})')
        
        ax1.set_xlabel('Offered Load (G = N × p)', fontsize=12)
        ax1.set_ylabel('Throughput (S)', fontsize=12)
        ax1.set_title('Efficiency Graph: Throughput vs Offered Load', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        ax1.set_xlim(0, 5)
        ax1.set_ylim(0, 0.4)
        
        st.pyplot(fig1)
    
    st.divider()
    
    # Additional visualizations
    st.subheader("Additional Visualizations")
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Pie chart
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        
        sizes = [stats['successful'], stats['collisions']]
        labels = ['Successful', 'Collisions']
        colors = ['#2ecc71', '#e74c3c']
        explode = (0.1, 0)
        
        ax2.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        ax2.set_title('Transmission Outcome Distribution', fontsize=14, fontweight='bold')
        
        st.pyplot(fig2)
    
    with chart_col2:
        # Time series chart - channel activity
        fig3, ax3 = plt.subplots(figsize=(8, 6))
        
        # Show first 100 time units
        display_units = min(100, num_time_units)
        time_nums = [t[0] for t in time_units_data[:display_units]]
        num_active = [t[1] for t in time_units_data[:display_units]]
        statuses = [t[2] for t in time_units_data[:display_units]]
        
        # Color code by status
        colors_map = {'Idle': '#95a5a6', 'Transmitting': '#2ecc71', 'Collision': '#e74c3c'}
        bar_colors = [colors_map[status] for status in statuses]
        
        ax3.bar(time_nums, num_active, color=bar_colors, alpha=0.7)
        ax3.set_xlabel('Time Unit', fontsize=12)
        ax3.set_ylabel('Number of Active Transmissions', fontsize=12)
        ax3.set_title(f'Channel Activity (First {display_units} time units)', fontsize=14, fontweight='bold')
        ax3.grid(True, alpha=0.3, axis='y')
        
        # Add legend
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#2ecc71', alpha=0.7, label='Single Transmission'),
            Patch(facecolor='#e74c3c', alpha=0.7, label='Collision'),
            Patch(facecolor='#95a5a6', alpha=0.7, label='Idle')
        ]
        ax3.legend(handles=legend_elements)
        
        st.pyplot(fig3)
    
    st.divider()
    
    # Download results
    st.subheader("Export Results")
    
    col_dl1, col_dl2 = st.columns(2)
    
    with col_dl1:
        # Transmission events CSV
        csv_events = df_transmissions.to_csv(index=False)
        st.download_button(
            label="Download Transmission Events (CSV)",
            data=csv_events,
            file_name=f"pure_aloha_events_N{num_nodes}_p{transmission_prob}.csv",
            mime="text/csv"
        )
    
    with col_dl2:
        # Statistics CSV
        stats_df = pd.DataFrame([{
            "Nodes": num_nodes,
            "Transmission Probability": transmission_prob,
            "Total Time Units": num_time_units,
            "Packet Duration": packet_duration,
            "Offered Load (G)": stats['offered_load'],
            "Throughput (S)": stats['throughput'],
            "Total Attempts": stats['total_transmissions'],
            "Successful": stats['successful'],
            "Collisions": stats['collisions'],
            "Success Rate (%)": (stats['successful']/stats['total_transmissions'])*100 if stats['total_transmissions'] > 0 else 0,
            "Collision Rate (%)": (stats['collisions']/stats['total_transmissions'])*100 if stats['total_transmissions'] > 0 else 0,
            "Efficiency (%)": stats['efficiency']
        }])
        csv_stats = stats_df.to_csv(index=False)
        st.download_button(
            label="Download Statistics Summary (CSV)",
            data=csv_stats,
            file_name=f"pure_aloha_stats_N{num_nodes}_p{transmission_prob}.csv",
            mime="text/csv"
        )

else:
    # Initial state - show explanation
    st.info("Set your parameters in the sidebar and click Run Simulation to start!")
    
    st.header("About Pure ALOHA")
    
    st.markdown("""
    ### How It Works:
    1. **No time synchronization** - Nodes can transmit at any time
    2. **Random transmission** - Each node transmits with probability `p` in each time unit
    3. **Success condition** - Transmission succeeds only if it doesn't overlap with any other transmission
    4. **Collision** - If any part of two packets overlap in time, both collide
    5. **Vulnerable period** - A packet is vulnerable to collision for 2× its transmission duration
    
    ### Key Concepts:
    - **Offered Load (G)**: G = N × p (number of nodes × transmission probability)
    - **Throughput (S)**: Average number of successful transmissions per time unit
    - **Maximum Throughput**: S_max = 1/(2e) ≈ 0.184 at G = 0.5
    - **Vulnerable Period**: 2T (where T is packet transmission time)
    
    ### Comparison with Slotted ALOHA:
    - **Pure ALOHA**: Maximum throughput = 1/(2e) ≈ 0.184 (18.4%)
    - **Slotted ALOHA**: Maximum throughput = 1/e ≈ 0.368 (36.8%)
    - Slotted ALOHA achieves **2× better throughput** due to synchronization
    
    ### Optimal Performance:
    For maximum throughput, set transmission probability to: **p = 0.5/N**
    
    This ensures the offered load G = N × (0.5/N) = 0.5, achieving maximum throughput!
    """)
    
    # Comparison table
    st.subheader("Pure ALOHA vs Slotted ALOHA")
    
    comparison_df = pd.DataFrame({
        "Feature": ["Time Synchronization", "Transmission Timing", "Vulnerable Period", 
                   "Max Throughput", "Optimal Load (G)", "Complexity"],
        "Pure ALOHA": ["Not Required", "Any time", "2T", "≈ 0.184 (18.4%)", "0.5", "Simple"],
        "Slotted ALOHA": ["Required", "Slot boundaries only", "T", "≈ 0.368 (36.8%)", "1.0", "Moderate"]
    })
    
    st.table(comparison_df)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center;">
    <p style="font-size: 0.9rem; color: #666;">
        Developed for Computer Networks Project | Pure ALOHA Protocol Simulator<br>
    </p>
</div>
""", unsafe_allow_html=True)