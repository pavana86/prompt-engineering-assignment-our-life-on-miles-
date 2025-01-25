import openai
import streamlit as st

# OpenAI API Key (Replace with your actual key)
openai.api_key = "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"

# Updated Function for OpenAI API
def get_openai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=300
    )
    return "Mocked response: This is your travel itinerary."
# Streamlit App
st.title("AI-Powered Travel Planner")
st.write("Create your personalized travel itinerary!")

# User Inputs
destination = st.text_input("Destination", "Paris")
budget = st.selectbox("Budget", ["Economy", "Moderate", "Luxury"])
trip_duration = st.slider("Trip Duration (Days)", 1, 14, 5)
purpose = st.selectbox("Purpose", ["Relaxation", "Adventure", "Cultural", "Business"])
preferences = st.text_area("Any specific preferences (dietary, walking tolerance, etc.)", "Hidden gems, vegetarian food")

# Generate Itinerary Button
if st.button("Generate Itinerary"):
    with st.spinner("Creating your travel itinerary..."):
        messages = [
            {"role": "system", "content": f"You are an AI travel assistant. Generate a travel itinerary for the following inputs:\n"
                                          f"Destination: {destination}\n"
                                          f"Budget: {budget}\n"
                                          f"Trip Duration: {trip_duration} days\n"
                                          f"Purpose: {purpose}\n"
                                          f"Preferences: {preferences}\n"
                                          f"Provide detailed day-by-day activities, attractions, and dining options."}
        ]
        itinerary = get_openai_response(messages)

        st.subheader("Your Travel Itinerary")
        st.text(itinerary)
