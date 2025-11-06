import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# --------------------- PAGE CONFIG ---------------------
st.set_page_config(
    page_title="CSMA & CSMA/CD Simulator",
    page_icon="💻",
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

# --------------------- TITLE ---------------------
st.title("CSMA & CSMA/CD Protocol Simulator")

st.markdown("""
This simulator models Carrier Sense Multiple Access (CSMA) and CSMA/CD,
showing node-level timelines, collisions, backoff, and performance comparison.
""")

st.divider()

# --------------------- SIDEBAR ---------------------
st.sidebar.header("Simulation Parameters")

num_nodes = st.sidebar.slider("Number of Nodes", 2, 30, 6)
num_packets = st.sidebar.slider("Packets per Node", 1, 20, 5)
prop_delay = st.sidebar.number_input("Propagation Delay (slots)", 0.0, 5.0, 0.0, 0.1)
tx_time = st.sidebar.number_input("Packet Transmission Time (slots)", 1.0, 10.0, 1.0, 0.5)
packet_gen_prob = st.sidebar.slider("Probability of New Packet Generation", 0.0, 1.0, 0.12, 0.01)
protocol_type = st.sidebar.selectbox(
    "Protocol Type",
    ["1-Persistent CSMA", "Non-Persistent CSMA", "p-Persistent CSMA (CSMA/CD)"]
)
compare_protocols = st.sidebar.checkbox("Compare All Protocols (Efficiency & Throughput)")
compare_runs = st.sidebar.slider("Comparison: runs per protocol (avg)", 3, 20, 6)
run_simulation = st.sidebar.button("Run Simulation", type="primary")

# --------------------- SIMULATOR (no fixed seed inside) ---------------------
def simulate_csma(num_nodes, num_packets, prop_delay, tx_time, gen_prob, protocol, seed=None, max_time=400):
    """
    Returns:
        usage_log: list of (event, timeslot) where event in {"Idle","Busy","Success (Node i)","Collision"}
        success_count, collision_count, efficiency, throughput, utilization, node_timelines
    """
    if seed is not None:
        np.random.seed(seed)

    success_count = 0
    collision_count = 0
    usage_log = []
    node_timelines = {i: [] for i in range(num_nodes)}

    channel_busy_until = 0.0
    backoff = np.zeros(num_nodes)
    packet_ready = np.zeros(num_nodes)
    retransmission_attempts = np.zeros(num_nodes)

    for t in range(int(max_time)):
        # Packet generation (nodes get packets to send)
        for i in range(num_nodes):
            if np.random.rand() < gen_prob:
                packet_ready[i] = 1

        # Nodes ready to sense and not backing off
        sensing_nodes = [i for i in range(num_nodes) if packet_ready[i] == 1 and backoff[i] <= 0]

        # If channel is busy (we approximate using channel_busy_until)
        if t < channel_busy_until:
            # Behaviors when busy
            if protocol == "Non-Persistent CSMA":
                for i in sensing_nodes:
                    backoff[i] = np.random.randint(2, 8)  # wait some slots
            elif protocol == "p-Persistent CSMA (CSMA/CD)":
                p = 0.4
                sensing_nodes = [i for i in sensing_nodes if np.random.rand() < p]
            # mark busy/idle for each node timeline
            usage_log.append(("Busy", t))
            for n in range(num_nodes):
                node_timelines[n].append((t, 0))  # idle for nodes while channel busy (they back off)
            backoff = np.maximum(backoff - 1, 0)
            continue

        # Channel is free -> attempt
        if len(sensing_nodes) == 0:
            usage_log.append(("Idle", t))
            for n in range(num_nodes):
                node_timelines[n].append((t, 0))
        elif len(sensing_nodes) == 1:
            # Successful transmission
            node = sensing_nodes[0]
            success_count += 1
            usage_log.append((f"Success (Node {node})", t))
            packet_ready[node] = 0
            retransmission_attempts[node] = 0
            # mark node timelines
            for n in range(num_nodes):
                node_timelines[n].append((t, 1 if n == node else 0))
            # channel busy for tx_time slots
            channel_busy_until = t + max(1.0, tx_time)
        else:
            # Collision among sensing_nodes
            collision_count += 1
            usage_log.append(("Collision", t))
            # exponential backoff based on retransmission attempts
            for i in sensing_nodes:
                retransmission_attempts[i] += 1
                k = int(min(retransmission_attempts[i], 10))
                backoff[i] = np.random.randint(1, 2 ** k)  # integer slots
            # mark which nodes collided in their timelines
            for n in range(num_nodes):
                node_timelines[n].append((t, 2 if n in sensing_nodes else 0))
            # collisions also occupy the medium (approx 1 slot)
            channel_busy_until = t + max(1.0, tx_time * 0.5)
        # decrement backoffs
        backoff = np.maximum(backoff - 1, 0)

    total_slots = int(max_time)
    # Efficiency defined as successful transmissions / total slots
    efficiency = success_count / total_slots if total_slots else 0.0
    # Throughput as successful packets per time unit (slots)
    throughput = success_count / total_slots if total_slots else 0.0
    # Utilization = fraction of slots where the channel was non-idle (success or collision)
    busy_slots = sum(1 for e, _ in usage_log if e != "Idle")
    utilization = busy_slots / total_slots if total_slots else 0.0

    return usage_log, success_count, collision_count, efficiency, throughput, utilization, node_timelines

# --------------------- PLOTTING: per-node Gantt timeline ---------------------
def plot_node_gantt(node_timelines, max_time):
    colors = {0: '#d3d3d3', 1: '#32CD32', 2: '#FF6347'}
    labels = {0: 'Idle', 1: 'Successful Transmission', 2: 'Collision'}

    fig, ax = plt.subplots(figsize=(12, 0.6 * len(node_timelines) + 1))
    max_t = 0
    for i, (node, timeline) in enumerate(sorted(node_timelines.items())):
        for t, state in timeline:
            ax.barh(i, 1, left=t, color=colors[state], height=0.6)
            if t > max_t:
                max_t = t
    ax.set_xlabel("Time Slot")
    ax.set_ylabel("Node")
    ax.set_title("Node-level Activity Timeline (Gantt view)", fontsize=13, pad=8)
    ax.set_xlim(0, max(max_time, max_t + 1))
    ax.set_yticks(range(len(node_timelines)))
    ax.set_yticklabels([f"Node {n}" for n in sorted(node_timelines.keys())])
    ax.grid(axis='x', alpha=0.25)
    legend_patches = [Patch(color=colors[k], label=labels[k]) for k in sorted(labels.keys())]
    ax.legend(handles=legend_patches, loc='upper right', frameon=True)
    st.pyplot(fig)

# --------------------- COMPARISON (multi-run averaging to stabilize) ---------------------
def run_compare(protocols, runs, **kwargs):
    effs, thrs, utils = [], [], []
    for proto in protocols:
        proto_effs = []
        proto_ths = []
        proto_utils = []
        for r in range(runs):
            seed = np.random.randint(0, 2**31 - 1)
            _, s_cnt, c_cnt, eff, thr, util, _ = simulate_csma(
                kwargs['num_nodes'], kwargs['num_packets'],
                kwargs['prop_delay'], kwargs['tx_time'],
                kwargs['gen_prob'], proto, seed=seed, max_time=kwargs.get('max_time', 400)
            )
            proto_effs.append(eff)
            proto_ths.append(thr)
            proto_utils.append(util)
        # average across runs
        effs.append(np.mean(proto_effs))
        thrs.append(np.mean(proto_ths))
        utils.append(np.mean(proto_utils))
    return effs, thrs, utils

# --------------------- MAIN EXECUTION ---------------------
if run_simulation:
    st.spinner("Running simulation...")
    # single run for user-selected protocol timeline
    # use a random seed for variety on each run
    seed0 = np.random.randint(0, 2**31 - 1)
    usage, success, collisions, efficiency, throughput, utilization, node_timeline = simulate_csma(
        num_nodes, num_packets, prop_delay, tx_time, packet_gen_prob, protocol_type, seed=seed0, max_time=400
    )

    # Metrics
    st.subheader("Simulation Results")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Successful Transmissions", success)
    c2.metric("Collisions", collisions)
    c3.metric("Efficiency", f"{efficiency*100:.2f}%")
    c4.metric("Throughput (pkts/slot)", f"{throughput:.4f}")

    st.divider()

    # Node-level Gantt timeline (clear)
    st.subheader("Channel Activity Timeline (per node)")
    plot_node_gantt(node_timeline, max_time=400)

    # Event table (aggregate)
    st.subheader("Event Table (aggregate per timeslot)")
    df = pd.DataFrame(usage, columns=["Event", "Time Slot"])
    st.dataframe(df, use_container_width=True)
    st.download_button("Download Event Data (CSV)", df.to_csv(index=False), "csma_event_table.csv", "text/csv")

    st.divider()

    # Comparison across protocols (averaged)
    if compare_protocols:
        st.subheader("Protocol Performance Comparison (averaged)")
        protocols = ["1-Persistent CSMA", "Non-Persistent CSMA", "p-Persistent CSMA (CSMA/CD)"]
        effs, thrs, utils = run_compare(
            protocols, compare_runs,
            num_nodes=num_nodes, num_packets=num_packets,
            prop_delay=prop_delay, tx_time=tx_time,
            gen_prob=packet_gen_prob, max_time=400
        )

        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        # Efficiency %
        axes[0].bar(protocols, [e * 100 for e in effs], color=["#3498DB", "#E67E22", "#2ECC71"])
        axes[0].set_ylabel("Efficiency (%)")
        axes[0].set_title("Efficiency (avg)")
        axes[0].set_ylim(0, 100)
        for i, v in enumerate(effs):
            axes[0].text(i, v * 100 + 1, f"{v*100:.1f}%", ha='center', fontweight='bold')

        # Throughput
        axes[1].bar(protocols, thrs, color=["#3498DB", "#E67E22", "#2ECC71"])
        axes[1].set_ylabel("Throughput (pkts/slot)")
        axes[1].set_title("Throughput (avg)")
        max_thr = max(thrs) if thrs else 1.0
        axes[1].set_ylim(0, max_thr * 1.4)
        for i, v in enumerate(thrs):
            axes[1].text(i, v + max_thr*0.02, f"{v:.4f}", ha='center', fontweight='bold')

        # Utilization %
        axes[2].bar(protocols, [u * 100 for u in utils], color=["#3498DB", "#E67E22", "#2ECC71"])
        axes[2].set_ylabel("Channel Utilization (%)")
        axes[2].set_title("Channel Utilization (avg)")
        axes[2].set_ylim(0, 100)
        for i, v in enumerate(utils):
            axes[2].text(i, v * 100 + 1, f"{v*100:.1f}%", ha='center', fontweight='bold')

        plt.tight_layout()
        st.pyplot(fig)

        # Download comparison CSV
        comp_df = pd.DataFrame({
            "Protocol": protocols,
            "Avg Efficiency (%)": [round(e * 100, 3) for e in effs],
            "Avg Throughput (pkts/slot)": [round(t, 6) for t in thrs],
            "Avg Utilization (%)": [round(u * 100, 3) for u in utils]
        })
        st.download_button("Download Comparison Data (CSV)", comp_df.to_csv(index=False),
                           "csma_protocol_comparison.csv", "text/csv")

else:
    st.info("Adjust parameters in the sidebar and click Run Simulation to start.")
    st.markdown("""
    ### Notes
    - 1-Persistent: transmits immediately when medium free (aggressive).
    - Non-Persistent: waits a random time before sensing again (reduces collisions).
    - p-Persistent (CSMA/CD): transmits with probability p when medium is free (balance).
    """)

st.divider()
st.markdown("""
<div style="text-align: center;">
    <p style="font-size: 0.9rem; color: #666;">
        Developed for Computer Networks Project | CSMA & CSMA/CD Simulator<br>
    </p>
</div>
""", unsafe_allow_html=True)