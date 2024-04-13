
import streamlit as st
import cv2
import face_recognition as frg
import yaml 
from utils import recognize, build_dataset
# Path: code\app.py

st.set_page_config(layout="wide")
#Config
cfg = yaml.load(open('config.yaml','r'),Loader=yaml.FullLoader)

st.sidebar.title("Settings")
button_start = st.sidebar.button("START")
#Infomation section 
st.sidebar.title("Staff Information")
name_container = st.sidebar.empty()
id_container = st.sidebar.empty()
name_container.info('Name: Unnknown')
id_container.success('ID: Unknown')
    
if button_start:
    st.title("CAMERA MAIN CONTROLLING ACCESS")
    #Camera Settings
    cam = cv2.VideoCapture(0)
    FRAME_WINDOW = st.image([])
    while True:
        ret, frame = cam.read()
        if not ret:
            st.error("Failed to capture frame from camera")
            st.info("Please turn off the other app that is using the camera and restart app")
            st.stop()
        image, name, id = recognize(frame,0.3)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #Display name and ID of the person
        name_container.info(f"Name: {name}")
        id_container.success(f"ID: {id}")
        FRAME_WINDOW.image(image)

with st.sidebar.form(key='my_form'):
    st.title("Developer Section")
    submit_button = st.form_submit_button(label='REBUILD DATASET')
    if submit_button:
        with st.spinner("Rebuilding dataset..."):
            build_dataset()
        st.success("Dataset has been reset")