import streamlit as st
import pandas as pd

# Data setup: converting the given data into a pandas DataFrame
data = {
    "Name": ["AhirBhairav", "Amritvarshini", "Asavari", "Bageshree", "BairagiBhairav",
             "Basant", "Bhairav", "Bhairavi", "Raga Bhatiyar Marwa That", "Bhimpalasi",
             "Bhinnashadaj", "Bihag", "Brindavani Sarang", "DarbariKanada", "Durga",
             "Kedar", "Khamaj", "Kirwani", "Lalit", "Madhuvanti", "Malkouns", "Marwa",
             "Megh", "Miamalhar", "MiyakiTodi", "Multani", "Piloo", "PooriaDhanashri",
             "Poorvi", "Shree", "SindhuBhairavi", "Sorath", "Yaman"],
    "Scale": ["S,r,G,M,P,D,n", "S,G,m,P,N", "S,R,g,M,P,d,n", "S,R,g,M,P,D,n", "S,r,M,P,n",
              "S,r,G,M,m,P,d,n", "S,r,G,M,P,d,N", "S,r,g,M,P,d,n", "S,r,G,M,m,P,D,N",
              "S,r,R,g,M,P,D,n", "S,G,M,D,N", "S,R,G,M,m,P,D,N", "S,R,M,P,n,N", "S,R,g,M,P,d,n",
              "S,R,M,P,D", "S,R,G,M,m,P,D,N", "S,R,G,M,P,D,d,n,N", "S,R,g,M,P,d,N",
              "S,r,G,M,m,d,N", "S,R,g,m,P,D,N", "S,g,M,d,n", "S,r,G,m,D,N", "S,R,M,P,n",
              "S,R,g.M,P,D,n,N", "S,r,g,m,P,d,N", "S,r,g,m,P,d,N", "S,R,g,G,M,P,d,D,n,N",
              "S,r,G,m,P,d,N", "S,R,G,M,m,P,D,N", "S,R,G,M,m,P,D,N", "S,R,M,P,D,n,N",
              "S,R,G,m,P,D,N"],
    "Thaat": ["Bhairav", "Kalyan", "Asavari", "Kafi", "Bhairav", "Poorvi", "Bhairav", "Bhairavi",
              "Marwa", "Kafi", "Bilawal", "Bilawal", "Kafi", "Asavani", "Bilawal", "Kalyan",
              "Khamraj", "Mishra", "Poorvi", "Todi", "Bhairavi", "Marwa", "Kafi", "Kafi", "Todi",
              "Todi", "Kafi", "Poorvi", "Poorvi", "Poorvi", "Asavari", "Khamaj", "Kalyan"],
    "Number of Notes": ["Seven", "Five", "Seven", "Seven", "Five", "Seven", "Seven", "Seven",
                        "Seven", "Seven", "Five", "Seven", "Five", "Six", "Five", "Six", "Seven",
                        "Seven", "Five", "Seven", "Seven", "Six", "Six", "Seven", "Seven", "Seven",
                        "Seven", "Seven", "Seven", "Seven", "Seven", "Seven", "Seven", "Seven"],
    "Family": ["Bhairav", "Nil", "Asavari", "Nil", "Bhairav", "Sarang", "Bhairav", "Bhairavi",
               "Nil", "Dhanashri", "Nil", "Bihag", "Sarang", "Kanada", "Nil", "Kedar", "Nil",
               "Nil", "Nil", "Nil", "Kouns", "Nil", "Malhar", "Malhar", "Todi", "Nil", "Nil",
               "Nil", "Nil", "Bhairavi", "Nil", "Nil", "Kalyan"],
    "Time": ["4a.m. - 7a.m.", "7 p.m. - 10 p.m.", "10 a.m. - 1 p.m.", "10p.m. - 1a.m.", "4a.m. - 7a.m.",
             "4a.m. - 7a.m.", "4a.m. - 7a.m.", "4a.m. - 7a.m.", "4a.m. - 7a.m.", "1a.m. - 4p.m.",
             "10p.m. - 1a.m.", "10p.m. - 1a.m.", "10a.m. - 1p.m.", "10p.m. - 1a.m.", "10p.m. - 1a.m.",
             "7p.m. - 10p.m.", "7p.m. - 10p.m.", "1a.m. -4a.m.", "4a.m. - 7a.m.", "1p.m. - 4p.m.",
             "1a.m. -4a.m.", "4p.m. - 7p.m.", "10p.m. - 1a.m.", "10p.m. - 1a.m.", "10a.m. - 1p.m.",
             "4p.m. - 7p.m.", "1p.m. - 4p.m.", "4p.m. - 7p.m.", "4p.m. - 7p.m.", "4p.m. - 7p.m.",
             "10a.m. - 1p.m.", "10p.m. - 1a.m.", "7p.m. - 10p.m."]
}

# Ensure that all columns have the same length
max_length = max(len(value) for value in data.values())
for key, value in data.items():
    if len(value) < max_length:
        # Padding with None if the list is shorter
        value.extend([None] * (max_length - len(value)))

# Create DataFrame from the data
df = pd.DataFrame(data)

# Set the page config only once at the top
st.set_page_config(page_title="Raga Information", page_icon="🎶", layout="wide")

# Streamlit app interface
st.title("Explore Indian Ragas 🎶")

# Sidebar for additional features or instructions
st.sidebar.header("About the App")
st.sidebar.write(""" 
    Explore the different Indian Ragas, their scales, family, time of performance, and other interesting details. 
    Select a Raga from the dropdown to learn more about it.
""")

# Dropdown to select the Name
st.subheader("Select a Raga:")
name_selected = st.selectbox("Choose a Raga", df["Name"])

# Filter data based on the selected Name
selected_raga = df[df["Name"] == name_selected].iloc[0]

# Display the details in a single column
st.markdown(f"### **{selected_raga['Name']}**")
st.markdown(f"**Scale**: {selected_raga['Scale']}")
st.markdown(f"**Thaat**: {selected_raga['Thaat']}")
st.markdown(f"**Number of Notes**: {selected_raga['Number of Notes']}")
st.markdown(f"**Family**: {selected_raga['Family']}")
st.markdown(f"**Time of Performance**: {selected_raga['Time']}")

# Custom Styling with Modern CSS for Music Player Look
st.markdown("""
    <style>
        body {
            background-color: #2E2E2E;
            color: #F5F5F5;
            font-family: 'Arial', sans-serif;
        }
        .stTitle {
            color: #1DB954; /* Green like Spotify */
        }
        .stSelectbox {
            background-color: #121212;
            color: #F5F5F5;
            border-radius: 8px;
            border: 1px solid #333;
        }
        .stSelectbox:hover {
            background-color: #333;
        }
        .stMarkdown {
            font-family: 'Arial', sans-serif;
            color: #B0B0B0;
        }
        .stButton {
            background-color: #1DB954;
            color: white;
            border-radius: 12px;
            font-weight: bold;
        }
        .stButton:hover {
            background-color: #1ED760;
        }
        .stSidebar {
            background-color: #121212;
            color: #F5F5F5;
        }
        .stSidebarHeader {
            font-size: 20px;
            font-weight: bold;
        }
        .stExpanderHeader {
            font-size: 16px;
            color: #B0B0B0;
        }
    </style>
""", unsafe_allow_html=True)
