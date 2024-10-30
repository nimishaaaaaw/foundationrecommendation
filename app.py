import streamlit as st
import pandas as pd

# Load Dataset with relative path
df = pd.read_csv("foundation_dataset.csv", encoding="ISO-8859-1")

# Clean the 'Price (INR)' column
df['Price (INR)'] = df['Price (INR)'].replace('[^0-9]', '', regex=True).astype(int)

# App Layout
st.title("💄 Foundation Recommender")
st.markdown("Find the best foundation tailored to your skin type, preferred finish, coverage, and budget!")

# Sidebar Filters
skin_type = st.selectbox("Choose your skin type:", options=["Select your skin type", "Oily", "Dry", "Normal", "Combination"])
finish = st.selectbox("Select your preferred finish:", options=["Select your finish", "Matte", "Dewy", "Natural"])
coverage = st.selectbox("Desired coverage:", options=["Select your coverage", "Low", "Medium", "Full"])
price = st.slider("Set your price range (₹):", 100, 10000, step=100)

# Filter data based on user selections
filtered_df = df[
    ((df['Skin Type'] == skin_type) | (skin_type == "Select your skin type")) &
    ((df['Finish'] == finish) | (finish == "Select your finish")) &
    ((df['Coverage'] == coverage) | (coverage == "Select your coverage")) &
    (df['Price (INR)'] <= price)
]

# Display Results
if st.button("Recommend"):
    if not filtered_df.empty:
        st.write("Here are some foundations that suit your preferences:")
        st.dataframe(filtered_df[['Brand', 'Product Name', 'Finish', 'Coverage', 'Price (INR)']])
    else:
        st.write("Sorry, no foundations found matching your preferences. Try adjusting the filters.")

<style>
    body {
        background-image: url('images/64f61761-3476-48c1-8664-aa15b09be558.webp');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        height: 100vh;
        margin: 0;
    }
    .stButton>button {
        background-color: #ffcccb;
    }
    .stDataFrame {
        font-size: large;
    }
</style>
""", unsafe_allow_html=True)
# Additional Styling
st.markdown("""
<style>
    body {
        background-image: url('images/64f61761-3476-48c1-8664-aa15b09be558.webp');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        height: 100vh; 
        margin: 0;
    }
    .stButton > button {
        background-color: #ffcccb;
    }
    .stDataFrame {
        font-size: large;
    }
</style>
""", unsafe_allow_html=True)



   
