import streamlit as st
from PIL import Image
from predict import predict

# Page config
st.set_page_config(page_title="Cat vs Dog Classifier", layout="centered")

st.title("Cat vs Dog Classifier")
st.write("Upload an image and the model will predict whether it's a **cat or dog**")

# Upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)

    # Show image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        label, confidence = predict(image)

        # Clean label formatting
        label = label.lower()

        # Emoji mapping
        emoji = "🐶" if "dog" in label else "🐱"

        # Result box
        st.markdown("### Prediction Result")
        st.success(f"{emoji} **{label.upper()}**")

        # Confidence bar
        st.progress(float(confidence))

        # Confidence text
        st.write(f"Confidence: **{confidence:.2%}**")

        # Interpretation message
        if confidence > 0.85:
            st.info("Very confident prediction")
        elif confidence > 0.65:
            st.warning("Moderately confident")
        else:
            st.error("Low confidence - Try another image")
