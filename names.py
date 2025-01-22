import streamlit as st
import os
import pandas as pd
import google.generativeai as genai
from openpyxl import load_workbook

# Set up Google AI API key
os.environ["AI_API_KEY"] = ""  # Replace with your actual API key
genai.configure(api_key=os.environ["AI_API_KEY"])

# Create the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 512,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Cache API responses
@st.cache_data
def fetch_raga_details_cached(raga_name):
    """Fetch additional details for a raga using the Gemini API and cache the result."""
    try:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(f"Provide a detailed description of the raga {raga_name}.")
        return response.text
    except Exception as e:
        return f"Error fetching details for {raga_name}: {e}"

# Load data from Excel file
@st.cache_data
def load_raga_data(file_path):
    """Load raga names from the Excel file and return as a list."""
    try:
        df = pd.read_excel(file_path, header=None)
        ragas = df.iloc[:, 0].dropna().unique()
        return list(ragas)
    except Exception as e:
        return f"Error loading data from file: {e}"

# Set the page layout to wide mode
st.set_page_config(layout="wide")

# Title and description of the app
st.title("Raga Information Finder 🎵")
st.markdown(
    """
    Welcome to the Raga Information Finder! Select a raga from the list to learn more about it.
    """
)

# Specify the path to your Excel file (update the path as needed)
file_path = "C://Users//Pranit//PycharmProjects//EDI_PART4//app.xlsx"  # Replace with the correct path

if os.path.exists(file_path):
    with st.spinner('Loading ragas...'):
        # Load raga data
        ragas = load_raga_data(file_path)
        if isinstance(ragas, str):
            st.error(ragas)  # Display error message if data loading failed
        elif ragas:
            # Allow user to select a raga
            selected_raga = st.selectbox("Select a Raga 🔍", ragas)
            if selected_raga:
                st.write(f"### You selected: **{selected_raga}**")
                st.markdown("---")

                # Fetch and display details for the selected raga
                with st.spinner(f"Fetching details for {selected_raga}..."):
                    raga_details = fetch_raga_details_cached(selected_raga)
                if raga_details:
                    st.write(f"### Detailed Description for Raga: {selected_raga}")
                    st.write(raga_details)
                else:
                    st.error("Sorry, we couldn't fetch the details for this raga. Please try again later.")
        else:
            st.warning("No ragas found in the provided Excel file.")
else:
    st.warning("The specified file path does not exist. Please check the path.")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #3B8D99;
        color: white;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
