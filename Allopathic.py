import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Health Remedy Finder",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color:#1A76D1 ;
        color: white;
    }
   
    h1{
    color:#1A76D1;
    }
    </style>
    """,unsafe_allow_html=True
)
# Load the dataset from the CSV file
df = pd.read_csv('allopathic_data.csv')


def get_remedy(specific_value):
    if specific_value in df['disease'].values:
        result = df.loc[df['disease'] == specific_value,'drug'].values[0]
        return result
    else:
        return "Sorry! No remedy found for this health issue."

st.title('Allopathic Medicine Finder')

# Auto-suggest widget for disease titles
user_input = st.text_input('Enter a disease:', key='user_input')
filtered_diseases = df['disease'].str.lower().str.contains(user_input.lower())
selected_diseases = st.selectbox('Select Disease:', df[filtered_diseases]['disease'], key='selected_disease')

clear_button = st.button('Clear')
if clear_button:
     user_input=""
     selected_diseases = ""

if st.button('Get Remedies'):
    specific_value = selected_diseases.lower()
    remedy = get_remedy(specific_value)
    st.write(f'Allopathic medicine for {specific_value.capitalize()}: {remedy}')