import streamlit as st
import os
import google.generativeai as genai

# Set up Google AI API key
os.environ["AI_API_KEY"] = "AIzaSyCQ3Yyeb9JJkPi9EvLh_S4TattSXRVxnoM"
genai.configure(api_key=os.environ["AI_API_KEY"])

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 1024,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Define raga-time mapping with emotional impacts and features
raga_data_by_time = {
    "4 AM - 6 AM": {
        "ragas": [
            {"name": "Bhupala", "description": "Peaceful and devotional, invoking a sense of calm.",
             "emotional_impact": "Calms the mind, promoting spiritual reflection."},
            {"name": "Revagupti", "description": "A raga with a rich, majestic feeling.",
             "emotional_impact": "Inspires devotion and a sense of grandeur."},
            {"name": "Bauli", "description": "Soft and gentle, evoking a serene atmosphere.",
             "emotional_impact": "Promotes peaceful contemplation."},
            {"name": "Malayamaruta", "description": "Bright and uplifting, invoking joy.",
             "emotional_impact": "Elicits feelings of optimism and joy."},
            {"name": "Valaji", "description": "Subtle and serene, with an air of peacefulness.",
             "emotional_impact": "Induces tranquility and calmness."},
            {"name": "Desakshi", "description": "Majestic, yet meditative.",
             "emotional_impact": "Creates an uplifting and reflective mood."},
        ],
        "features": "Majestic, peaceful, and devotional ragas that help foster serenity and joy during the early morning hours."
    },
    "6 AM - 9 AM": {
        "ragas": [
            {"name": "Bilahari", "description": "Bright and uplifting, with a hint of playfulness.",
             "emotional_impact": "Promotes energy and joy."},
            {"name": "Kedaram", "description": "Melancholic yet soothing, evoking deep reflection.",
             "emotional_impact": "Induces introspection and peace."},
            {"name": "Dhanyasi", "description": "Calm and soothing, evoking a sense of peace.",
             "emotional_impact": "Creates tranquility and focus."},
        ],
        "features": "Bright and peaceful ragas that help evoke positivity and calmness in the morning."
    },
    "9 AM - 12 PM": {
        "ragas": [
            {"name": "Asaveri", "description": "Energetic and majestic, invoking a sense of awe.",
             "emotional_impact": "Promotes a sense of wonder and invigoration."},
            {"name": "Saveri", "description": "Slightly serious, yet joyful.",
             "emotional_impact": "Brings clarity and joy to the listener."},
            {"name": "Devamanohari", "description": "Soft and devotional, invoking deep emotions.",
             "emotional_impact": "Fosters devotion and emotional balance."},
        ],
        "features": "Majestic and devotional ragas that bring balance and joy to the morning."
    },
    "12 PM - 1 PM": {
        "ragas": [
            {"name": "Sriraga", "description": "Soft and serene, with a gentle, soothing effect.",
             "emotional_impact": "Promotes peace and clarity."},
            {"name": "Madhyamavati", "description": "Bright and devotional, evoking a sense of piety.",
             "emotional_impact": "Creates a peaceful, devotional atmosphere."},
            {"name": "Manirangu", "description": "Playful and joyful, with a touch of sadness.",
             "emotional_impact": "Elicits joy, tinged with nostalgia."},
        ],
        "features": "Soothing, joyful ragas that balance devotion and lightness."
    },
    "1 PM - 4 PM": {
        "ragas": [
            {"name": "Mukhari", "description": "Serious and contemplative, with a meditative quality.",
             "emotional_impact": "Induces deep thought and reflection."},
            {"name": "Begada", "description": "Bright and lively, with an energetic feel.",
             "emotional_impact": "Energizes the mind and body."},
        ],
        "features": "Serious yet energetic ragas that inspire focus and mental clarity."
    },
    "4 PM - 7 PM": {
        "ragas": [
            {"name": "Vasanta", "description": "Lively and uplifting, evoking a sense of joy.",
             "emotional_impact": "Brings a sense of freshness and happiness."},
            {"name": "Natakurunji", "description": "Majestic and regal, evoking awe.",
             "emotional_impact": "Promotes focus and introspection."},
            {"name": "Purvakalyani", "description": "Bright and uplifting, invoking cheerfulness.",
             "emotional_impact": "Generates positivity and joy."},
        ],
        "features": "Lively and joyful ragas that uplift the spirit during the late afternoon and early evening."
    },
    "7 PM - 10 PM": {
        "ragas": [
            {"name": "Neelambari", "description": "Calm and serene, invoking peace.",
             "emotional_impact": "Creates a peaceful, reflective atmosphere."},
            {"name": "Kedaragaulai", "description": "Soothing, with a tinge of sadness.",
             "emotional_impact": "Induces introspection and tranquility."},
        ],
        "features": "Soothing ragas that calm the mind and promote peaceful reflection in the evening."
    },
    "All Times": {
        "ragas": [
            {"name": "Bhairavi", "description": "Emotional and devotional, filled with depth.",
             "emotional_impact": "Elicits intense feelings of devotion and longing."},
            {"name": "Kambhogi", "description": "Serene and calming, with an emotional touch.",
             "emotional_impact": "Creates a soothing, meditative environment."},
            {"name": "Shankarabharanam", "description": "Majestic and regal, uplifting and energetic.",
             "emotional_impact": "Invokes a sense of grandeur and power."},
            {"name": "Kalyani", "description": "Serene and graceful, evoking beauty and calm.",
             "emotional_impact": "Promotes peace and emotional balance."},
        ],
        "features": "Universal ragas that fit all times of day, providing calm, devotion, and grandeur."
    }
}


