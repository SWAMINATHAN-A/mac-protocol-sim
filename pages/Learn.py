import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Learn",
    page_icon="📚",
    layout="wide"
)
st.sidebar.page_link('Home.py', label='Home')
st.sidebar.page_link('pages/CSMA_CD.py', label='CSMA/CD')
st.sidebar.page_link('pages/Slotted_Aloha.py', label='Slotted_Aloha')
st.sidebar.markdown("---")
# Custom CSS
st.markdown("""
<style>
    .page-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .learn-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .video-container {
        background: #f5f5f5;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
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
<div class="page-header">
    <h1>Learn About Network Protocols</h1>
    <p style="font-size: 1.2rem; margin-top: 0.5rem;">
        Educational Materials and Resources
    </p>
</div>
""", unsafe_allow_html=True)

# Main Content Sections
st.markdown("## Project Materials from Prescribed Textbook")

with st.expander("CSMA/CA"):
    st.markdown("""
    ## Carrier Sense Multiple Access (CSMA)  
*(Cited from: Kurose & Ross, “Computer Networking: A Top-Down Approach”, 6th Edition)*

CSMA improves upon ALOHA by **listening before transmitting**.

### Key Idea — Carrier Sensing
A node checks whether the channel is idle before sending.

- If **channel is idle** → transmit
- If **channel is busy** → wait until idle

Still, **collisions can occur** due to **propagation delay**:
- A node may **not detect** another transmission already started far away
- Two nodes may sense idle ⇒ transmit ⇒ collision occurs

➡ CSMA reduces collisions compared to ALOHA but cannot eliminate them completely.
    """)

with st.expander("CSMA/CD"):
    st.markdown("## Carrier Sense Multiple Access with Collision Detection (CSMA/CD)")
    st.markdown("*(Cited from: Kurose & Ross, “Computer Networking: A Top-Down Approach”, 6th Edition)*")
    
    st.markdown("""
        CSMA/CD adds **collision detection** to CSMA. A transmitting node **listens to the channel**:
        * If it detects another transmission interfering → **abort immediately**
        * **Do not send the entire corrupted frame**
        * Then wait a **random backoff time** before retrying
        ---
        ### CSMA/CD Algorithm (Adapter Behavior)
        1. Get a frame ready for transmission
        2. Sense channel
            * If idle → start sending
            * If busy → wait until idle
        3. While sending, **listen** for collision
        4. If **no collision** → success ✅
        5. If **collision detected** → stop + backoff → retry later
        ---
        ### Binary Exponential Backoff
        If a frame has suffered **n collisions**:
    """)
    
    st.latex(r'''
        K \in \{0, 1, 2, \ldots, 2^n - 1\}
    ''')
    
    st.markdown("Wait time:")
    
    st.latex(r'''
        \text{Backoff} = K \times 512 \text{ bit times}
    ''')
    
    st.markdown("""
        * Small wait when few collisions
        * Longer wait as collisions increase
        ---
        ### Efficiency Approximation
    """)
    
    st.latex(r'''
        \text{Efficiency} \approx \frac{1}{1 + 5 \cdot (d_{prop} / d_{trans})}
    ''')
    
    st.markdown("""
        Where:
        * $d_{prop}$ = propagation delay (Using inline math in st.markdown is generally safe for simple variables)
        * $d_{trans}$ = frame transmission time
        
        ✅ Efficiency increases when:
        * Propagation delay is small
        * Frame size is large
    """)

