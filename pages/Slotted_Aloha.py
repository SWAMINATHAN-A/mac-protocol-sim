import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Slotted ALOHA Simulator",
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
st.title("Slotted ALOHA Protocol Simulator")
st.markdown("""
This simulator demonstrates the **Slotted ALOHA** protocol, a random access protocol 
where time is divided into slots and nodes can only transmit at the beginning of a slot.
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
    value=0.3,
    step=0.01,
    help="Probability that a node will attempt to transmit in a given slot"
)

num_slots = st.sidebar.slider(
    "Number of Time Slots",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100,
    help="Total number of time slots to simulate"
)

# Run simulation button
run_simulation = st.sidebar.button("Run Simulation", type="primary")

# Slotted ALOHA simulation logic
def simulate_slotted_aloha(num_nodes, p, num_slots):
    """
    Simulate Slotted ALOHA protocol
    
    Returns:
    - slots_data: List of tuples (slot_number, num_transmissions, status)
    - node_transmissions: Dict tracking which nodes transmitted in each slot
    - statistics: Dictionary with overall statistics
    """
    slots_data = []
    node_transmissions = {i: [] for i in range(num_nodes)}  # Track per-node attempts
    successful_transmissions = 0
    collisions = 0
    idle_slots = 0
    
    for slot in range(num_slots):
        # Each node decides to transmit with probability p
        transmitting_nodes = np.random.random(num_nodes) < p
        num_transmissions = np.sum(transmitting_nodes)
        
        # Record which nodes are transmitting
        transmitting_node_ids = [i for i in range(num_nodes) if transmitting_nodes[i]]
        
        if num_transmissions == 0:
            status = "Idle"
            idle_slots += 1
            # All nodes idle
            for i in range(num_nodes):
                node_transmissions[i].append((slot, 0))  # 0 = idle
        elif num_transmissions == 1:
            status = "Success"
            successful_transmissions += 1
            # Mark successful node
            for i in range(num_nodes):
                if i in transmitting_node_ids:
                    node_transmissions[i].append((slot, 1))  # 1 = success
                else:
                    node_transmissions[i].append((slot, 0))  # 0 = idle
        else:
            status = "Collision"
            collisions += 1
            # Mark colliding nodes
            for i in range(num_nodes):
                if i in transmitting_node_ids:
                    node_transmissions[i].append((slot, 2))  # 2 = collision
                else:
                    node_transmissions[i].append((slot, 0))  # 0 = idle
        
        slots_data.append((slot, num_transmissions, status))
    
    # Calculate throughput (successful transmissions per slot)
    throughput = successful_transmissions / num_slots
    
    # Theoretical maximum throughput for Slotted ALOHA is 1/e ≈ 0.368
    theoretical_max = 1 / np.e
    
    # Calculate offered load (G = N * p)
    offered_load = num_nodes * p
    
    statistics = {
        "successful": successful_transmissions,
        "collisions": collisions,
        "idle": idle_slots,
        "throughput": throughput,
        "theoretical_max": theoretical_max,
        "offered_load": offered_load,
        "efficiency": (throughput / theoretical_max) * 100
    }
    
    return slots_data, node_transmissions, statistics

# Theoretical throughput curve
def get_theoretical_throughput(G_values):
    """Calculate theoretical throughput: S = G * e^(-G)"""
    return G_values * np.exp(-G_values)

# Plot node-level timeline diagram (Gantt chart)
def plot_node_timeline(node_transmissions, num_slots_to_show=50):
    """
    Create a Gantt-style timeline showing packet transmission attempts per node
    """
    colors = {0: '#d3d3d3', 1: '#2ecc71', 2: '#e74c3c'}
    labels = {0: 'Idle', 1: 'Success', 2: 'Collision'}
    
    num_nodes = len(node_transmissions)
    display_slots = min(num_slots_to_show, len(node_transmissions[0]))
    
    fig, ax = plt.subplots(figsize=(14, max(6, num_nodes * 0.4)))
    
    for node_id, transmissions in node_transmissions.items():
        for slot, state in transmissions[:display_slots]:
            ax.barh(node_id, 1, left=slot, color=colors[state], height=0.8, edgecolor='white', linewidth=0.5)
    
    ax.set_xlabel('Time Slot', fontsize=12)
    ax.set_ylabel('Node ID', fontsize=12)
    ax.set_title(f'Timeline Diagram: Packet Transmission Attempts (First {display_slots} slots)', 
                 fontsize=14, fontweight='bold')
    ax.set_xlim(-0.5, display_slots)
    ax.set_ylim(-0.5, num_nodes - 0.5)
    ax.set_yticks(range(num_nodes))
    ax.set_yticklabels([f"Node {i}" for i in range(num_nodes)])
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=colors[k], label=labels[k]) for k in sorted(labels.keys())]
    ax.legend(handles=legend_elements, loc='upper right', frameon=True, fontsize=10)
    
    plt.tight_layout()
    st.pyplot(fig)

# Main simulation
if run_simulation:
    with st.spinner("Running simulation..."):
        slots_data, node_transmissions, stats = simulate_slotted_aloha(num_nodes, transmission_prob, num_slots)
    
    # Display statistics
    st.header("Simulation Results")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Throughput (S)",
            f"{stats['throughput']:.4f}",
            help="Successful transmissions per slot"
        )
    
    with col2:
        st.metric(
            "Success Rate",
            f"{(stats['successful']/num_slots)*100:.1f}%"
        )
    
    with col3:
        st.metric(
            "Collision Rate",
            f"{(stats['collisions']/num_slots)*100:.1f}%"
        )
    
    with col4:
        st.metric(
            "Idle Rate",
            f"{(stats['idle']/num_slots)*100:.1f}%"
        )
    
    st.divider()
    
    # Slot-wise event table (SUCCESS, COLLISION, IDLE)
    st.subheader("Slot-wise Event Table")
    st.markdown("Event log showing success, collision, or idle status for each time slot")
    
    # Create DataFrame from slots_data
    df_events = pd.DataFrame(slots_data, columns=['Slot', 'Num Transmissions', 'Status'])
    
    # Display table
    st.dataframe(df_events, use_container_width=True, height=400)
    
    st.divider()
    
    # Timeline diagram showing packet transmission attempts
    st.subheader("Timeline Diagram: Packet Transmission Attempts")
    st.markdown("Gantt chart showing which nodes attempted transmission in each slot")
    plot_node_timeline(node_transmissions, num_slots_to_show=min(100, num_slots))
    
    st.divider()
    
    # Throughput calculation and Efficiency graph vs offered load
    st.subheader("Throughput Calculation & Efficiency Graph vs Offered Load")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("**Throughput Calculation:**")
        st.markdown(f"""
        - **Successful Transmissions:** {stats['successful']}
        - **Total Slots:** {num_slots}
        - **Throughput (S):** {stats['throughput']:.4f}
        - **Formula:** S = Successful Transmissions / Total Slots
        - **Calculation:** S = {stats['successful']} / {num_slots} = {stats['throughput']:.4f}
        """)
        
        st.markdown("**Performance Metrics:**")
        st.markdown(f"""
        - **Offered Load (G):** {stats['offered_load']:.3f}
        - **Efficiency:** {stats['efficiency']:.1f}% of theoretical max
        - **Theoretical Maximum:** {stats['theoretical_max']:.4f}
        - **Collisions:** {stats['collisions']}
        - **Idle Slots:** {stats['idle']}
        """)
    
    with col_b:
        # Efficiency graph vs offered load
        fig1, ax1 = plt.subplots(figsize=(8, 6))
        
        # Theoretical curve
        G_range = np.linspace(0, 5, 100)
        S_theoretical = get_theoretical_throughput(G_range)
        ax1.plot(G_range, S_theoretical, 'b-', linewidth=2, label='Theoretical')
        
        # Simulated point
        ax1.plot(stats['offered_load'], stats['throughput'], 'ro', 
                markersize=12, label=f'Simulated (G={stats["offered_load"]:.2f})')
        
        # Mark maximum throughput
        max_G = 1.0
        max_S = 1/np.e
        ax1.plot(max_G, max_S, 'g*', markersize=15, 
                label=f'Maximum (G=1, S={max_S:.3f})')
        
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
        
        sizes = [stats['successful'], stats['collisions'], stats['idle']]
        labels = ['Successful', 'Collisions', 'Idle']
        colors = ['#2ecc71', '#e74c3c', '#95a5a6']
        explode = (0.1, 0, 0)
        
        ax2.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        ax2.set_title('Slot Status Distribution', fontsize=14, fontweight='bold')
        
        st.pyplot(fig2)
    
    with chart_col2:
        # Time series chart
        fig3, ax3 = plt.subplots(figsize=(8, 6))
        
        # Show first 100 slots
        display_slots = min(100, num_slots)
        slot_numbers = [s[0] for s in slots_data[:display_slots]]
        num_transmissions = [s[1] for s in slots_data[:display_slots]]
        statuses = [s[2] for s in slots_data[:display_slots]]
        
        # Color code by status
        colors_map = {'Idle': '#95a5a6', 'Success': '#2ecc71', 'Collision': '#e74c3c'}
        bar_colors = [colors_map[status] for status in statuses]
        
        ax3.bar(slot_numbers, num_transmissions, color=bar_colors, alpha=0.7)
        ax3.set_xlabel('Time Slot', fontsize=12)
        ax3.set_ylabel('Number of Transmissions', fontsize=12)
        ax3.set_title(f'Transmission Activity (First {display_slots} slots)', fontsize=14, fontweight='bold')
        ax3.grid(True, alpha=0.3, axis='y')
        
        # Add legend
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#2ecc71', alpha=0.7, label='Success'),
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
        # Event table CSV
        csv_events = df_events.to_csv(index=False)
        st.download_button(
            label="Download Slot-wise Events (CSV)",
            data=csv_events,
            file_name=f"slotted_aloha_events_N{num_nodes}_p{transmission_prob}.csv",
            mime="text/csv"
        )
    
    with col_dl2:
        # Statistics CSV
        stats_df = pd.DataFrame([{
            "Nodes": num_nodes,
            "Transmission Probability": transmission_prob,
            "Total Slots": num_slots,
            "Offered Load (G)": stats['offered_load'],
            "Throughput (S)": stats['throughput'],
            "Success Rate (%)": (stats['successful']/num_slots)*100,
            "Collision Rate (%)": (stats['collisions']/num_slots)*100,
            "Idle Rate (%)": (stats['idle']/num_slots)*100,
            "Efficiency (%)": stats['efficiency']
        }])
        csv_stats = stats_df.to_csv(index=False)
        st.download_button(
            label="Download Statistics Summary (CSV)",
            data=csv_stats,
            file_name=f"slotted_aloha_stats_N{num_nodes}_p{transmission_prob}.csv",
            mime="text/csv"
        )

else:
    # Initial state - show explanation
    st.info("Set your parameters in the sidebar and click Run Simulation to start!")
    
    st.header("About Slotted ALOHA")
    
    st.markdown("""
    ### How It Works:
    1. **Time is divided into slots** - Nodes can only transmit at slot boundaries
    2. **Random transmission** - Each node transmits with probability `p` in each slot
    3. **Success condition** - Transmission succeeds only if exactly one node transmits
    4. **Collision** - If multiple nodes transmit simultaneously, all packets collide
    
    ### Key Concepts:
    - **Offered Load (G)**: G = N × p (number of nodes × transmission probability)
    - **Throughput (S)**: Average number of successful transmissions per slot
    - **Maximum Throughput**: S_max = 1/e ≈ 0.368 at G = 1
    
    ### Optimal Performance:
    For maximum throughput, set transmission probability to: **p = 1/N**
    
    This ensures the offered load G = N × (1/N) = 1, achieving maximum throughput!
    """)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center;">
    <p style="font-size: 0.9rem; color: #666;">
        Developed for Computer Networks Project | Slotted ALOHA Protocol Simulator<br>
    </p>
</div>
""", unsafe_allow_html=True)