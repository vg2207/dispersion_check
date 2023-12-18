import streamlit as st

start_camera = st.button("Start Camera", type="secondary", use_container_width=True)
if start_camera:
    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)