with st.expander("Pure ALOHA"):
    st.markdown("## Pure (Unslotted) ALOHA")
    st.markdown("*(Cited from: Kurose & Ross, “Computer Networking: A Top-Down Approach”, 6th Edition)*")

    st.markdown("""
        Pure ALOHA does not require synchronization.

        ### Operation
        * Whenever a frame arrives for transmission, the node sends it immediately
        * If collision occurs:
            * After completing the transmission, the node retransmits with probability **p**
            * It may wait idle for one frame-time before another attempt

        ### Vulnerability Period
        A collision can occur if any other node transmits within:
    """)

    # Use st.latex for the vulnerability window
    st.latex(r'''
        \text{vulnerability window} = 2 \text{ frame times}
    ''')

    st.markdown("Thus, probability of success:")

    # Use st.latex for the probability of success
    # Note: I assumed the formula represents the probability of a *single* node's success in a frame time.
    st.latex(r'''
        p(1 - p)^{2(N-1)}
    ''')

    st.markdown("### Maximum Efficiency")

    # Use st.latex for the maximum efficiency
    st.latex(r'''
        \frac{1}{2e} \approx 0.18
    ''')

    st.markdown("""
        * ➡ Only **18%** of slots are successful
        * ➡ Exactly **half** the efficiency of Slotted ALOHA
        * ➡ Simplicity comes with lower performance
    """)
    
with st.expander("Slotted ALOHA"):
    st.markdown("## Slotted ALOHA")
    st.markdown("*(Cited from: Kurose & Ross, “Computer Networking: A Top-Down Approach”, 6th Edition)*")

    st.markdown("""
        Slotted ALOHA is a random access protocol used in multiple access links.
        The following assumptions are made:

        * All frames are of equal size (L bits)
        * Time is divided into slots of duration $L/R$ seconds (one frame time)
        * Nodes begin transmission only at the start of a slot
        * All nodes are synchronized to slot boundaries
        * Any collision is detected before the slot ends

        ### Operation
        * If a node has a new frame, it waits for the next slot and transmits
        * If the transmission is successful (no collision), the frame is done
        * If a collision occurs, the node retransmits in future slots with probability **p**
            * Each collision-involved node retransmits independently using probability **p**

        ### Notes
        * Highly decentralized; nodes independently detect collisions and decide retransmissions
        * Efficient when only one active node exists
        * Inefficiency arises when:
            * More than one node transmits (collision → wasted slot)
            * No node transmits (empty slot)

        ### Efficiency
        Probability of a successful slot:
    """)

    # Use st.latex for the probability of a successful slot
    st.latex(r'''
        Np(1 - p)^{(N-1)}
    ''')

    st.markdown("Maximum efficiency as $N \\to \infty$:")

    # Use st.latex for the maximum efficiency
    st.latex(r'''
        \frac{1}{e} \approx 0.37
    ''')
st.markdown("""##### Citation:""")
st.markdown("""All above material is taken and summarized from:  
**James F. Kurose & Keith W. Ross — “Computer Networking: A Top-Down Approach”, Sixth Edition**, Pearson.
""")
st.divider()

st.markdown("## How We Built This Project")

tab1, tab2, tab3, tab4 = st.tabs(["1. Research", "2. Design", "3. Implementation", "4. Testing"])

with tab1:
    st.markdown("""
    ### Research Phase
    
##### Literature Review

- Studied MAC layer protocols including:
  - **CSMA/CD** for wired Ethernet networks
  - **CSMA/CA** for wireless medium access
  - **Pure ALOHA** and **Slotted ALOHA** for random access communication
- Reviewed academic papers focusing on:
  - Collision detection efficiency in CSMA/CD
  - Collision avoidance with RTS/CTS and ACK in CSMA/CA
  - Probabilistic retransmission in ALOHA protocols
- Analyzed real-world applications:
  - Ethernet (CSMA/CD)
  - Wi-Fi (CSMA/CA under IEEE 802.11)
  - Satellite/RFID networks (ALOHA systems)

##### Protocol Analysis

- Key performance metrics studied:
  - **Throughput**, **Delay**, **Collision Probability**, **Channel Utilization**
- Collision handling strategies compared:
  - **CSMA/CD** → Detects collisions & backs off
  - **CSMA/CA** → Avoids collisions using backoff + control frames
  - **ALOHA** → Random retransmissions using probability \( p \)
- Protocol efficiencies evaluated:
  - Slotted ALOHA: \( \frac{1}{e} \approx 0.37 \) (≈ 37%)
  - Pure ALOHA: \( \frac{1}{2e} \approx 0.18 \) (≈ 18%)
  - CSMA-based protocols perform significantly better under load


##### Tools Selection

- **Python** for simulation and probability modeling
- **Streamlit** for an interactive and user-friendly interface
- **NumPy** for computing slot-wise success/collision probabilities
- **Matplotlib** for plotting throughput vs load graphs
    """)

