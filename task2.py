import google.generativeai as genai
import streamlit as st
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up your Gemini API key
gemini_api_key = "YOUR-GEMINI-API-KEY"  # Enter your Gemini API key here in inverted commas
genai.configure(api_key=gemini_api_key)

# Function to fetch demanding degrees
def fetch_demanding_degrees():
    try:
        prompt = "Recommend some of the degrees to pursue from college which are in demand nowadays."
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error fetching demanding degrees: {e}")
        st.error("Sorry, we couldn't fetch the demanding degrees at this time.")
        return "Error: Unable to fetch demanding degrees."

# Function to fetch locations for a degree
def fetch_location(degree):
    try:
        prompt = f"Recommend places for pursuing {degree} degree."
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error fetching locations: {e}")
        st.error("Sorry, we couldn't fetch the locations at this time.")
        return "Error: Unable to fetch locations."

# Function to fetch colleges for a degree and location
def fetch_colleges(degree, location):
    try:
        prompt = f"Give the best colleges for {degree} degree at {location}."
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error fetching colleges: {e}")
        st.error("Sorry, we couldn't fetch the recommended colleges at this time.")
        return "Error: Unable to fetch recommended colleges."

# Function to fetch admission procedure for a college
def fetch_procedure(college, degree, location):
    try:
        prompt = f"Give procedure, requirements and deadlines for the admission in {college} college at {location} for {degree} degree."
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error fetching procedure: {e}")
        st.error("Sorry, we couldn't fetch the admission procedure at this time.")
        return "Error: Unable to fetch admission procedure."

# Function to get response for a user's question
def get_response(user_input, context):
    try:
        prompt = f"{context} {user_input}"
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        st.error("Sorry, we couldn't generate a response at this time.")
        return "Error: Unable to generate response."

# Function to fetch admission-related information based on query and context
def get_admission_info(query, context):
    try:
        prompt = f"{context} {query}"
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        logging.error(f"Error fetching information: {e}")
        st.error("Sorry, I couldn't fetch the information at this time.")
        return "Error: Unable to fetch information."

# Function to reset session context
def reset_context():
    if 'context' in st.session_state:
        st.session_state.context = ""
        st.write("Context has been reset.")
    else:
        st.warning("Context was not set yet.")

# Main function to run the Streamlit app
def main():
    st.title("AdmitBot - College Admission Q&A Bot")
    st.write("Welcome to AdmitBot! Let's guide you through your college admission journey.")

    if 'context' not in st.session_state:
        st.session_state.context = ""
    
    user_name = st.text_input("What is your name?", key="name")

    if user_name:
        st.write(f"Hello, {user_name}! Let's start with some recommendations.")
        
        if st.button("Fetch Demanding Degrees"):
            demanding_degrees = fetch_demanding_degrees()
            st.write("Some of the demanding degrees to pursue from colleges are:")
            st.write(demanding_degrees)

        degree = st.text_input("What is your desired degree to pursue?", key="degree")

        if degree:
            if st.button("Fetch Favourable Locations for this Degree"):
                favourable_locations = fetch_location(degree)
                st.write(f"Some of the favourable places to pursue {degree} degree are:")
                st.write(favourable_locations)

            location = st.text_input("What is your desired location of college?", key="location")

            if location:
                if st.button("Fetch Recommended Colleges at this Location"):
                    recommended_colleges = fetch_colleges(degree, location)
                    st.write(f"Here are some recommended colleges for you in {location}:")
                    st.write(recommended_colleges)

                college = st.text_input("What is your desired college?", key="college")

                if college:
                    if st.button("Fetch Admission Procedure of this College"):
                        procedure = fetch_procedure(college, degree, location)
                        st.write(f"Here are procedure, requirements, and deadlines for the admission in {college} college:")
                        st.write(procedure)

                    st.write("Now you can ask questions related to admissions (write Done to end):")
                    
                    user_input = st.text_area("Enter your question:", key="user_input")

                    if st.button("Get Response"):
                        if user_input.lower() != "done":
                            response = get_response(user_input, st.session_state.context)
                            st.write(f"*You:* {user_input}")
                            st.write(f"*Bot:* {response}")
                        else:
                            st.write("Thank you for using EduAdvisor. Signing off with warm wishes for your bright future ahead!")
                            
        st.write("*Quick Information:*")
        if st.button("General Admission Information"):
            general_info = get_admission_info("Provide general information about college admissions.", st.session_state.context)
            st.write(general_info)
        if st.button("Admission Deadlines"):
            deadlines = get_admission_info("What are the admission deadlines?", st.session_state.context)
            st.write(deadlines)
            
        if st.button("Reset Context"):
            reset_context()

if __name__ == "__main__":
    main()
