import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Learn",
    page_icon="📚",
    layout="wide"
)

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
    <h1>📚 Learn About Network Protocols</h1>
    <p style="font-size: 1.2rem; margin-top: 0.5rem;">
        Educational Materials and Resources
    </p>
</div>
""", unsafe_allow_html=True)

# Main Content Sections
st.markdown("## 📖 Project Materials from Prescribed Textbook")

st.markdown("""
<div class="learn-card">
    <h3>📘 Reference Textbook</h3>
    <p><strong>Book:</strong> Computer Networks - A Systems Approach</p>
    <p><strong>Authors:</strong> Larry L. Peterson & Bruce S. Davie</p>
    <p><strong>Relevant Chapters:</strong></p>
    <ul>
        <li><strong>Chapter 2:</strong> Direct Links - Medium Access Control</li>
        <li><strong>Section 2.6:</strong> Ethernet and Multiple Access Networks</li>
        <li><strong>Section 2.6.1:</strong> Physical Properties</li>
        <li><strong>Section 2.6.2:</strong> Access Protocol (CSMA/CD)</li>
    </ul>
</div>
""", unsafe_allow_html=True)

with st.expander("📄 View Chapter Summary - CSMA/CD"):
    st.markdown("""
    ### CSMA/CD (Carrier Sense Multiple Access with Collision Detection)
    
    **Key Concepts:**
    
    1. **Carrier Sense**: Before transmitting, a node listens to check if the channel is idle
    2. **Multiple Access**: Multiple nodes share the same broadcast medium
    3. **Collision Detection**: Nodes detect when their transmission collides with another
    
    **Algorithm Steps:**
    1. Listen to the channel
    2. If idle, begin transmission
    3. If busy, wait and retry
    4. Monitor for collisions during transmission
    5. If collision detected, send jam signal
    6. Back off using exponential backoff algorithm
    7. Retry transmission
    
    **Variants:**
    - **1-Persistent**: Transmit immediately when idle (probability = 1)
    - **Non-Persistent**: Wait random time before checking again
    - **p-Persistent**: Transmit with probability p when idle
    """)

with st.expander("📄 View Chapter Summary - Slotted ALOHA"):
    st.markdown("""
    ### Slotted ALOHA Protocol
    
    **Key Concepts:**
    
    1. **Time Slots**: Time is divided into discrete, equal-length slots
    2. **Synchronization**: All nodes are synchronized to slot boundaries
    3. **Random Access**: Nodes transmit at the beginning of a slot with probability p
    
    **Algorithm Steps:**
    1. Wait for the beginning of the next time slot
    2. Transmit packet with probability p
    3. If collision occurs, wait for acknowledgment timeout
    4. Retry in a future slot (randomly selected)
    
    **Performance:**
    - Maximum throughput: S = 1/e ≈ 0.368 (36.8%)
    - Achieved when offered load G = 1
    - Formula: S = G × e^(-G)
    
    **Advantages:**
    - Simple implementation
    - No carrier sensing required
    - Works well for low traffic
    
    **Disadvantages:**
    - Lower maximum throughput compared to CSMA
    - Requires synchronization
    """)

st.divider()

st.markdown("## 🎓 How We Built This Project")

st.markdown("""
<div class="learn-card">
    <h3>🔧 Project Development Process</h3>
    <p>This simulator was built following a systematic approach:</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["1. Research", "2. Design", "3. Implementation", "4. Testing"])

with tab1:
    st.markdown("""
    ### Research Phase
    
    **Literature Review:**
    - Studied MAC layer protocols from textbook
    - Reviewed academic papers on CSMA/CD and ALOHA
    - Analyzed real-world implementations in Ethernet
    
    **Protocol Analysis:**
    - Identified key parameters affecting performance
    - Studied collision handling mechanisms
    - Analyzed throughput optimization strategies
    
    **Tools Selection:**
    - Python for implementation flexibility
    - Streamlit for interactive web interface
    - NumPy for numerical computations
    - Matplotlib for visualizations
    """)

with tab2:
    st.markdown("""
    ### Design Phase
    
    **Architecture:**
    ```
    Project Structure:
    ├── Home.py (Main page)
    ├── pages/
    │   ├── CSMA_CD.py (CSMA/CD Simulator)
    │   ├── Slotted_ALOHA.py (ALOHA Simulator)
    │   ├── Learn.py (Educational content)
    │   ├── Help.py (User guide)
    │   ├── Download.py (Export functionality)
    │   └── Developed_by.py (Team info)
    ```
    
    **Simulation Algorithm:**
    1. Initialize nodes and parameters
    2. For each time slot:
       - Determine which nodes want to transmit
       - Apply protocol rules
       - Detect collisions
       - Record events
    3. Calculate performance metrics
    4. Generate visualizations
    """)

