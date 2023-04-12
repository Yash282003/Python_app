import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_webrtc import webrtc_streamer

with st.sidebar:
    choose = option_menu("App Gallery", ["About", "Camera", "Video"],
                         icons=['house', 'camera fill', 'book'],
                         menu_icon="app-indicator", default_index=0,

                         styles={
        "container": {"padding": "200px", "background-color": "grey",
                      "orientation": "horizontal", "color": "green"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee", "color": "green"},
        "nav-link-selected": {"background-color": "red", "color": "black"},
    }
    )

if choose == "About":

    st.title("About the creator")
    st.subheader("Hii,I am Yashika Sharma from the department of Computer Science and Engineering!!!")
elif choose == "Camera":
    str = st.text_input("Enter caption")
    image = st.file_uploader("Please upload an image", type=[
        "png", "jpg", "jpeg", "bmp", "gif"])
    if image is not None:
        st.image(image)
        st.caption(str)

    image = st.camera_input("Please upload an image", key=None)
    if image is not None:
        st.image(image)
        st.caption(str)
elif choose == "Video":
    str = st.text_input("Enter caption")

    video = st.file_uploader("Please upload an video", type=[
                               "mp4", "mov", "wmv", "flv", "avi", "mpg"])
    if video is not None:
            st.video(video)
            st.caption(str)

    webrtc_streamer(key="key")
    st.caption(str)