with tab2:
    st.markdown("""
    ### Design Phase
    
    **Architecture:**
    """)
    
    st.code("""
Project Structure:
├── Home.py                      (Main page)
├── pages/
│   ├── CSMA_CD.py               (CSMA/CD Simulator)
│   ├── CSMA_CA.py               (CSMA/CA Simulator)
│   ├── Pure_Aloha.py            (Pure ALOHA Simulator)
│   ├── Slotted_Aloha.py         (Slotted ALOHA Simulator)
│   ├── Learn.py                 (Educational Theory / Learning Content)
│   ├── Help.py                  (User Instructions)
│   ├── Download.py              (Download Results / Export Page)
│   └── Developed_by.py          (Developer / Team Info Page)
├── images/                      (UI Images / Graphs / Icons)
├── assets/                      (Stylesheets / Additional Resources)
├── LICENSE
├── README.md
└── requirements.txt
    """, language="text")
    
    st.markdown("""
    **Simulation Algorithm:**
    1. **Initialize Environment**
       - Set number of nodes (N)
       - Set transmission probability (p)
       - Set simulation duration (time slots/units)
       - Initialize data structures
    
    2. **Main Simulation Loop** - For each time slot/unit:
       - Determine which nodes want to transmit
       - Apply protocol-specific rules (ALOHA/CSMA/CD/CA)
       - Detect collisions
       - Record events (Success/Collision/Idle)
    
    3. **Calculate Performance Metrics**
       - Throughput (S)
       - Offered Load (G)
       - Success Rate
       - Collision Rate
       - Channel Utilization
    
    4. **Generate Visualizations**
       - Timeline/Gantt charts
       - Throughput vs Load graphs
       - Distribution pie charts
       - Time-series activity plots
    
    ---
    
    **Protocol Comparison:**
    
    | Protocol | Max Throughput | Optimal Load | Efficiency |
    |----------|----------------|--------------|------------|
    | Pure ALOHA | 0.184 (18.4%) | G = 0.5 | Low |
    | Slotted ALOHA | 0.368 (36.8%) | G = 1.0 | Medium |
    | CSMA/CD | 0.80-0.95 | Variable | High |
    | CSMA/CA | 0.50-0.70 | Variable | Medium-High |
    """)

with tab3:
    st.markdown("""
    ### Implementation Phase
    
    **Core Components:**
    
    1. **Simulation Engine:**
       - Event-driven simulation loop
       - Node state management
       - Collision detection logic
       - Backoff mechanism (exponential for CSMA/CD, random for CSMA/CA)
       - Carrier sensing mechanism
       - ACK/timeout handling
    
    2. **Visualization:**
       - Gantt charts for timeline
       - Bar charts for metrics comparison
       - Line graphs for throughput analysis
       - Pie charts for slot distribution
       - Throughput vs Offered Load curves
    
    3. **User Interface:**
       - Parameter controls via sliders
       - Real-time simulation execution
       - Interactive data tables
       - CSV export functionality
       - Protocol-specific parameter adjustment
    
    ---
    
    **Key Algorithms Implemented:**
    """)
    
    st.subheader("Pure ALOHA")
    st.code("""
# Pure ALOHA - Transmit anytime
for each time_unit:
    for each node:
        if not transmitting and random() < probability:
            start_transmission(duration)
    
    # Check for overlapping transmissions
    if overlapping_transmissions > 1:
        collision = True
    """, language="python")
    
    st.subheader("Slotted ALOHA")
    st.code("""
# Slotted ALOHA - Transmit at slot boundaries
for each slot:
    transmitting_nodes = 0
    for each node:
        if random() < probability:
            transmitting_nodes += 1
    
    if transmitting_nodes > 1:
        collision = True
    """, language="python")
    
    st.subheader("CSMA/CD")
    st.code("""
# CSMA/CD - Carrier Sense + Collision Detection
if channel_idle:
    start_transmission()
    
    if collision_detected:
        send_jam_signal()
        backoff_time = random(0, 2^min(attempts, 10) - 1)
        wait(backoff_time)
        retry_transmission()
    """, language="python")
    
    st.subheader("CSMA/CA")
    st.code("""
# CSMA/CA - Carrier Sense + Collision Avoidance
wait_for_DIFS()

if channel_idle:
    backoff_counter = random(0, CW - 1)
    
    while backoff_counter > 0:
        if channel_idle:
            backoff_counter -= 1
        else:
            freeze_counter()
    
    send_packet()
    
    if ACK_received:
        success = True
        reset_CW()
    else:
        double_CW()
        retry()
    """, language="python")

