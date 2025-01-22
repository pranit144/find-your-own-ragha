import streamlit as st
import os
import google.generativeai as genai

# Set up Google AI API key
os.environ["AI_API_KEY"] = ""
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

# Define raga-mood mapping with features and placeholders for API links
raga_data = {
    "Love, Attractiveness": {
        "ragas": [
            {"name": "Mohana", "description": "Sweet and romantic, with flowing melodies.", "link": "https://example.com/mohana"},
            {"name": "Kalyani", "description": "Graceful and charming, evokes beauty.", "link": "https://example.com/kalyani"},
            {"name": "Kedaram", "description": "Melodic, emphasizing attraction.", "link": "https://example.com/kedaram"},
            {"name": "Mand", "description": "Soothing and romantic.", "link": "https://example.com/mand"},
            {"name": "Suruti", "description": "Delightful and engaging.", "link": "https://example.com/suruti"},
        ],
        "features": "Sweet, romantic, and graceful; these ragas emphasize melodic flow and pleasing ornamentation.",
    },
    "Laughter, Mirth, Comedy": {
        "ragas": [
            {"name": "Desh", "description": "Bright and uplifting.", "link": "https://example.com/desh"},
            {"name": "Hamsadhwani", "description": "Light and cheerful, perfect for joyful moods.", "link": "https://example.com/hamsadhwani"},
            {"name": "Bihag", "description": "Playful and lively.", "link": "https://example.com/bihag"},
            {"name": "Hindolam", "description": "Cheerful, invoking mirth.", "link": "https://example.com/hindolam"},
            {"name": "Malkauns", "description": "Majestic yet playful.", "link": "https://example.com/malkauns"},
        ],
        "features": "Bright, lively, and uplifting; these ragas bring out joy and humor.",
    },
    "Fury, Anger": {
        "ragas": [
            {"name": "Marwa", "description": "Intense and dramatic.", "link": "https://example.com/marwa"},
            {"name": "Bhairavi", "description": "Expresses strong emotions with sharp transitions.", "link": "https://example.com/bhairavi"},
            {"name": "Darbari Kanada", "description": "Serious and intense, evoking power.", "link": "https://example.com/darbarikanada"},
            {"name": "Hamsadhwani", "description": "Forceful and assertive.", "link": "https://example.com/hamsadhwani"},
            {"name": "Bhairav", "description": "Powerful and commanding.", "link": "https://example.com/bhairav"},
        ],
        "features": "Intense, dramatic, and commanding; these ragas emphasize sharp transitions to evoke fury.",
    },
    "Compassion, Mercy": {
        "ragas": [
            {"name": "Bhairavi", "description": "Gentle and tender, full of empathy.", "link": "https://example.com/bhairavi"},
            {"name": "Yaman", "description": "Soothing, with a touch of sorrow.", "link": "https://example.com/yaman"},
            {"name": "Darbari Kanada", "description": "Evokes a sense of deep understanding.", "link": "https://example.com/darbarikanada"},
            {"name": "Kafi", "description": "Soft and empathetic.", "link": "https://example.com/kafi"},
            {"name": "Kharaharapriya", "description": "Full of gentle oscillations, expressing kindness.", "link": "https://example.com/kharaharapriya"},
        ],
        "features": "Slow, tender, and empathetic; these ragas emphasize kindness and compassion.",
    },
    "Disgust, Aversion": {
        "ragas": [
            {"name": "Shivaranjani", "description": "Unsettling and tense.", "link": "https://example.com/shivaranjani"},
            {"name": "Dhanasri", "description": "Eerie and uncomfortable.", "link": "https://example.com/dhanasri"},
            {"name": "Bhairavi", "description": "Tense transitions evoke aversion.", "link": "https://example.com/bhairavi"},
            {"name": "Darbari Kanada", "description": "Tense and dramatic.", "link": "https://example.com/darbarikanada"},
        ],
        "features": "Unsettling and tense; these ragas evoke discomfort and aversion.",
    },
    "Horror, Terror": {
        "ragas": [
            {"name": "Shivaranjani", "description": "Dark and eerie, with an unsettling atmosphere.", "link": "https://example.com/shivaranjani"},
            {"name": "Marwa", "description": "A sense of looming dread, intense and dramatic.", "link": "https://example.com/marwa"},
            {"name": "Darbari Kanada", "description": "Serious, ominous, and grave.", "link": "https://example.com/darbarikanada"},
            {"name": "Bhairavi", "description": "Powerful and haunting, filled with intense emotions.", "link": "https://example.com/bhairavi"},
        ],
        "features": "Dark, eerie, and unsettling; these ragas evoke fear and terror.",
    },
    "Heroic Mood": {
        "ragas": [
            {"name": "Bhairav", "description": "Commanding and strong, invoking heroism.", "link": "https://example.com/bhairav"},
            {"name": "Desh", "description": "Majestic and uplifting, full of grandeur.", "link": "https://example.com/desh"},
            {"name": "Hindolam", "description": "Serene yet powerful, evoking courage.", "link": "https://example.com/hindolam"},
            {"name": "Marwa", "description": "Intense and dramatic, filled with energy.", "link": "https://example.com/marwa"},
        ],
        "features": "Majestic, powerful, and uplifting; these ragas evoke heroism and courage.",
    },
    "Wonder, Amazement": {
        "ragas": [
            {"name": "Yaman", "description": "Soothing and serene, creating a sense of awe.", "link": "https://example.com/yaman"},
            {"name": "Bageshree", "description": "Mysterious and profound, evoking wonder.", "link": "https://example.com/bageshree"},
            {"name": "Bihag", "description": "Intriguing and inspiring, a sense of awe.", "link": "https://example.com/bihag"},
            {"name": "Marwa", "description": "Majestic and powerful, creating wonder.", "link": "https://example.com/marwa"},
        ],
        "features": "Mysterious, awe-inspiring, and profound; these ragas evoke a sense of wonder and amazement.",
    },
    "Peace or Tranquillity": {
        "ragas": [
            {"name": "Hamsadhwani", "description": "Soft, calm, and soothing, perfect for peace.", "link": "https://example.com/hamsadhwani"},
            {"name": "Vasant", "description": "Serene and gentle, evoking a peaceful mood.", "link": "https://example.com/vasant"},
            {"name": "Shree", "description": "Calm and meditative, inducing tranquility.", "link": "https://example.com/shree"},
            {"name": "Yaman", "description": "Gentle and serene, a perfect match for peace.", "link": "https://example.com/yaman"},
        ],
        "features": "Calm, serene, and gentle; these ragas evoke peace and tranquility.",
    },
}

