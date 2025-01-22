import streamlit as st
import os
import google.generativeai as genai

# Set up Google AI API key
os.environ["AI_API_KEY"] = ""
genai.configure(api_key=os.environ["AI_API_KEY"])

# Configure the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 512,
        "response_mime_type": "text/plain",
    },
)

# Data: Thaats and their associated ragas
thaat_data = {
    "Bhairav": ["AhirBhairav", "BairagiBhairav", "Bhairav", "Malkouns"],
    "Kalyan": ["Amritvarshini", "Kedar", "Yaman"],
    "Asavari": ["Asavari", "DarbariKanada", "SindhuBhairavi"],
    "Kafi": ["Bageshree", "Bhimpalasi", "Brindavani Sarang", "Megh", "Miamalhar", "Piloo"],
    "Poorvi": ["Basant", "Lalit", "PooriaDhanashri", "Poorvi", "Shree"],
    "Marwa": ["Raga Bhatiyar Marwa That", "Marwa"],
    "Bilawal": ["Bhinnashadaj", "Bihag", "Durga"],
    "Mishra": ["Kirwani"],
    "Todi": ["Madhuvanti", "MiyakiTodi", "Multani"],
    "Khamaj": ["Khamaj", "Sorath"],
}

# Function to fetch raga-thaat details from Gemini API
def fetch_thaat_details(raga_name, thaat_name):
    try:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(f"Provide insights for the raga '{raga_name}' in the '{thaat_name}' thaat.")
        return response.text
    except Exception as e:
        return f"Error fetching details: {e}"

# Streamlit app configuration
st.set_page_config(layout="wide")
st.title("🎶 Raga-Thaat Mapping and Insights")
st.markdown("""
    **Explore ragas and their corresponding thaats, along with emotional impacts and other details.**
    Select a raga to discover its associated thaat and detailed insights.
""")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body { background: linear-gradient(145deg, #66ccff, #3366ff); color: #fff; font-family: Arial, sans-serif; }
    .stApp { padding: 20px; border-radius: 12px; box-shadow: 0 0 15px rgba(0, 0, 0, 0.2); }
    h1 { color: #ffcc00; text-align: center; font-size: 40px; }
    .stSelectbox, .stMarkdown, .stWrite { background-color: #444; border-radius: 8px; padding: 10px; color: white; }
    .stButton>button { background-color: #ffcc00; color: black; border-radius: 8px; transition: 0.3s; }
    .stButton>button:hover { background-color: #ff9900; }
    </style>
    """,
    unsafe_allow_html=True
)

# User Input: Select a Raga
selected_raga = st.selectbox("Select a Raga 🏷️:", [raga for thaat in thaat_data.values() for raga in thaat])

# Determine associated thaat for the selected raga
associated_thaat = next((thaat for thaat, ragas in thaat_data.items() if selected_raga in ragas), None)

if associated_thaat:
    # Display thaat information
    st.markdown(f"### 🎵 {selected_raga} belongs to the **{associated_thaat} Thaat** 🎶")

    # Fetch and display detailed insights
    insights = fetch_thaat_details(selected_raga, associated_thaat)
    st.write(insights or "No additional insights available.")

    # Recommend other ragas from the same thaat
    other_ragas = [raga for raga in thaat_data[associated_thaat] if raga != selected_raga]
    if other_ragas:
        st.markdown("### 🎼 Other Ragas in the Same Thaat:")
        st.write(", ".join(other_ragas))
else:
    st.error("The selected raga does not belong to any defined thaat.")

# Expandable section for learning more about thaats and ragas
with st.expander("📚 Learn More About Thaats and Their Ragas"):
    st.write("""
        In Hindustani classical music, a thaat is a framework that organizes ragas based on shared characteristics.
        - **Raga**: A melodic framework for improvisation and composition.
        - **Thaat**: A group of ragas sharing a common scale and emotional theme.
        - **Emotional Impact**: Each raga and thaat evokes specific emotions and moods.

        Explore the depth and beauty of Indian classical music through its ragas and thaats.
    """)
