import streamlit as st

from main import img_segmentation

st.write(
    """
    # Image Segmentation
    """
)

st.subheader("Upload an Image")
img = st.file_uploader("IMG", type=['jpg', 'jpeg', 'png'])
if img:
    _, center_co, _ = st.columns(3)
    with center_co:
        st.image(img)
    st.write('## Segments')
    st.image(img_segmentation(img))