# Cache API responses for optimization
@st.cache_data
def fetch_raga_details_cached(raga_name):
    """Fetch additional details for a raga using the Gemini API and cache the result."""
    try:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(f"Provide insights for the raga {raga_name}.")
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Set wide mode
st.set_page_config(layout="wide")

# Page Header
st.title("Raga Recommendation by Mood 🎶")
st.markdown(
    "## Discover the perfect raga for your current emotional state."
    " Select a mood from the dropdown below to explore the ideal ragas that resonate with it."
)

# User Input
selected_mood = st.selectbox("Select your mood 😊:", list(raga_data.keys()))

# Fetch ragas for the selected mood
selected_data = raga_data[selected_mood]
ragas = selected_data["ragas"]
features = selected_data["features"]

# Display recommended ragas
st.markdown(f"### Recommended Ragas for **{selected_mood}**")
st.write(features)

# Display ragas dynamically with expandable sections
st.markdown("#### Raga List")
for raga in ragas:
    with st.expander(f"🎵 {raga['name']}: {raga['description']}"):
        st.markdown(f"[Listen to {raga['name']}]({raga['link']})")
        with st.spinner(f"Fetching details for {raga['name']}..."):
            details = fetch_raga_details_cached(raga["name"])
        st.write(f"**Details**: {details if details else 'No additional insights available.'}")

# Custom styling
st.markdown(
    """
    <style>
        body {
            background-color: #2C3E50;
            color: #ECF0F1;
        }
        .stButton button {
            background-color: #1ABC9C;
            color: white;
            border-radius: 5px;
        }
        .stExpander {
            background-color: #34495E;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
