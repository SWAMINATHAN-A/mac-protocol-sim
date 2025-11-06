import streamlit as st
import pandas as pd
import io

# Page configuration
st.set_page_config(
    page_title="Download",
    page_icon="📥",
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
    .download-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .example-box {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
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
    <h1>📥 Download Data & Documentation</h1>
    <p style="font-size: 1.2rem; margin-top: 0.5rem;">
        Export Simulation Results and Project Documentation
    </p>
</div>
""", unsafe_allow_html=True)

# Main content
st.markdown("## 📊 Available Downloads")

st.info("""
**Note:** To download simulation data (inputs, outputs, event logs), you must first run a simulation 
on the CSMA/CD or Slotted ALOHA pages. After running, download buttons will appear on those pages.
""")

st.divider()

# Download Templates and Documentation
st.markdown("## 📄 Project Documentation Templates")

tab1, tab2, tab3 = st.tabs(["Simulation Results Format", "Example: Hamming Code", "Project Templates"])

with tab1:
    st.markdown("""
    ### Simulation Data Export Format
    
    When you download CSV files from the simulators, they contain the following information:
    """)
    
    col_f1, col_f2 = st.columns(2)
    
    with col_f1:
        st.markdown("""
        #### CSMA/CD Event Data Format
        
        **Columns:**
        - `Event`: Type of event (Idle, Busy, Success, Collision)
        - `Time Slot`: Time slot number when event occurred
        
        **Example:**
        ```csv
        Event,Time Slot
        Idle,0
        Success (Node 2),1
        Collision,2
        Busy,3
        ```
        """)
        
        # Create sample CSMA data
        sample_csma = pd.DataFrame({
            'Event': ['Idle', 'Success (Node 2)', 'Collision', 'Busy', 'Success (Node 0)'],
            'Time Slot': [0, 1, 2, 3, 4]
        })
        
        st.dataframe(sample_csma, use_container_width=True)
        
        csv_csma = sample_csma.to_csv(index=False)
        st.download_button(
            "Download Sample CSMA Data",
            csv_csma,
            "sample_csma_events.csv",
            "text/csv"
        )
    
    with col_f2:
        st.markdown("""
        #### Slotted ALOHA Event Data Format
        
        **Columns:**
        - `Slot`: Time slot number
        - `Num Transmissions`: Number of nodes transmitting
        - `Status`: Idle, Success, or Collision
        
        **Example:**
        ```csv
        Slot,Num Transmissions,Status
        0,0,Idle
        1,1,Success
        2,3,Collision
        3,1,Success
        ```
        """)
        
        # Create sample ALOHA data
        sample_aloha = pd.DataFrame({
            'Slot': [0, 1, 2, 3, 4],
            'Num Transmissions': [0, 1, 3, 1, 2],
            'Status': ['Idle', 'Success', 'Collision', 'Success', 'Collision']
        })
        
        st.dataframe(sample_aloha, use_container_width=True)
        
        csv_aloha = sample_aloha.to_csv(index=False)
        st.download_button(
            "Download Sample ALOHA Data",
            csv_aloha,
            "sample_aloha_events.csv",
            "text/csv"
        )

with tab2:
    st.markdown("""
    ### Example: Detailed Step-by-Step Procedure
    
    This example shows how to document your simulation results in detail, 
    similar to the Hamming Code example format.
    """)
    
    st.markdown("""
    <div class="example-box">
        <h4>📝 Example Format: Hamming Code Processing</h4>
        <p><strong>Problem:</strong> Encode the binary data 110011 using Hamming Code</p>
        <p><strong>Input:</strong> 110011</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    #### Step 1: Input Conversion
    
    **Input is already in binary format**
    - Result: Binary: 110011
    - Input format: binary
    - Input value: 110011
    - Binary output: 110011
    - Length: 6 bits
    
    ========================================
    """)
    
    st.markdown("""
    #### Step 2: Input Data Bits
    
    **Received 6 data bits to encode**
    - Result: Data: 110011
    - Binary representation: 110011
    
    ========================================
    """)
    
    st.markdown("""
    #### Step 3: Calculate Parity Bits
    
    **Determine number of parity bits needed**
    - Data bits (m) = 6
    - Parity bits (r) must satisfy: 2^r ≥ m + r + 1
    - Result: r = 4 parity bits needed
    - Total bits = 6 + 4 = 10 bits
    
    ========================================
    """)
    
    st.markdown("""
    #### Step 4: Position Assignment
    
    **Place data and parity bits in positions**
    
    | Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
    |----------|---|---|---|---|---|---|---|---|---|----|
    | Type     | P | P | D | P | D | D | D | P | D | D  |
    | Value    | ? | ? | 1 | ? | 1 | 0 | 0 | ? | 1 | 1  |
    
    - P = Parity bit (to be calculated)
    - D = Data bit
    
    ========================================
    """)
    
    st.markdown("""
    #### Step 5: Calculate Each Parity Bit
    
    **P1 (position 1)** checks positions 1,3,5,7,9...
    - Checks: 1,3,5,7,9 → ?,1,1,0,1
    - XOR: 1⊕1⊕0⊕1 = 1
    - **P1 = 1**
    
    **P2 (position 2)** checks positions 2,3,6,7,10...
    - Checks: 2,3,6,7,10 → ?,1,0,0,1
    - XOR: 1⊕0⊕0⊕1 = 0
    - **P2 = 0**
    
    **P4 (position 4)** checks positions 4,5,6,7...
    - Checks: 4,5,6,7 → ?,1,0,0
    - XOR: 1⊕0⊕0 = 1
    - **P4 = 1**
    
    **P8 (position 8)** checks positions 8,9,10...
    - Checks: 8,9,10 → ?,1,1
    - XOR: 1⊕1 = 0
    - **P8 = 0**
    
    ========================================
    """)
    
    st.markdown("""
    #### Step 6: Final Hamming Code
    
    | Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
    |----------|---|---|---|---|---|---|---|---|---|----|
    | Type     | P | P | D | P | D | D | D | P | D | D  |
    | Value    | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1  |
    
    **Final Encoded Output:** 1011100011
    
    ========================================
    """)
    
    st.markdown("""
    ### 📥 Download This Example
    
    Create a text file with the above step-by-step procedure for your records.
    """)
    
    # Create downloadable text file
    example_text = """
    HAMMING CODE ENCODING EXAMPLE
    ========================================
    
    Input: 110011
    
    Step 1: Input Conversion
    Input is already in binary format
    Result: Binary: 110011
    • Input format: binary
    • Input value: 110011
    • Binary output: 110011
    • Length: 6 bits
    
    Step 2: Input Data Bits
    Received 6 data bits to encode
    Result: Data: 110011
    • Binary representation: 110011
    
    Step 3: Calculate Parity Bits
    Determine number of parity bits needed
    • Data bits (m) = 6
    • Parity bits (r) must satisfy: 2^r ≥ m + r + 1
    • Result: r = 4 parity bits needed
    • Total bits = 6 + 4 = 10 bits
    
    Step 4: Position Assignment
    Place data and parity bits in positions
    Position: 1  2  3  4  5  6  7  8  9  10
    Type:     P  P  D  P  D  D  D  P  D  D
    Value:    ?  ?  1  ?  1  0  0  ?  1  1
    
    Step 5: Calculate Each Parity Bit
    P1 (position 1) checks positions 1,3,5,7,9...
    • Checks: 1,3,5,7,9 → ?,1,1,0,1
    • XOR: 1⊕1⊕0⊕1 = 1
    • P1 = 1
    
    P2 (position 2) checks positions 2,3,6,7,10...
    • Checks: 2,3,6,7,10 → ?,1,0,0,1
    • XOR: 1⊕0⊕0⊕1 = 0
    • P2 = 0
    
    P4 (position 4) checks positions 4,5,6,7...
    • Checks: 4,5,6,7 → ?,1,0,0
    • XOR: 1⊕0⊕0 = 1
    • P4 = 1
    
    P8 (position 8) checks positions 8,9,10...
    • Checks: 8,9,10 → ?,1,1
    • XOR: 1⊕1 = 0
    • P8 = 0
    
    Step 6: Final Hamming Code
    Position: 1  2  3  4  5  6  7  8  9  10
    Type:     P  P  D  P  D  D  D  P  D  D
    Value:    1  0  1  1  1  0  0  0  1  1
    
    Final Encoded Output: 1011100011
    """
    
    st.download_button(
        "Download Hamming Code Example (TXT)",
        example_text,
        "hamming_code_example.txt",
        "text/plain"
    )

with tab3:
    st.markdown("""
    ### Project Documentation Templates
    
    Download these templates to document your simulation results properly.
    """)
    
    col_t1, col_t2 = st.columns(2)
    
    with col_t1:
        st.markdown("""
        #### Simulation Report Template
        
        Use this template to document your simulation runs:
        
        **Sections included:**
        1. Simulation Parameters
        2. Execution Steps
        3. Results and Observations
        4. Performance Analysis
        5. Conclusions
        """)
        
        report_template = """
NETWORK PROTOCOL SIMULATION REPORT
========================================

1. SIMULATION PARAMETERS
----------------------------------------
Protocol: [CSMA/CD / Slotted ALOHA]
Date: [Date]
Duration: [Number of time slots]

Parameters:
• Number of Nodes: [N]
• Transmission Probability: [p]
• Propagation Delay: [delay]
• Transmission Time: [time]

2. EXECUTION STEPS
----------------------------------------
Step 1: Parameter Configuration
[Describe how you set up parameters]

Step 2: Simulation Execution
[Describe how simulation ran]

Step 3: Data Collection
[Describe what data was collected]

3. RESULTS
----------------------------------------
Performance Metrics:
• Throughput (S): [value]
• Efficiency: [value]%
• Success Rate: [value]%
• Collision Rate: [value]%
• Idle Rate: [value]%

4. OBSERVATIONS
----------------------------------------
[Your observations about the results]

5. ANALYSIS
----------------------------------------
[Analysis of why results occurred]

6. CONCLUSIONS
----------------------------------------
[What you learned from this simulation]

========================================
        """
        
        st.download_button(
            "Download Report Template",
            report_template,
            "simulation_report_template.txt",
            "text/plain"
        )
    
    with col_t2:
        st.markdown("""
        #### Comparison Analysis Template
        
        Use this when comparing multiple protocol variants:
        
        **Sections included:**
        1. Protocols Compared
        2. Test Conditions
        3. Results Comparison
        4. Performance Ranking
        5. Recommendations
        """)
        
        comparison_template = """
PROTOCOL COMPARISON ANALYSIS
========================================

1. PROTOCOLS COMPARED
----------------------------------------
• Protocol 1: [Name]
• Protocol 2: [Name]
• Protocol 3: [Name]

2. TEST CONDITIONS
----------------------------------------
Common Parameters:
• Number of Nodes: [N]
• Test Duration: [slots]
• Number of Runs: [runs]

3. RESULTS COMPARISON
----------------------------------------
                    Protocol 1  Protocol 2  Protocol 3
Throughput (S)      [   ]       [   ]       [   ]
Efficiency (%)      [   ]       [   ]       [   ]
Collision Rate (%)  [   ]       [   ]       [   ]
Avg Delay (slots)   [   ]       [   ]       [   ]

4. PERFORMANCE RANKING
----------------------------------------
1st Place: [Protocol] - [Reason]
2nd Place: [Protocol] - [Reason]
3rd Place: [Protocol] - [Reason]

5. OBSERVATIONS
----------------------------------------
[Your observations]

6. BEST USE CASES
----------------------------------------
Protocol 1: Best for [scenario]
Protocol 2: Best for [scenario]
Protocol 3: Best for [scenario]

7. RECOMMENDATIONS
----------------------------------------
[Your recommendations]

========================================
        """
        
        st.download_button(
            "Download Comparison Template",
            comparison_template,
            "comparison_analysis_template.txt",
            "text/plain"
        )

st.divider()

st.markdown("## 📋 How to Use Downloaded Data")

col_u1, col_u2 = st.columns(2)

with col_u1:
    st.markdown("""
    ### Analysis in Excel/Google Sheets
    
    **Steps:**
    1. Download CSV file from simulator
    2. Open in Excel or Google Sheets
    3. Create pivot tables for analysis
    4. Generate additional charts
    5. Calculate custom metrics
    
    **Useful Formulas:**
    ```excel
    Success Rate = COUNTIF(Status,"Success") / COUNT(Status)
    Collision Rate = COUNTIF(Status,"Collision") / COUNT(Status)
    Average Load = AVERAGE(Num_Transmissions)
    ```
    """)

with col_u2:
    st.markdown("""
    ### Analysis in Python
    
    **Sample Code:**
    ```python
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # Load data
    df = pd.read_csv('simulation_results.csv')
    
    # Calculate metrics
    success_rate = (df['Status']=='Success').sum()/len(df)
    
    # Plot
    df['Status'].value_counts().plot(kind='bar')
    plt.title('Slot Status Distribution')
    plt.show()
    ```
    """)

st.divider()

st.markdown("## 💾 Complete Procedure Documentation")

st.markdown("""
<div class="download-card">
    <h3>📖 Step-by-Step Procedure Documentation</h3>
    <p>For complete documentation of your simulation procedure (similar to the Hamming Code example), 
    follow these steps:</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
1. **Run your simulation** on the CSMA/CD or Slotted ALOHA page
2. **Note all parameters** you used
3. **Download the CSV data** using the button on that page
4. **Document each step** following the example format above:
   - Input parameters
   - Processing steps
   - Intermediate results
   - Final outputs
   - Analysis and interpretation
5. **Include visualizations** by taking screenshots of the charts
6. **Write conclusions** based on your observations

**The downloaded CSV file contains:**
- All your inputs (parameters you selected)
- All outputs (simulation results)
- Step-by-step event log (detailed procedure)
""")

# Create comprehensive example
st.markdown("### 📥 Download Complete Documentation Example")

comprehensive_doc = """
NETWORK PROTOCOL SIMULATION - COMPLETE DOCUMENTATION
========================================

SIMULATION: Slotted ALOHA Protocol Analysis

INPUT PARAMETERS:
----------------------------------------
• Number of Nodes (N): 10
• Transmission Probability (p): 0.10
• Number of Time Slots: 1000
• Date: 2024-11-06

STEP 1: PARAMETER SETUP
----------------------------------------
Configured the following parameters:
• Set N = 10 nodes competing for channel access
• Set p = 0.10 (10% transmission probability per slot)
• Set simulation duration = 1000 time slots
• Calculated offered load: G = N × p = 10 × 0.10 = 1.0

========================================

STEP 2: SIMULATION EXECUTION
----------------------------------------
For each time slot (t = 0 to 999):
  1. Each node i generates random number r_i ∈ [0,1]
  2. If r_i < p, node i transmits
  3. Count total transmitting nodes: T_t
  4. Classify slot status:
     - If T_t = 0: Idle
     - If T_t = 1: Success
     - If T_t > 1: Collision
  5. Record event

Example for first 5 slots:
Slot 0: T=0, Status=Idle
Slot 1: T=1, Status=Success (Node 3)
Slot 2: T=3, Status=Collision (Nodes 1,5,7)
Slot 3: T=1, Status=Success (Node 2)
Slot 4: T=0, Status=Idle

========================================

STEP 3: RESULTS COLLECTION
----------------------------------------
Total Slots: 1000

Slot Status Distribution:
• Successful Slots: 368
• Collision Slots: 264
• Idle Slots: 368

Performance Metrics:
• Throughput (S) = 368/1000 = 0.368
• Success Rate = 36.8%
• Collision Rate = 26.4%
• Idle Rate = 36.8%

========================================

STEP 4: THEORETICAL COMPARISON
----------------------------------------
Theoretical Throughput Formula:
S_theory = G × e^(-G)

With G = 1.0:
S_theory = 1.0 × e^(-1.0)
S_theory = 1.0 × 0.3679
S_theory = 0.3679

Simulated Result: S_sim = 0.368
Difference: |0.3679 - 0.368| = 0.0001 (0.03%)

Conclusion: Simulation matches theory very closely!

========================================

STEP 5: PERFORMANCE ANALYSIS
----------------------------------------

Efficiency vs. Theoretical Maximum:
• Theoretical Max = 1/e ≈ 0.368
• Achieved = 0.368
• Efficiency = (0.368/0.368) × 100% = 100.0%

Operating Point Analysis:
• Offered Load G = 1.0 (OPTIMAL)
• This is the maximum throughput point
• System is operating at peak efficiency

Collision Analysis:
• Expected collisions at G=1: ~26%
• Observed collisions: 26.4%
• Matches expected behavior

========================================

STEP 6: VISUALIZATION INTERPRETATION
----------------------------------------

Timeline Diagram Shows:
• Random distribution of transmissions
• No visible patterns (confirms randomness)
• Fair channel access across nodes

Throughput Graph Shows:
• Simulation point on theoretical curve
• Located at peak (G=1, S≈0.368)
• Optimal operating condition confirmed

Slot Distribution Chart Shows:
• Balanced distribution
• Success ≈ Idle ≈ 36-37%
• Collisions ≈ 26%
• Healthy distribution for G=1

========================================

STEP 7: CONCLUSIONS
----------------------------------------

Key Findings:
1. Slotted ALOHA achieves maximum throughput at G=1
2. Simulation accurately matches theoretical predictions
3. At optimal load, efficiency is maximized
4. System exhibits expected random behavior
5. No unfair channel monopolization detected

Practical Implications:
• For N nodes, set p = 1/N for optimal performance
• With 10 nodes, p = 0.10 is ideal
• Higher p causes more collisions, lower throughput
• Lower p causes more idle slots, wasted capacity

Recommendations:
• Maintain offered load around G ≈ 1.0
• Monitor and adjust transmission probability
• Consider load-adaptive protocols for variable traffic

========================================

END OF DOCUMENTATION
"""

st.download_button(
    "📥 Download Complete Simulation Documentation Example",
    comprehensive_doc,
    "complete_simulation_documentation_example.txt",
    "text/plain",
    use_container_width=True
)

st.divider()

# Footer
st.markdown("""
<div style="text-align: center;">
    <p style="font-size: 0.9rem; color: #666;">
        Network Protocol Simulator | Download Center<br>
        Run simulations on CSMA/CD or Slotted ALOHA pages to generate downloadable data!
    </p>
</div>
""", unsafe_allow_html=True)