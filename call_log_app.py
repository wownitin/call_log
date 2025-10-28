import streamlit as st
import pdfplumber
import pandas as pd
import matplotlib.pyplot as plt  # ✅ Add this at the top

st.title("📞 Call Log Analyzer")

# File upload and PDF parsing
uploaded_file = st.file_uploader("Upload your call log PDF", type="pdf")
if uploaded_file:
    # ... extract and clean data ...
    # final_df = your filtered DataFrame

    # ✅ Add your Matplotlib chart here
    st.subheader("📊 Call Duration Histogram")
    fig, ax = plt.subplots()
    final_df['Duration'].dt.total_seconds().plot.hist(bins=10, ax=ax)
    ax.set_xlabel("Duration (seconds)")
    ax.set_title("Distribution of Call Durations")
    st.pyplot(fig)

    # CSV download button
    csv = final_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "filtered_calls.csv", "text/csv")
