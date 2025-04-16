import streamlit as st
import random
import requests

# Website Title
st.set_page_config(page_title="My Streamlit Website", layout="wide")
st.title("🚀 My Awesome Python Website")

# Sidebar Navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Fun Facts", "Image Upload", "Contact", "Weather"])

# Dark Mode Toggle
dark_mode = st.sidebar.checkbox("🌙 Dark Mode")
if dark_mode:
    st.markdown("<style>body { background-color: #1e1e1e; color: white; }</style>", unsafe_allow_html=True)

# ---------------------- Home Page ----------------------
if page == "Home":
    st.header("🏠 Welcome to My Website")
    st.write("This is a cool, interactive website built with Python & Streamlit! 🚀")

    # User Input for Greeting
    name = st.text_input("Enter your name:", "")
    if name:
        st.success(f"Hello, {name}! Welcome to my site. 😊")

# ---------------------- Fun Facts Page ----------------------
elif page == "Fun Facts":
    st.header("🎉 Fun Facts")
    
    facts = [
        "Python was named after the comedy show *Monty Python's Flying Circus*!",
        "The first website was published in 1991 by Tim Berners-Lee.",
        "The Eiffel Tower can be 15 cm taller in summer due to expansion!",
        "Octopuses have three hearts and blue blood!",
        "The shortest war in history lasted 38-45 minutes!"
    ]

    if st.button("Click for a Random Fact!"):
        st.info(random.choice(facts))

# ---------------------- Image Upload Page ----------------------
elif page == "Image Upload":
    st.header("🖼️ Upload Your Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.success("Image uploaded successfully!")

# ---------------------- Contact Page ----------------------
elif page == "Contact":
    st.header("📞 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            if name and email and message:
                st.success(f"Thank you, {name}! Your message has been received. 😊")
            else:
                st.error("Please fill in all the fields!")

# ---------------------- Weather Page (Optional) ----------------------
elif page == "Weather":
    st.header("🌦️ Check the Weather")
    
    city = st.text_input("Enter your city:", "")
    api_key = "your_openweathermap_api_key"  # Replace with a real API key from OpenWeatherMap
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    if st.button("Get Weather"):
        if city:
            response = requests.get(weather_url)
            if response.status_code == 200:
                data = response.json()
                temperature = data["main"]["temp"]
                weather_description = data["weather"][0]["description"]
                st.success(f"🌡️ Temperature in {city}: {temperature}°C \n🌤️ Condition: {weather_description.capitalize()}")
            else:
                st.error("City not found. Please check the spelling.")
        else:
            st.warning("Please enter a city name.")

# ---------------------- Footer ----------------------
st.markdown("---")
st.markdown("🔹 Built with ❤️ using Streamlit")