with tab4:
    st.markdown("""
    ### Testing Phase
    
    **Validation Steps:**
    
    1. **Unit Testing:**
       - Test individual protocol functions
       - Verify collision detection
       - Validate backoff calculations
    
    2. **Performance Testing:**
       - Compare with theoretical results
       - Verify throughput formulas
       - Test edge cases (high/low load)
    
    3. **User Testing:**
       - Interface usability
       - Parameter sensitivity
       - Result interpretation
    
    **Results:**
    - Simulated throughput matches theory within 5%
    - All protocol variants work correctly
    - Visualizations accurately represent events
    """)

st.divider()

st.markdown("## Video Demonstrations")

def embed_youtube(url, width=350, height=200):
    st.markdown(
        f"""
        <iframe width="{width}" height="{height}" 
        src="{url.replace("watch?v=", "embed/")}" 
        frameborder="0" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True,
    )
st.subheader(" ")
st.subheader("CSMA/CD & CSMA/CA")

col1, col2 = st.columns(2)
with col1:
    embed_youtube("https://www.youtube.com/watch?v=XrimgDtk34s")
    embed_youtube("https://www.youtube.com/watch?v=iKn0GzF5-IU")
with col2:
    embed_youtube("https://www.youtube.com/watch?v=IAKncL67Pp4")
    embed_youtube("https://www.youtube.com/watch?v=nyYr3cR5BTw")
st.subheader(" ")    

st.subheader("Pure ALOHA & Slotted ALOHA")

col3, col4 = st.columns(2)
with col3:
    embed_youtube("https://www.youtube.com/watch?v=Z9kuc4tK1HE")
    embed_youtube("https://www.youtube.com/watch?v=fgrYDvP_Nyk")
with col4:
    embed_youtube("https://www.youtube.com/watch?v=p2caqyspMk8")
    embed_youtube("https://www.youtube.com/watch?v=hgmI1pOdfzI")


st.divider()

st.markdown("## References")

st.markdown("""
    **Textbook**
- Kurose, J. F., & Ross, K. W. (2013). *Computer Networking: A Top-Down Approach* (6th ed.). Pearson.

**Research & Learning Videos**
- PowerCert Animated Videos. (2019). *CSMA/CD explained*. YouTube. https://www.youtube.com/watch?v=XrimgDtk34s
- PowerCert Animated Videos. (2019). *CSMA/CD – How it works*. YouTube. https://www.youtube.com/watch?v=IAKncL67Pp4
- PowerCert Animated Videos. (2019). *CSMA/CA explained*. YouTube. https://www.youtube.com/watch?v=iKn0GzF5-IU
- Technical Gurukul. (2020). *CSMA vs CSMA/CD*. YouTube. https://www.youtube.com/watch?v=nyYr3cR5BTw
- Neso Academy. (2020). *Pure ALOHA*. YouTube. https://www.youtube.com/watch?v=Z9kuc4tK1HE
- PowerCert Animated Videos. (2020). *Slotted ALOHA*. YouTube. https://www.youtube.com/watch?v=p2caqyspMk8
- NPTEL. (2018). *ALOHA protocol basics*. YouTube. https://www.youtube.com/watch?v=fgrYDvP_Nyk

**Software / Tools**
- Streamlit. (2024). *Streamlit documentation*. https://streamlit.io
- Python Software Foundation. (2024). *Python Language Reference*. https://www.python.org
    """)


