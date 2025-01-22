import streamlit as st
import os
import google.generativeai as genai

# Set up Google AI API key
os.environ["AI_API_KEY"] = "AIzaSyBmUqRqqo3qh3hP3R7Syu8jszN1ObarDzA"
genai.configure(api_key=os.environ["AI_API_KEY"])

# Create the model
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

# Group ragas by raga family
RAGA_FAMILY_DATA = {
    "Bhairav Family": ["Raag Bhairav", "Raag Shree", "Raag Todi"],
    "Asavari Family": ["Raag Asavari", "Raag Marwa", "Raag Bhairavi"],
    "Bhairavi Family": ["Raag Bhairavi", "Raag Desh", "Raag Yaman Bhairavi"],
    "Dhani Family": ["Raag Dhani", "Raag Marwa", "Raag Bilawal"],
    "Todi Family": ["Raag Todi", "Raag Multani", "Raag Miyan ki Todi"],
    "Malhar Family": ["Raag Miyan ki Malhar", "Raag Malhar", "Raag Megh"],
    "Kanada Family": ["Raag Darbari Kanada", "Raag Kanada", "Raag Desh Kanada"],
    "Marwa Family": ["Raag Marwa", "Raag Purvi", "Raag Todi"],
    "Bilawal Family": ["Raag Bilawal", "Raag Yaman", "Raag Bhairav"],
    "Hamsadhwani Family": ["Raag Hamsadhwani", "Raag Shuddha Sarang"],
    "Desh Family": ["Raag Desh", "Raag Deshkar"],
    "Yaman Family": ["Raag Yaman", "Raag Yaman Kalyan"],
    "Vachaspati Family": ["Raag Vachaspati", "Raag Bahar"],
    "Lalit Family": ["Raag Lalit", "Raag Bairagi"]
}

# Cache API responses for efficiency
@st.cache_data
def fetch_raga_family_details(raga_family_name):
    """Fetch additional details for a raga family using the Gemini API and cache the result."""
    try:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(f"Provide insights for the raga family {raga_family_name}.")
        return response.text
    except Exception as e:
        return f"Error fetching details for {raga_family_name}: {e}"

# Page configuration
st.set_page_config(layout="wide", page_title="Raga Family Insights", page_icon="🎶")

# Apply custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #222;
        color: #f1f1f1;
        font-family: 'Poppins', sans-serif;
    }
    .stButton>button {
        background-color: #FF6F61;
        color: white;
        border-radius: 12px;
        font-size: 18px;
        padding: 10px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FF3D34;
    }
    .stSelectbox>div>div>input {
        background-color: #303030;
        color: white;
        border-radius: 8px;
    }
    h1, h2, h3 {
        color: #FF6F61;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("🎶 Raga Family Mapping and Insights")
st.markdown(
    """
    Explore raga families and their corresponding ragas, along with emotional impacts and other details.
    Select a raga family to discover its associated ragas and detailed insights.
    """
)

# Raga Family Selection
selected_family = st.selectbox("Select a Raga Family:", list(RAGA_FAMILY_DATA.keys()))

# Display associated ragas
st.markdown(f"### 🎵 Ragas in the **{selected_family}**")
associated_ragas = RAGA_FAMILY_DATA[selected_family]
for raga in associated_ragas:
    st.write(f"🌟 **{raga}**")

# Fetch and display raga family details
with st.spinner(f"Fetching insights for the {selected_family}..."):
    raga_family_details = fetch_raga_family_details(selected_family)

if raga_family_details:
    st.markdown(f"### 🌟 Insights for **{selected_family}**")
    st.write(raga_family_details)
else:
    st.error(f"Could not fetch details for {selected_family}. Please try again.")

# Expander for additional information
with st.expander("📚 Learn More About Raga Families and Their Ragas"):
    st.write("""
        In Hindustani classical music, ragas are grouped into families based on shared features such as scale, emotion, and performance time.
        Each raga family allows exploration of emotional depth within a framework while maintaining the uniqueness of each raga.
    """)

st.markdown("### **Glossary**")
st.write("""
- **Raga Family**: A group of ragas sharing common characteristics.
- **Raga**: A melodic framework in Indian classical music with specific notes and improvisation rules.
- **Thaat**: The parent scale used to derive ragas.
- **Ang**: A characteristic style or feature used to classify ragas.
""")