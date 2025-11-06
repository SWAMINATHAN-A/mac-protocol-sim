import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Help",
    page_icon="❓",
    layout="wide"
)

# Sidebar
st.sidebar.page_link('Home.py', label='Home')
st.sidebar.page_link('pages/CSMA_CD.py', label='CSMA/CD')
st.sidebar.page_link('pages/Slotted_Aloha.py', label='Slotted_Aloha')
st.sidebar.markdown("---")

# ====================== CSS ======================
st.markdown("""
<style>
html, body, [class*="css"] {
    transition: background-color 0.3s ease, color 0.3s ease;
}

/* Page header */
.page-header {
    text-align: center;
    padding: 2rem 0;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 10px;
    margin-bottom: 2rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.25);
}

/* Sections */
.help-section {
    background-color: var(--background-color);
    border-radius: 10px;
    padding: 1.5rem;
    border: 1px solid var(--border-color);
    margin: 1rem 0;
}
.step-box {
    background: var(--step-bg);
    padding: 1rem;
    border-radius: 8px;
    border-left: 4px solid #667eea;
    margin: 0.5rem 0;
    color: var(--text-color);
}

/* Input / bullet card */
.input-box {
    background-color: var(--step-bg);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 1rem 1.5rem;
    margin: 0.5rem 0 1.5rem 0;
}
.input-box ul, .input-box ol {
    margin-left: 1.3rem;
}
.input-box li {
    margin: 0.4rem 0;
    line-height: 1.5rem;
}
.input-box code {
    background: rgba(0, 0, 0, 0.15);
    padding: 0.1rem 0.4rem;
    border-radius: 4px;
    font-size: 0.9rem;
}
@media (prefers-color-scheme: dark) {
    .input-box code {
        background: rgba(255, 255, 255, 0.1);
    }
}

/* Adaptive colors */
@media (prefers-color-scheme: light) {
    :root {
        --background-color: #ffffff;
        --step-bg: #f7f8fb;
        --text-color: #222;
        --border-color: #e6e6e6;
    }
}
@media (prefers-color-scheme: dark) {
    :root {
        --background-color: #121212;
        --step-bg: rgba(255,255,255,0.03);
        --text-color: #eaeaea;
        --border-color: rgba(255,255,255,0.06);
    }
}

/* Buttons */
.stButton > button {
    border-radius: 8px;
    transition: all 0.2s ease-in-out;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 3px 10px rgba(0,0,0,0.25);
}
</style>
""", unsafe_allow_html=True)

# ====================== PAGE ======================
st.divider()
col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
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
    <p style="font-size: 1.05rem; margin-top: 0.25rem;">
        Full instructions to run the CSMA/CD and Slotted ALOHA simulators, understand outputs, and export results.
    </p>