with tab3:
    st.markdown("""
    ### Implementation Phase
    
    **Core Components:**
    
    1. **Simulation Engine:**
       - Event-driven simulation loop
       - Node state management
       - Collision detection logic
       - Backoff mechanism
    
    2. **Visualization:**
       - Gantt charts for timeline
       - Bar charts for metrics comparison
       - Line graphs for throughput analysis
       - Pie charts for slot distribution
    
    3. **User Interface:**
       - Parameter controls via sliders
       - Real-time simulation execution
       - Interactive data tables
       - CSV export functionality
    
    **Key Algorithms Implemented:**
    ```python
    # CSMA/CD Collision Detection
    if transmitting_nodes > 1:
        collision = True
        apply_exponential_backoff()
    
    # Slotted ALOHA Transmission
    for each slot:
        if random() < probability:
            attempt_transmission()
    ```
    """)

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

st.markdown("## 🎬 Video Demonstrations")

st.markdown("""
<div class="learn-card">
    <h3>📺 Animated Video Explaining Project Topics</h3>
    <p>Watch these videos to understand the protocols better:</p>
</div>
""", unsafe_allow_html=True)

col_v1, col_v2 = st.columns(2)

with col_v1:
    st.markdown("""
    <div class="video-container">
        <h4>🎥 CSMA/CD Protocol Explained</h4>
        <p>Duration: 10 minutes</p>
        <p>Topics covered:</p>
        <ul style="text-align: left;">
            <li>How carrier sensing works</li>
            <li>Collision detection mechanism</li>
            <li>Exponential backoff algorithm</li>
            <li>Protocol variants comparison</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    video_url_1 = st.text_input("Enter YouTube URL for CSMA/CD video:", key="video1")
    if video_url_1:
        st.video(video_url_1)

with col_v2:
    st.markdown("""
    <div class="video-container">
        <h4>🎥 Slotted ALOHA Protocol Explained</h4>
        <p>Duration: 8 minutes</p>
        <p>Topics covered:</p>
        <ul style="text-align: left;">
            <li>Time slot synchronization</li>
            <li>Random access mechanism</li>
            <li>Throughput optimization</li>
            <li>Performance analysis</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    video_url_2 = st.text_input("Enter YouTube URL for ALOHA video:", key="video2")
    if video_url_2:
        st.video(video_url_2)

st.divider()

st.markdown("## 📚 Additional References")

st.markdown("""
<div class="learn-card">
    <h3>📖 Recommended Reading Materials</h3>
</div>
""", unsafe_allow_html=True)

col_r1, col_r2 = st.columns(2)

with col_r1:
    st.markdown("""
    ### Textbooks
    1. **Computer Networks** - Andrew S. Tanenbaum
       - Chapter 4: The Medium Access Control Sublayer
    
    2. **Data Communications and Networking** - Behrouz A. Forouzan
       - Chapter 12: Multiple Access
    
    3. **Computer Networking: A Top-Down Approach** - Kurose & Ross
       - Chapter 6: The Link Layer
    """)

with col_r2:
    st.markdown("""
    ### Online Resources
    1. **IEEE 802.3 Standard** (Ethernet)
       - Official CSMA/CD specification
    
    2. **RFC 894** - A Standard for the Transmission of IP Datagrams over Ethernet
    
    3. **Academic Papers:**
       - "Packet Communication" - Norman Abramson (ALOHA)
       - "Ethernet: Distributed Packet Switching" - Metcalfe & Boggs
    """)

st.divider()

st.markdown("## 💡 Key Takeaways")

col_k1, col_k2, col_k3 = st.columns(3)

with col_k1:
    st.info("""
    **CSMA/CD**
    
    ✅ Best for wired networks
    
    ✅ High efficiency (50-90%)
    
    ✅ Requires collision detection
    
    ✅ Used in traditional Ethernet
    """)

with col_k2:
    st.success("""
    **Slotted ALOHA**
    
    ✅ Simple implementation
    
    ✅ Max throughput: 36.8%
    
    ✅ No carrier sensing needed
    
    ✅ Good for low traffic
    """)

with col_k3:
    st.warning("""
    **Comparison**
    
    📊 CSMA/CD: Higher throughput
    
    📊 ALOHA: Simpler protocol
    
    📊 Trade-off: Complexity vs. Performance
    
    📊 Choose based on use case
    """)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center;">
    <p style="font-size: 0.9rem; color: #666;">
        Network Protocol Simulator | Learn More About MAC Protocols<br>
    </p>
</div>
""", unsafe_allow_html=True)