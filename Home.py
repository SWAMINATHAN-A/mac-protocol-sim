import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Network Protocol Simulator",
    page_icon="assets/logo1.png",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.page_link('Home.py', label='Home')
#st.sidebar.page_link('pages/CSMA_CA.py', label='CSMA/CA')
st.sidebar.page_link('pages/CSMA_CD.py', label='CSMA/CD')
#st.sidebar.page_link('pages/Pure_Aloha.py', label='Pure Aloha')
st.sidebar.page_link('pages/Slotted_Aloha.py', label='Slotted Aloha')
st.sidebar.markdown("---")

st.markdown("""
<style>
    .nav-bar {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        display: flex;
        justify-content: flex-end;
        gap: 1rem;
        align-items: center;
    }
    .nav-button {
        background-color: white;
        color: #667eea;
        padding: 0.5rem 1.5rem;
        border-radius: 5px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s;
        border: 2px solid white;
    }
    .nav-button:hover {
        background-color: #667eea;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .protocol-card {
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        margin: 1rem 0;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .protocol-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)
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

# Header
st.markdown("""
<div class="main-header">
    <h1>🌐 Network Protocol Simulator</h1>
    <p style="font-size: 1.2rem; margin-top: 0.5rem;">
        Interactive Simulations of MAC Layer Protocols
    </p>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown("""
## Welcome!

This application provides interactive simulations of fundamental **Medium Access Control (MAC)** protocols 
used in computer networks. Explore how different protocols handle channel access, collision detection, 
and resource sharing.
""")

st.divider()

# Protocol Overview Section
st.header("Available Protocols")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="protocol-card" style="border-color: #667eea;">
        <h3>💻 CSMA/CD</h3>
        <p><strong>Carrier Sense Multiple Access with Collision Detection</strong></p>
        <p>
        Simulates three variants of CSMA protocols used in Ethernet networks:
        </p>
        <ul>
            <li><strong>1-Persistent CSMA:</strong> Transmits immediately when channel is idle</li>
            <li><strong>Non-Persistent CSMA:</strong> Waits random time before re-sensing</li>
            <li><strong>p-Persistent CSMA:</strong> Transmits with probability p when idle</li>
        </ul>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Node-level Gantt timeline visualization</li>
            <li>Collision detection and exponential backoff</li>
            <li>Performance comparison across variants</li>
            <li>Efficiency and throughput metrics</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="protocol-card" style="border-color: #764ba2;">
        <h3>📡 Slotted ALOHA</h3>
        <p><strong>Time-Slotted Random Access Protocol</strong></p>
        <p>
        Simulates the Slotted ALOHA protocol where time is divided into discrete slots 
        and nodes can only transmit at slot boundaries.
        </p>
        <ul>
            <li><strong>Random Access:</strong> Nodes transmit with probability p</li>
            <li><strong>Collision Handling:</strong> Multiple simultaneous transmissions collide</li>
            <li><strong>Maximum Throughput:</strong> Achieves S = 1/e ≈ 36.8% at G=1</li>
        </ul>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Throughput vs offered load analysis</li>
            <li>Slot status distribution visualization</li>
            <li>Time-series activity tracking</li>
            <li>Theoretical vs simulated comparison</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Getting Started Section
st.header("Getting Started")

st.markdown("""
### How to Use This Simulator:

1. **Select a Protocol** from the sidebar navigation
2. **Adjust Parameters** using the sidebar controls:
   - Number of nodes
   - Transmission probabilities
   - Propagation delays
   - Simulation duration
3. **Run Simulation** and observe the results
4. **Download Data** for further analysis (CSV export available)
""")

st.divider()

# Protocol Comparison Table
st.header("Protocol Comparison")

comparison_data = {
    "Feature": [
        "Access Method",
        "Time Structure",
        "Collision Detection",
        "Channel Sensing",
        "Maximum Throughput",
        "Best Use Case",
        "Complexity"
    ],
    "CSMA/CD": [
        "Listen before transmit",
        "Continuous time",
        "Yes (during transmission)",
        "Required",
        "~50-90% (depends on variant)",
        "Wired LANs (Ethernet)",
        "Medium"
    ],
    "Slotted ALOHA": [
        "Random access",
        "Discrete time slots",
        "No (after transmission)",
        "Not required",
        "36.8% (at G=1)",
        "Low-traffic wireless networks",
        "Low"
    ]
}

st.table(comparison_data)

st.divider()

# Educational Content
st.header("Key Concepts")

tab1, tab2, tab3 = st.tabs(["Throughput", "Collisions", "Efficiency"])

with tab1:
    st.markdown("""
    ### Throughput (S)
    **Definition:** The rate of successful message delivery over a communication channel.
    
    - Measured in **packets per time slot** or **bits per second**
    - Represents actual useful data transmitted
    - Always ≤ Channel capacity
    
    **Formula:** `S = (Successful Transmissions) / (Total Time Slots)`
    
    Higher throughput indicates better protocol performance.
    """)

with tab2:
    st.markdown("""
    ### Collisions
    **Definition:** When two or more nodes transmit simultaneously, causing data corruption.
    
    **Collision Handling Strategies:**
    - **CSMA/CD:** Detects during transmission, aborts immediately, uses exponential backoff
    - **Slotted ALOHA:** Detects after transmission, relies on acknowledgments
    
    **Backoff Mechanism:** After collision, nodes wait a random time before retrying:
    - Binary exponential backoff: Wait time = random(0, 2^k - 1) slots
    - Where k = number of consecutive collisions
    """)

with tab3:
    st.markdown("""
    ### Efficiency
    **Definition:** The fraction of time the channel is used for successful transmissions.
    
    `Efficiency = (Time for Successful Transmissions) / (Total Time)`
    
    **Factors Affecting Efficiency:**
    - Number of competing nodes
    - Transmission probability
    - Propagation delay
    - Protocol variant
    
    **Optimization:** Balance between aggressive transmission (more collisions) and 
    conservative approach (channel underutilization).
    """)

st.divider()

# Footer
st.markdown("""
<div style="text-align: center;">
    <p style="font-size: 0.9rem; color: #666;">
        Developed for Computer Networks Project<br>
    </p>
</div>
""", unsafe_allow_html=True)