</div>
""", unsafe_allow_html=True)

# Quick overview
st.markdown("## 🚀 Quick Overview")
st.markdown("""
<div class="help-section">
<strong>What this project does:</strong> interactive simulators for MAC-layer protocols (CSMA/CD and Slotted ALOHA).
You can configure parameters, run simulations, view timelines and charts, compare protocol variants, and download CSV/TXT reports.
</div>
""", unsafe_allow_html=True)

# General flow
st.markdown("## 📋 If you clicked Help — here’s the exact flow you should follow")
st.markdown("""
<div class="input-box">
<ol>
<li><b>Choose a Simulator:</b> from the sidebar, select either <code>CSMA/CD</code> or <code>Slotted ALOHA</code>.</li>
<li><b>Set Inputs:</b> enter parameters (examples below). Use defaults to start, then vary one parameter at a time.</li>
<li><b>Run Simulation:</b> click <code>Run Simulation</code>. Wait for results (1–3 seconds).</li>
<li><b>Inspect Outputs:</b> examine the event table, Gantt timeline, and graphs.</li>
<li><b>Export:</b> click <code>Download CSV</code> or <code>TXT</code> to save your data.</li>
</ol>
</div>
""", unsafe_allow_html=True)

st.divider()

# Tabs
tab1, tab2, tab3 = st.tabs(["CSMA/CD: Full Guide", "Slotted ALOHA: Full Guide", "General — Inputs, Execution, Export"])

# ====================== TAB 1 ======================
with tab1:
    st.markdown("### CSMA/CD — Full Usage Guide")

    st.markdown("""
    <div class="help-section">
        <h4>Purpose</h4>
        <p>CSMA/CD simulates carrier sensing and collision detection where nodes listen before transmitting and abort on collision.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Example Inputs (what to enter)")
    st.markdown("""
    <div class="input-box">
    <ul>
        <li><b>Number of Nodes (N):</b> integer, e.g. <code>5</code></li>
        <li><b>Packets per Node:</b> number of packets per node, e.g. <code>1–10</code></li>
        <li><b>Propagation Delay:</b> in slots, e.g. <code>0–5</code></li>
        <li><b>Transmission Time:</b> per packet, e.g. <code>1–5</code></li>
        <li><b>Packet Generation Probability:</b> 0–1, e.g. <code>0.3</code></li>
        <li><b>Protocol Variant:</b> 1-Persistent, Non-Persistent, or p-Persistent (enter p value if applicable)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### How the simulation executes (internals)")
    st.markdown("""
    <div class="input-box">
    <ol>
      <li><b>Initialization:</b> create node objects with packet queues.</li>
      <li><b>Each slot:</b> nodes sense carrier and decide based on protocol rules.</li>
      <li><b>Collision Detection:</b> overlapping transmissions abort.</li>
      <li><b>Backoff:</b> collided nodes reschedule (Binary Exponential Backoff).</li>
      <li><b>Logging:</b> events (idle, busy, success, collision) recorded.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### What is produced (outputs)")
    st.markdown("""
    <div class="input-box">
    <ul>
        <li><b>Event Log (CSV):</b> slot-by-slot events.</li>
        <li><b>Timeline (Gantt):</b> node vs time visualization.</li>
        <li><b>Metrics:</b> successes, collisions, throughput, efficiency.</li>
        <li><b>Comparison CSV:</b> averaged results across protocol variants.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### How to interpret results")
    st.markdown("""
    <div class="input-box">
    <ul>
        <li><b>Throughput:</b> higher = better.</li>
        <li><b>Collisions:</b> too many = high contention.</li>
        <li><b>Idle slots:</b> too many = p too low or few nodes.</li>
        <li><b>Timeline:</b> red = collisions, green = success, gray = idle.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Sample troubleshooting (CSMA/CD)")
    st.markdown("""
    <div class="input-box">
    <ul>
        <li>Reduce slots if simulation is slow.</li>
        <li>Check packet probability > 0 if no successes appear.</li>
        <li>Try Non-Persistent to reduce collisions.</li>
        <li>Lower propagation delay for fairer comparison.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ====================== TAB 2 ======================
with tab2:
    st.markdown("### Slotted ALOHA — Full Usage Guide")

    st.markdown("""
    <div class="help-section">
        <h4>Purpose</h4>
        <p>Simulates slotted random access where nodes transmit at slot boundaries; used to analyze throughput vs offered load.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Example Inputs (what to enter)")
    st.markdown("""
    <div class="input-box">
    <ul>
        <li><b>Number of Nodes (N):</b> integer, e.g. <code>10</code></li>
        <li><b>Transmission Probability (p):</b> 0.01–1.0, e.g. <code>0.1</code></li>
        <li><b>Number of Time Slots:</b> e.g. <code>100–5000</code></li>
        <li><b>Random Seed (optional):</b> for reproducibility.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### How the simulation executes (internals)")
    st.markdown("""
    <div class="input-box">
    <ol>
        <li>Each node generates random r ∈ [0,1] per slot.</li>
        <li>Transmit if r < p.</li>
        <li>0 = Idle, 1 = Success, >1 = Collision.</li>
        <li>Record each slot’s status.</li>
        <li>Compute metrics & compare with theory S = G × e^{-G}.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Outputs")
    st.markdown("""
    <div class="input-box">
    <ul>
        <li><b>Event CSV:</b> slot, transmissions, status.</li>
        <li><b>Metrics:</b> success, collision, idle counts, throughput S.</li>
        <li><b>Graphs:</b> throughput vs G with theory curve.</li>
        <li><b>Timeline:</b> node activity (if enabled).</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Interpreting results")
    st.markdown("""
    <div class="input-box">
    <ul>
        <li><b>Offered load (G = N × p):</b> max throughput near G=1.</li>
        <li><b>Theoretical peak:</b> S = G × e^{-G} ≈ 0.368.</li>
        <li><b>Observed S:</b> close to theory = valid simulation.</li>
        <li>Run multiple trials to reduce randomness.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Troubleshooting (Slotted ALOHA)")
    st.markdown("""
    <div class="input-box">
    <ul>
        <li>Throughput > 1 → check formula or CSV parsing.</li>
        <li>S deviates from theory → increase slots.</li>
        <li>Too many idle slots → increase p or nodes.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ====================== TAB 3 ======================
with tab3:
    st.markdown("### General — Inputs, Execution Flow, What is Processed, and Exporting")

    st.markdown("""
    <div class="input-box">
    <ul>
        <li>Integers: Node count, slots, packets per node.</li>
        <li>Floats: Probabilities (0–1).</li>
        <li>Options: Protocol type, BEB enable, comparison runs.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Correct execution flow (concise)")
    st.markdown("""
    <div class="input-box">
    1. Set parameters → 2. (optional) comparison → 3. Run → 4. Inspect results → 5. Download CSV/TXT.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### What the simulator processes (high-level)")
    st.markdown("""
    <div class="input-box">
    <ul>
        <li>Random generation for each slot/node.</li>
        <li>Channel evaluation (busy/idle).</li>
        <li>Collision/backoff handling (CSMA/CD).</li>
        <li>Event logging and metric computation.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### What each graph/table depicts")
    st.markdown("""
    <div class="input-box">
    <ul>
        <li><b>Event Table:</b> Slot-by-slot record.</li>
        <li><b>Gantt Timeline:</b> Node vs time color-coded activity.</li>
        <li><b>Throughput vs Load:</b> Theoretical vs simulated.</li>
        <li><b>Bar Charts:</b> Compare efficiency of variants.</li>
        <li><b>Pie Chart:</b> Success/Collision/Idle ratio.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Exporting data (how to get files)")
    st.markdown("""
    <div class="input-box">
    <ol>
        <li>Run a simulation.</li>
        <li>Scroll to download section or open <b>Download</b> page.</li>
        <li>Click <b>Download CSV</b> or <b>TXT</b>.</li>
    </ol>
    <p>CSV opens in Excel; TXT contains formatted step-by-step documentation.</p>
    </div>
    """, unsafe_allow_html=True)

# ====================== FOOTER ======================
st.divider()
st.markdown("""
<div style="text-align: center;">
<p style="font-size: 0.9rem; color: var(--text-color);">
Network Protocol Simulator | Help & Documentation<br>
Still have questions? Check the Learn or Developed By pages.
</p>
</div>
""", unsafe_allow_html=True)
