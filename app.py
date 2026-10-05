import streamlit as st
from PIL import Image
from ocr import extract_text
from safety_checker import check_safety
st.set_page_config(
    page_title="PharmaSafe AI",
    page_icon="💊",
    layout="centered"
)
st.title("PharmaSafe AI")
st.subheader("Medicine Label Safety Checker")
st.write(
    "Upload a medicine label image to extract important safety information "
    "and identify missing safety details."
)
uploaded_file = st.file_uploader(
    "Upload Medicine Label",
    type=["jpg", "jpeg", "png"]
)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(
        image,
        caption="Uploaded Medicine Label",
        use_container_width=True
    )
    if st.button("Check Medicine Label"):
        with st.spinner("Reading medicine label..."):
            extracted_text = extract_text(image)
        st.subheader("Extracted Label Information")
        if extracted_text:
            st.text_area(
                "OCR Result",
                extracted_text,
                height=200
            )
            information, warnings = check_safety(extracted_text)
            st.subheader("Safety Information")
            if information:
                for item in information:
                    st.success(item)
            st.subheader("Safety Warnings")
            if warnings:
                for warning in warnings:
                    st.warning(warning)
            else:
                st.success("No missing safety information was detected.")
        else:
            st.error(
                "Could not read the medicine label. "
                "Please upload a clearer image."
            )