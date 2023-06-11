import streamlit as st
import requests

# Set page title
st.set_page_config(page_title='Random Quote Generator')

# Fetch a random quote from the API
def fetch_quote():
    response = requests.get('https://api.quotable.io/random')
    data = response.json()
    return data['content'], data['author']

# Display the quote on the app
def display_quote(quote, author):
    st.title('Random Quote Generator')
    st.subheader(f'"{quote}"')
    st.write(f"- {author}")

# Create a session state to store the current quote
if 'quote' not in st.session_state:
    st.session_state.quote, st.session_state.author = fetch_quote()

# Display the current quote
display_quote(st.session_state.quote, st.session_state.author)

# Add a "Next" button to fetch and display a new quote
if st.button('Next'):
    st.session_state.quote, st.session_state.author = fetch_quote()
    st.experimental_rerun()