def fetch_raga_details(raga_name):
    """Fetch additional details for a raga using the Gemini API."""
    try:
        # Use the Gemini API for generating insights for the raga
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(f"Provide insights for the raga {raga_name}.")
        return response.text  # Extracts and returns the text from the response
    except Exception as e:
        st.error(f"Error fetching details for {raga_name}: {e}")
        return None


# Page Header
st.set_page_config(layout="wide", page_title="Raga Recommendation")  # Set wide layout
st.markdown("""
    <style>
        /* Custom Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        /* Global Styles */
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #121212;
            color: #f5f5f5;
        }

        .css-1d391kg {
            background-color: #1d1f25;
        }

        h1 {
            color: #E50914;
        }

        h3 {
            color: #f5f5f5;
        }

        /* Custom Button */
        .stButton>button {
            background-color: #E50914;
            color: white;
            font-size: 16px;
            border-radius: 12px;
            padding: 12px 24px;
            transition: 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #B4070A;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }

        /* Expandable Section */
        .css-1cpxqw2 {
            background-color: #262626;
            color: #f5f5f5;
        }

        .stSelectbox>div>div>input {
            background-color: #2e2e2e;
            color: white;
            border: 1px solid #E50914;
        }

        .stSelectbox>div>div>div>div {
            background-color: #262626;
        }

        .css-vk3zhk {
            background-color: #121212;
        }

        .stTable>div {
            background-color: #262626;
            color: white;
        }

        /* Header and Footer */
        .stHeader {
            background-color: #121212;
        }
    </style>
""", unsafe_allow_html=True)

# Page content
st.title("🎶 Raga Recommendation by Time of Day")
st.markdown("""
    **Discover the perfect raga to match the time of day and your emotional state.**  
    Select the time of day from the dropdown to explore the ideal ragas that resonate with it.
""")

# User Input
selected_time = st.selectbox("Select the time of day 🌞🌜:", list(raga_data_by_time.keys()))

# Fetch ragas for the selected time
selected_data = raga_data_by_time[selected_time]
ragas = selected_data["ragas"]
features = selected_data["features"]

# Display recommended ragas
st.markdown(f"### Recommended Ragas for **{selected_time}** ⏰")
st.markdown(f"**Key Features:** {features}")

# Add icon with image for visual enhancement
st.image("https://www.example.com/music-icon.png", width=100)  # Replace with your own image URL

# Create a stylish table for displaying raga information
raga_table_data = []

for raga in ragas:
    details = fetch_raga_details(raga["name"]) if fetch_raga_details(
        raga["name"]) else "No additional insights available."
    raga_table_data.append([raga["name"], raga["description"], raga["emotional_impact"], details])

# Display ragas in a table format for cleaner structure
st.table(raga_table_data)

# Optional: Add a collapsible section for detailed insights
with st.expander("📚 Learn More About Ragas and Their Emotional Impact"):
    st.write("""
    Ragas have a profound impact on our emotional state, with each raga being designed to evoke certain feelings.
    Whether it's the peaceful serenity of early morning ragas or the contemplative intensity of late-night ragas, music has the power to transform our mood.
    Explore how different ragas can elevate your day and your emotions.
    """)
