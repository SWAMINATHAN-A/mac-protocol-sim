# 🛰️ MAC Access Protocols Simulator

### *(Slotted ALOHA, CSMA/CD)*

An interactive **Streamlit-based web application** that simulates and visualizes the performance of two key **Medium Access Control (MAC)** protocols:
**Slotted ALOHA**, **CSMA/CD**.

This simulator helps you understand how multiple nodes compete for a shared communication channel, how collisions occur, and how different access strategies improve throughput and efficiency.

---

## Features

### Interactive Controls

* **Number of Nodes (N)** – Set how many devices share the channel.
* **Transmission Probability (p)** – Set how likely each node is to transmit per time slot.
* **Propagation Delay Factor (α)** – Adjust for CSMA/CD to simulate real propagation effects.
* Real-time metrics:

  * Offered Load: **G = N × p**
  * Throughput (S)
  * Efficiency (%)
  * Channel Utilization (%)

---

### Real-Time Visualizations

#### 1. Throughput vs Offered Load

Plots both:

* The **theoretical curve** for Slotted ALOHA:
  **S = G × e<sup>−G</sup>**
* Your **simulation result** (red dot).
* The **maximum theoretical throughput** (green star) at **G = 1**, where
  **S<sub>max</sub> = 1/e ≈ 0.368 (36.8%)**

#### 2. Time Slot Distribution

Pie chart showing:

* 🟩 Successful transmissions
* 🟥 Collisions
* ⬛ Idle slots

#### 3. Channel Activity Timeline

Color-coded timeline of simulation slots:

* 🟩 Success
* 🟥 Collision
* ⬛ Idle

#### 4. Protocol Performance Comparison

Bar charts comparing:

* Efficiency (%)
* Throughput (packets per time unit)
* Channel Utilization (%)

Protocols compared:

* **1-Persistent CSMA**
* **Non-Persistent CSMA**
* **CSMA/CD**

---

### Download Results

Export the protocol comparison data as a **CSV file** for your report or analysis.

---

## Theory Overview

### Slotted ALOHA

* Time is divided into slots.
* A node transmits **only at the start of a slot**.
* A **success** occurs if exactly one node transmits.
* A **collision** occurs if two or more transmit at once.
* Idle if no node transmits.

**Throughput formula:**

> S = G × e<sup>−G</sup>

**Maximum efficiency:**

> S<sub>max</sub> = 1/e ≈ 0.368 → 36.8%

---

### CSMA (Carrier Sense Multiple Access)

Nodes **listen before transmitting**:

* If channel is idle → transmit immediately.
* If busy → wait and retry according to persistence type.

| Type           | Behavior                                 | Typical Efficiency |
| -------------- | ---------------------------------------- | ------------------ |
| 1-Persistent   | Waits until idle, then transmits         | ~50–60%            |
| Non-Persistent | Waits random backoff before retrying     | ~60–70%            |
| p-Persistent   | Transmits with probability *p* when idle | Tunable            |

**Approximate throughput model:**

> S ≈ (G × e<sup>−aG</sup>) / (1 + 2aG)

where **a = propagation delay / transmission time**.

As **a → 0**, efficiency approaches **100%**.

---

### CSMA/CD (Carrier Sense Multiple Access with Collision Detection)

Used in **Ethernet (IEEE 802.3)**.
Enhances CSMA by **detecting collisions while transmitting**.

When a collision occurs:

1. Transmission stops immediately.
2. A **jam signal** is sent.
3. Node waits for a **random backoff** (Binary Exponential Backoff).

**Efficiency formula:**

> η = 1 / (1 + 5a)

where **a = propagation delay / transmission time**.

**Examples:**

* a = 0.01 → η ≈ 95%
* a = 0.1 → η ≈ 66%

Efficiency falls as propagation delay grows.

---

## Protocol Comparison Summary

| Protocol            | Channel Sensing | Collision Detection | Max Efficiency | Typical Medium   | Example Use     |
| ------------------- | --------------- | ------------------- | -------------- | ---------------- | --------------- |
| Slotted ALOHA       | ❌               | ❌                   | ~36.8%         | Radio/Satellite  | Uplink channels |
| 1-Persistent CSMA   | ✅               | ❌                   | ~55–60%        | Radio            | Simple LANs     |
| Non-Persistent CSMA | ✅               | ❌                   | ~60–70%        | Radio            | Wireless MAC    |
| CSMA/CD             | ✅               | ✅                   | ~80–95%        | Wired (Ethernet) | IEEE 802.3 LANs |

---

## Learning Outcomes

This simulator helps you:

* Visualize **random access protocols** in real time.
* Understand how **carrier sensing** and **collision detection** improve efficiency.
* Compare **ALOHA, CSMA, and CSMA/CD** under identical load.
* Analyze **throughput vs load** and **efficiency trade-offs**.
* Export and report performance metrics easily.

---

## How to Run This Project

1. **Clone the repository:**

   ```bash
   git clone https://github.com/razbearr/basic-mac-protocol-simulation.git
   cd basic-mac-protocol-simulation
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   .\venv\Scripts\activate    # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**

   ```bash
   streamlit run Home.py
   ```

---

## Technologies Used

* **Python 3.x**
* **Streamlit** – Interactive web UI
* **NumPy / Pandas** – Simulation logic
* **Matplotlib / Altair** – Data visualization
* **CSV Export** – Analysis-ready output

---

## Key Mathematical Summary

| Protocol            | Throughput Formula                      | Max Efficiency         |
| ------------------- | --------------------------------------- | ---------------------- |
| Slotted ALOHA       | S = G × e<sup>−G</sup>                  | 1/e ≈ 0.368 (36.8%)    |
| Pure ALOHA          | S = G × e<sup>−2G</sup>                 | 1/(2e) ≈ 0.184 (18.4%) |
| 1-Persistent CSMA   | S ≈ (G × e<sup>−aG</sup>) / (1 + 2aG)   | ~55–60%                |
| Non-Persistent CSMA | S ≈ (G × e<sup>−aG</sup>) / (1 + a + G) | ~60–70%                |
| CSMA/CD             | η = 1 / (1 + 5a)                        | up to ~95%             |

---

## Authors

* **Katyayni Aarya** — [@razbearr](https://github.com/razbearr)
* **Suyesha Saha** — [@suyu101](https://github.com/suyu101)


