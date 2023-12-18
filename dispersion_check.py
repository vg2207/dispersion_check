import streamlit as st
import cv2
import numpy as np


# start_camera = st.button("Start Camera", type="secondary", use_container_width=True, key='start_camera_button')
# if start_camera:
picture = st.camera_input("Take a picture")

if picture is not None:
    # To read image file buffer with OpenCV:
    bytes_data = picture.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_GRAYSCALE)
    st.image(cv2_img)
    st.write(cv2_img)


    _, edged = cv2.threshold(cv2_img, 20, 255, cv2.THRESH_BINARY)
    # cv2.imshow("(Edged)", edged)
    # cv2.waitKey(0)
    cnts, _ = cv2.findContours(
        # does this need to be changed?
        edged,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )
    print(f"Cnts Simple Shape (1): {cnts[0].shape}")
    print(f"Cnts Simple Shape (2): {cnts[0].shape}")
    cnts2, _ = cv2.findContours(
        # does this need to be changed?
        edged,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE,
    )
    print(f"Cnts NoApprox Shape:{cnts2[0].shape}")
    print(cnts)
    canvas = np.ones(cv2_img.shape)
    cv2.drawContours(canvas, cnts, -1, (0, 255, 255), 1)
    st.image(canvas)
    # cv2.imshow("Contour", canvas)
    # cv2.waitKey(0)
    st.write(f"Found {len(cnts)} shapes!")

    st.image(picture)
