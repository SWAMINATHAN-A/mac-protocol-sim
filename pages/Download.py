import streamlit as st
import pandas as pd
import io
from datetime import datetime


# Page configuration
st.set_page_config(
    page_title="Download",
    page_icon="📥",
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
    .download-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .example-box {
    background: transparent;
    color: inherit;
    border-left: 4px solid #667eea;
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

# ---------------- HEADER ----------------
st.markdown("""
<div class="page-header">
    <h1>📥 Download Simulation Data & Reports</h1>
    <p style="font-size: 1.2rem; margin-top: 0.5rem;">
        Export your CSMA/CD or Slotted ALOHA simulation results with full documentation
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 📊 Available Downloads")
st.info("""
**Note:** After running your CSMA/CD or Slotted ALOHA simulation, you can export your data here.
""")
st.divider()

# ---------------- TABS ----------------
st.markdown("## 📄 Download Simulation Outputs & Documentation")
tab1, tab2 = st.tabs(["CSMA/CD Example", "Slotted ALOHA Example"])

# ==============================================================
# TAB 1 – CSMA/CD Example
# ==============================================================
with tab1:
    st.markdown("""
    ### Example: CSMA/CD Simulation Documentation
    """)
    st.markdown("""
    <div class="example-box">
        <h4>📝 Example Format: CSMA/CD Step-by-Step Procedure</h4>
        <p><strong>Simulation:</strong> Carrier Sense Multiple Access with Collision Detection (CSMA/CD)</p>
    </div>
    """, unsafe_allow_html=True)

    # Create sample data for CSMA/CD
    sample_csma = pd.DataFrame({
        "Time Slot": [0, 1, 2, 3, 4, 5],
        "Event": ["Idle", "Success (Node 2)", "Collision", "Busy", "Success (Node 0)", "Collision"]
    })
    st.dataframe(sample_csma, use_container_width=True)

    csv_csma = sample_csma.to_csv(index=False)
    st.download_button("⬇️ Download Sample CSMA/CD Data", csv_csma,
                       "sample_csma_cd_data.csv", "text/csv")

    # Detailed step-by-step explanation
    csma_doc = f"""
CSMA/CD SIMULATION DETAILED DOCUMENTATION
============================================================
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Protocol: CSMA/CD (Carrier Sense Multiple Access with Collision Detection)
============================================================

Step 1: Input Parameters
------------------------------------------------------------
• Number of Nodes (N): 5
• Transmission Probability (p): 0.2
• Number of Time Slots: 10
• Propagation Delay: 1 slot
------------------------------------------------------------

Step 2: Initialization
------------------------------------------------------------
All 5 nodes share the same transmission medium.
Each node senses the medium before transmitting.
If the channel is busy, the node waits.
If idle, it attempts to transmit.
------------------------------------------------------------

Step 3: Transmission Process
------------------------------------------------------------
Each node generates a random number r ∈ [0,1].
If r < p, it attempts to transmit.
------------------------------------------------------------

Step 4: Collision Detection
------------------------------------------------------------
If multiple nodes transmit at the same time:
• Collision is detected by all transmitting nodes.
• They stop transmission immediately.
• Each waits for a random backoff time before retrying.
------------------------------------------------------------

Step 5: Event Log Example
------------------------------------------------------------
Time Slot | Event
0 | Idle
1 | Success (Node 2)
2 | Collision (Nodes 1, 3)
3 | Busy
4 | Success (Node 0)
5 | Collision (Nodes 2, 4)
------------------------------------------------------------

Step 6: Performance Metrics
------------------------------------------------------------
• Successful Transmissions: 2
• Collisions: 2
• Idle Slots: 1
• Busy Slots: 1
• Throughput (S) = 2 / 6 = 0.333
• Efficiency = 33.3%
------------------------------------------------------------

Step 7: Observations
------------------------------------------------------------
When multiple nodes attempt transmission, collision occurs.
CSMA/CD detects these collisions early, reducing wasted time.
Performance decreases as node count increases.
------------------------------------------------------------

Step 8: Conclusion
------------------------------------------------------------
CSMA/CD improves channel utilization by sensing before transmitting.
It works best under moderate load conditions.
------------------------------------------------------------
    """
    st.download_button("📄 Download Detailed CSMA/CD Documentation (TXT)",
                       csma_doc, "csma_cd_detailed_report.txt", "text/plain")

# ==============================================================
# TAB 2 – Slotted ALOHA Example
# ==============================================================
with tab2:
    st.markdown("""
    ### Example: Slotted ALOHA Simulation Documentation
    """)
    st.markdown("""
    <div class="example-box">
        <h4>📝 Example Format: Slotted ALOHA Step-by-Step Procedure</h4>
        <p><strong>Simulation:</strong> Slotted ALOHA Random Access Protocol</p>
    </div>
    """, unsafe_allow_html=True)

    # Create sample data for Slotted ALOHA
    sample_aloha = pd.DataFrame({
        "Slot": [0, 1, 2, 3, 4],
        "Num Transmissions": [0, 1, 3, 1, 2],
        "Status": ["Idle", "Success", "Collision", "Success", "Collision"]
    })
    st.dataframe(sample_aloha, use_container_width=True)

    csv_aloha = sample_aloha.to_csv(index=False)
    st.download_button("⬇️ Download Sample ALOHA Data", csv_aloha,
                       "sample_aloha_data.csv", "text/csv")

    # Detailed step-by-step ALOHA example
    aloha_doc = f"""
SLOTTED ALOHA SIMULATION DETAILED DOCUMENTATION
============================================================
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Protocol: Slotted ALOHA
============================================================

Step 1: Input Parameters
------------------------------------------------------------
• Number of Nodes (N): 10
• Transmission Probability (p): 0.1
• Number of Time Slots: 20
------------------------------------------------------------

Step 2: Time Slot Division
------------------------------------------------------------
Time is divided into discrete slots.
Nodes can transmit only at the start of each slot.
------------------------------------------------------------

Step 3: Transmission Attempt
------------------------------------------------------------
Each node generates a random number r ∈ [0,1].
If r < p, the node transmits.
Otherwise, it waits for the next slot.
------------------------------------------------------------

Step 4: Slot Classification
------------------------------------------------------------
• 0 transmissions → Idle Slot
• 1 transmission → Success
• >1 transmissions → Collision
------------------------------------------------------------

Step 5: Example Event Log
------------------------------------------------------------
Slot | Num Transmissions | Status
0 | 0 | Idle
1 | 1 | Success (Node 3)
2 | 3 | Collision (Nodes 1, 4, 5)
3 | 1 | Success (Node 7)
4 | 2 | Collision (Nodes 2, 8)
------------------------------------------------------------

Step 6: Results Summary
------------------------------------------------------------
• Successful Slots: 2
• Collisions: 2
• Idle Slots: 1
• Throughput (S) = 2 / 5 = 0.4
• Success Rate = 40%
------------------------------------------------------------

Step 7: Theoretical Comparison
------------------------------------------------------------
Throughput (Theoretical) = G × e^(-G)
For offered load G = N × p = 1.0
S_theoretical = 1 × e^-1 = 0.368
Simulated throughput matches theory (≈ 0.4)
------------------------------------------------------------

Step 8: Conclusion
------------------------------------------------------------
Slotted ALOHA achieves max throughput near G=1.
At this load, system operates efficiently with low idle time.
------------------------------------------------------------
"""
    st.download_button("📄 Download Detailed Slotted ALOHA Documentation (TXT)",
                       aloha_doc, "slotted_aloha_detailed_report.txt", "text/plain")

st.divider()

# ---------------- FOOTER ----------------
st.markdown("""
<div style="text-align: center;">
    <p style="font-size: 0.9rem; color: #666;">
        Network Protocol Simulator | Download Center<br>
        Run simulations on CSMA/CD or Slotted ALOHA pages to generate downloadable data!
    </p>
</div>
""", unsafe_allow_html=True)