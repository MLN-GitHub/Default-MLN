import streamlit as st
from PIL import Image

def main_page():
    st.title("Image Captioning System")
    # st.write("Select the Model")
    # st.write("Please select an option from the dropdown below:")
    
    # Define the options for the dropdown list
    options = ["Scratch CNN + LSTM", "ResNet + LSTM", "ResNetFineTuned + LSTM", "ResNetFineTuned2 + LSTM", "ResNetFineTuned2 + Attention without LRS + LSTM", "ResNetFineTuned2 + Attention with LRS + LSTM"]

    # Create the selectbox (dropdown list)
    selected_option = st.selectbox("Select a model:", options)

    # Display the selected option
    st.write(f"You selected: **{selected_option}**")

    if st.button("Upload Image"):
        # do nothing
        x = 1
    
    if st.button("Capture New Image"):
        # do nothing
        x = 2
   
    # Option 1: Display an image from a local file
    try:
        image = Image.open("Rugby.jpg") # Replace with your image file path
        st.image(image, caption="Rugby.jpg", width=220)
    except FileNotFoundError:
        st.warning("Local image 'Rugby.jpg' not found. Please ensure it's in the same directory.")
    
    st.write("Caption generated successfully:")
    st.write("a football player in a red uniform is running in a field hockey . <EOS> . <EOS> . <EOS> . ")

    # st.subheader("More Content")
    # st.write("This is a dummy section to demonstrate more content on the page.")
    # st.write("You can add various Streamlit widgets and elements here.")
    # st.write("This is a simple main page created with Streamlit.")
    # st.subheader("Features:")
    # st.write("- Displaying text")
    # st.write("- Using Streamlit widgets")
    # st.button("Click Me!")

def about_page():
    st.title("About This Dummy App")
    st.write("This application demonstrates a multi-page setup in Streamlit.")
    st.write("It's a basic example to showcase navigation between pages.")
    st.info("Built with Streamlit and Python.")

# Main application logic for multi-page setup
page_selection = st.sidebar.selectbox(
    "Choose a page:",
    ("Main Page", "About Page")
)

if page_selection == "Main Page":
    main_page()
elif page_selection == "About Page":
    about_page()
