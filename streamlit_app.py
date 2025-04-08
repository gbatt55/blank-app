import streamlit as st
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🔋 Rare Earth Market Cap Estimator")

# --- Companies & Factors ---
companies = ['MP', 'USARE', 'UUUU', 'LYC', 'NEO', 'ARU']
factors = ['VI', 'Ops', 'Jur', 'Ph', 'Eb', 'Rev', 'DoD', 'Pen_No_VI', 'Pen_Exec_conc']
allocations = {
    'VI': 2000, 'Ops': 750, 'Jur': 150, 'Ph': 200,
    'Eb': 200, 'Rev': 500, 'DoD': 200,
    'Pen_No_VI': -1500, 'Pen_Exec_conc': -500
}

# --- Default Weights (Adjustable) ---
default_weights = {
    'MP':    [0.9, 0.7, 0.7, 1.0, 0.75, 0.5, 1.0, 0.0, 0.15],
    'USARE': [0.7, 0.1, 0.3, 1.0, 0.33, 0.5, 0.25, 0.25, 0.6],
    'UUUU':  [0.6, 0.1, 0.1, 0.75, 0.25, 0.75, 0.75, 0.4, 0.8],
    'LYC':   [0.9, 0.8, 0.8, 1.0, 0.9, 0.8, 1.0, 0.0, 0.1],
    'NEO':   [0.0, 1.0, 1.0, 0.1, 0.75, 0.8, 1.0, 0.9, 0.1],
    'ARU':   [0.1, 0.2, 0.2, 0.5, 0.33, 0.5, 0.25, 0.2, 0.4],
}

# --- Market Cap Data ---
cap_actual = [3900, 770, 730, 4200, 210, 228]

# --- Build Table for Editing ---
df_weights = pd.DataFrame(default_weights, index=factors).T
st.subheader("📊 Adjust Company Scores")
editable_df = st.data_editor(df_weights, num_rows="fixed", use_container_width=True)

# --- Calculate Estimated Market Cap ---
est_mcap = []
for _, row in editable_df.iterrows():
    score = sum(row[f] * allocations[f] for f in factors)
    est_mcap.append(score)

# --- Compile Results ---
results_df = pd.DataFrame({
    'Company': companies,
    'Actual Mcap': cap_actual,
    'Mcap CALC': est_mcap
})
results_df['Delta'] = results_df['Mcap CALC'] - results_df['Actual Mcap']
results_df['% Delta'] = (results_df['Delta'] / results_df['Actual Mcap'] * 100).round(1)

st.subheader("📈 Valuation Results")
st.dataframe(results_df, use_container_width=True)
