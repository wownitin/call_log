import streamlit as st
import pdfplumber
import pandas as pd
import matplotlib.pyplot as plt

st.title("📞 Call Log Analyzer")

uploaded_file = st.file_uploader("Upload your call log PDF", type="pdf")

if uploaded_file:
    all_tables = []
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)

    df = pd.concat(all_tables, ignore_index=True)
    df['Duration'] = pd.to_timedelta(df['Duration'], errors='coerce')
    df['Name'] = df['Name'].str.replace(r'^\+91', '', regex=True)
    names_with_valid_duration = df[df['Duration'] > pd.Timedelta(seconds=0)]['Name'].unique()
    final_df = df[~df['Name'].isin(names_with_valid_duration)]

    # ✅ Now it's safe to use final_df here
    st.subheader("📊 Call Duration Histogram")
    fig, ax = plt.subplots()
    final_df['Duration'].dt.total_seconds().plot.hist(bins=10, ax=ax)
    ax.set_xlabel("Duration (seconds)")
    ax.set_title("Distribution of Call Durations")
    st.pyplot(fig)
