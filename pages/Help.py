#change placeholder code
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Help",
    page_icon="❓",
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
    .help-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .step-box {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        margin: 0.5rem 0;
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
    <h1>❓ Help & User Guide</h1>
    <p style="font-size: 1.2rem; margin-top: 0.5rem;">
        Learn How to Execute and Use This Project
    </p>
</div>
""", unsafe_allow_html=True)

# Quick Start Guide
st.markdown("## 🚀 Quick Start Guide")

st.markdown("""
<div class="help-section">
    <h3>📝 Overview</h3>
    <p>This simulator provides interactive demonstrations of MAC layer protocols. 
    Follow the steps below to run simulations and analyze results.</p>
</div>
""", unsafe_allow_html=True)

# Step-by-step instructions
st.markdown("## 📋 Step-by-Step Instructions")

tab1, tab2, tab3 = st.tabs(["CSMA/CD Simulator", "Slotted ALOHA Simulator", "General Features"])

with tab1:
    st.markdown("### How to Use CSMA/CD Simulator")
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 1: Navigate to CSMA/CD Page</h4>
        <p>• Click on <strong>"CSMA & CSMA/CD"</strong> in the sidebar</p>
        <p>• The simulator page will load with default parameters</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 2: Set Simulation Parameters</h4>
        <p><strong>Number of Nodes (2-30):</strong> How many devices compete for channel access</p>
        <p><strong>Packets per Node (1-20):</strong> Number of packets each node wants to send</p>
        <p><strong>Propagation Delay (0-5 slots):</strong> Time for signal to travel between nodes</p>
        <p><strong>Transmission Time (1-10 slots):</strong> Time needed to transmit one packet</p>
        <p><strong>Packet Generation Probability (0-1):</strong> Chance of new packet arriving</p>
        <p><strong>Protocol Type:</strong> Select 1-Persistent, Non-Persistent, or p-Persistent CSMA</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 3: Run the Simulation</h4>
        <p>• Click the <strong>"Run Simulation"</strong> button in the sidebar</p>
        <p>• Wait for simulation to complete (usually 1-3 seconds)</p>
        <p>• Results will appear automatically</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 4: Interpret Results</h4>
        <p><strong>Metrics Display:</strong></p>
        <ul>
            <li><strong>Successful Transmissions:</strong> Number of packets sent without collision</li>
            <li><strong>Collisions:</strong> Number of times packets collided</li>
            <li><strong>Efficiency:</strong> Percentage of successful transmissions</li>
            <li><strong>Throughput:</strong> Packets successfully transmitted per time slot</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 5: Analyze Timeline</h4>
        <p><strong>Node-level Gantt Chart:</strong></p>
        <ul>
            <li><strong>Gray:</strong> Node is idle</li>
            <li><strong>Green:</strong> Successful transmission</li>
            <li><strong>Red:</strong> Collision occurred</li>
        </ul>
        <p>Each row represents one node, time flows left to right</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 6: Compare Protocols (Optional)</h4>
        <p>• Enable <strong>"Compare All Protocols"</strong> checkbox</p>
        <p>• Set number of comparison runs for averaging</p>
        <p>• View bar charts comparing efficiency and throughput</p>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("### How to Use Slotted ALOHA Simulator")
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 1: Navigate to Slotted ALOHA Page</h4>
        <p>• Click on <strong>"Slotted ALOHA"</strong> in the sidebar</p>
        <p>• Default parameters will be loaded</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 2: Configure Parameters</h4>
        <p><strong>Number of Nodes (2-50):</strong> Devices competing for access</p>
        <p><strong>Transmission Probability p (0.01-1.0):</strong> Chance a node transmits per slot</p>
        <p><strong>Number of Time Slots (100-5000):</strong> Duration of simulation</p>
        <p><strong>💡 Tip:</strong> For optimal throughput, set p = 1/N (where N = number of nodes)</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 3: Execute Simulation</h4>
        <p>• Click <strong>"Run Simulation"</strong> button</p>
        <p>• Simulation will process all time slots</p>
        <p>• Results appear in multiple sections</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 4: Review Performance Metrics</h4>
        <p><strong>Key Metrics:</strong></p>
        <ul>
            <li><strong>Throughput (S):</strong> Successful transmissions per slot</li>
            <li><strong>Success Rate:</strong> Percentage of successful slots</li>
            <li><strong>Collision Rate:</strong> Percentage of collision slots</li>
            <li><strong>Idle Rate:</strong> Percentage of idle slots</li>
            <li><strong>Offered Load (G):</strong> G = N × p</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 5: Examine Event Table</h4>
        <p>• View slot-by-slot event log</p>
        <p>• See number of transmissions per slot</p>
        <p>• Status shows: Success, Collision, or Idle</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 6: Study Timeline Diagram</h4>
        <p><strong>Color Coding:</strong></p>
        <ul>
            <li><strong>Gray:</strong> Node did not transmit (idle)</li>
            <li><strong>Green:</strong> Successful transmission</li>
            <li><strong>Red:</strong> Collision occurred</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h4>Step 7: Analyze Efficiency Graph</h4>
        <p>• <strong>Blue curve:</strong> Theoretical throughput S = G × e^(-G)</p>
        <p>• <strong>Red dot:</strong> Your simulation result</p>
        <p>• <strong>Green star:</strong> Maximum throughput point (G=1, S≈0.368)</p>
        <p>• Compare your result with theoretical prediction</p>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("### General Features & Tips")
    
    st.markdown("""
    <div class="step-box">
        <h4>📥 Downloading Results</h4>
        <p><strong>CSV Export Options:</strong></p>
        <ul>
            <li><strong>Event Data:</strong> Detailed slot-by-slot or event-by-event records</li>
            <li><strong>Statistics:</strong> Summary metrics for your simulation</li>
            <li><strong>Comparison Data:</strong> Protocol performance comparison (CSMA/CD)</li>
        </ul>
        <p><strong>How to Download:</strong></p>
        <ol>
            <li>Run a simulation</li>
            <li>Scroll to download section</li>
            <li>Click appropriate "Download ... (CSV)" button</li>
            <li>File saves to your Downloads folder</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
        <h4>⚙️ Parameter Tuning Tips</h4>
        <p><strong>For High Efficiency:</strong></p>
        <ul>
            <li>Keep number of nodes moderate (5-15)</li>
            <li>Use lower transmission probability</li>
            <li>For ALOHA: set p = 1/N</li>
        </ul>
        <p><strong>To Observe Collisions:</strong></p>
        <ul>
            <li>Increase number of nodes (20+)</li>
            <li>Increase transmission probability</li>
            <li>Use 1-Persistent CSMA</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("## 🔍 Understanding the Graphs")

col_g1, col_g2 = st.columns(2)

with col_g1:
    st.markdown("""
    ### Gantt Timeline Chart
    
    **What it shows:**
    - Each row = one node
    - Horizontal axis = time (slots)
    - Colors indicate node state
    
    **How to read it:**
    - Look for patterns of collisions (red clusters)
    - Successful transmissions show as green bars
    - Long gray periods = channel idle or node backing off
    
    **What to analyze:**
    - Are collisions concentrated at certain times?
    - Do nodes fairly share the channel?
    - How effective is the backoff mechanism?
    """)

with col_g2:
    st.markdown("""
    ### Throughput Efficiency Graph (ALOHA)
    
    **What it shows:**
    - X-axis: Offered load (G = N × p)
    - Y-axis: Throughput (S = success rate)
    - Theory vs. your simulation
    
    **How to read it:**
    - Your result should be near the blue curve
    - Maximum is at G=1 (green star)
    - Beyond G=1, more collisions reduce throughput
    
    **What to analyze:**
    - Is your simulation close to theory?
    - What happens with higher load?
    - Where is the optimal operating point?
    """)

st.divider()

st.markdown("## 🎯 What is Processed?")

st.markdown("""
<div class="help-section">
    <h3>Simulation Processing Steps</h3>
</div>
""", unsafe_allow_html=True)

col_p1, col_p2 = st.columns(2)

with col_p1:
    st.markdown("""
    ### CSMA/CD Processing
    
    **Input:**
    - Number of nodes
    - Protocol parameters
    - Propagation delays
    
    **Processing:**
    1. **Initialization:** Create nodes with packet queues
    2. **Time Loop:** For each time slot:
       - Check if channel is busy
       - Nodes sense carrier
       - Apply protocol rules (1-persistent, non-persistent, p-persistent)
       - Detect collisions
       - Calculate backoff if collision
    3. **Recording:** Log all events (success, collision, idle)
    4. **Metrics Calculation:** 
       - Count successes and collisions
       - Calculate efficiency = successes / total_slots
       - Calculate throughput = successes / time
    
    **Output:**
    - Event timeline
    - Performance metrics
    - Visualizations
    """)

with col_p2:
    st.markdown("""
    ### Slotted ALOHA Processing
    
    **Input:**
    - Number of nodes
    - Transmission probability (p)
    - Number of slots
    
    **Processing:**
    1. **Slot Loop:** For each time slot:
       - Each node generates random number
       - Transmit if random < p
       - Count transmitting nodes
       - Classify: Idle (0), Success (1), Collision (2+)
    2. **Recording:** Store slot status and transmitting nodes
    3. **Metrics Calculation:**
       - Throughput S = successes / total_slots
       - Offered load G = N × p
       - Compare with theory: S_theory = G × e^(-G)
    
    **Output:**
    - Slot-by-slot events
    - Timeline diagram
    - Throughput analysis
    - Comparison graphs
    """)

st.divider()

st.markdown("## 📊 How to Interpret Results")

with st.expander("Understanding Efficiency Metrics"):
    st.markdown("""
    ### Efficiency Interpretation
    
    **CSMA/CD Efficiency:**
    - **50-90%:** Excellent - Protocol working well
    - **30-50%:** Good - Some collisions but manageable
    - **10-30%:** Fair - High collision rate
    - **< 10%:** Poor - Too many nodes or high transmission rate
    
    **Slotted ALOHA Throughput:**
    - **S ≈ 0.368 (36.8%):** Optimal - Maximum theoretical throughput
    - **S > 0.25:** Good performance
    - **S < 0.15:** Low efficiency, adjust parameters
    
    **Collision Rate:**
    - **< 20%:** Excellent
    - **20-40%:** Acceptable
    - **> 40%:** High contention, consider reducing load
    """)

with st.expander("What Graphs Depict"):
    st.markdown("""
    ### Graph Meanings
    
    **Bar Charts (CSMA/CD Comparison):**
    - Compare three protocol variants side-by-side
    - Taller bars = better performance
    - Look for the protocol with highest efficiency for your scenario
    
    **Line Graph (ALOHA Throughput vs Load):**
    - Shows relationship between offered load and throughput
    - Bell-shaped curve is expected
    - Peak at G=1 is the optimal operating point
    
    **Pie Chart (Slot Distribution):**
    - Shows proportion of Successful, Collision, and Idle slots
    - Ideal: Large green (success) portion
    - High red (collision) = overloaded channel
    
    **Time Series Bar Chart:**
    - Shows transmission activity over time
    - Color indicates outcome
    - Helps identify bursty behavior
    """)

st.divider()

st.markdown("## ⚠️ Troubleshooting")

st.markdown("""
<div class="help-section">
    <h3>Common Issues and Solutions</h3>
</div>
""", unsafe_allow_html=True)

col_t1, col_t2 = st.columns(2)

with col_t1:
    st.markdown("""
    ### Issue: Low Efficiency
    
    **Possible Causes:**
    - Too many nodes
    - High transmission probability
    - Using 1-Persistent CSMA with many nodes
    
    **Solutions:**
    - Reduce number of nodes
    - Lower transmission/generation probability
    - Try Non-Persistent or p-Persistent CSMA
    - For ALOHA: set p = 1/N
    """)
    
    st.markdown("""
    ### Issue: Few Collisions
    
    **Possible Causes:**
    - Too few nodes
    - Very low transmission probability
    - Long propagation delay
    
    **Solutions:**
    - Increase number of nodes
    - Increase transmission probability
    - This might be okay - shows low contention!
    """)

with col_t2:
    st.markdown("""
    ### Issue: Simulation Takes Long Time
    
    **Possible Causes:**
    - Too many time slots
    - Many comparison runs
    
    **Solutions:**
    - Reduce number of slots (500-1000 is usually enough)
    - Reduce comparison runs to 5-10
    - Results are still statistically valid
    """)
    
    st.markdown("""
    ### Issue: Results Don't Match Theory
    
    **Possible Causes:**
    - Small sample size
    - Extreme parameters
    - Random variation
    
    **Solutions:**
    - Increase number of time slots
    - Run multiple simulations and average
    - Check if parameters are reasonable
    - Some variation is normal in random simulations
    """)

st.divider()

st.markdown("## 📖 Additional Help")

col_h1, col_h2, col_h3 = st.columns(3)

with col_h1:
    st.info("""
    **Need More Theory?**
    
    Visit the **Learn** page for:
    - Textbook references
    - Video explanations
    - Protocol details
    - Academic papers
    """)

with col_h2:
    st.success("""
    **Want to Export Data?**
    
    Visit the **Download** page for:
    - CSV export guides
    - Data format info
    - Analysis tips
    - Example workflows
    """)

with col_h3:
    st.warning("""
    **Have Questions?**
    
    Check the **Developed By** page to:
    - Contact team members
    - Report issues
    - Suggest features
    - Get support
    """)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center;">
    <p style="font-size: 0.9rem; color: #666;">
        Network Protocol Simulator | Help & Documentation<br>
        Still have questions? Check the Learn page or contact the development team!
    </p>
</div>
""", unsafe_allow_html=True)