import os
import requests
import streamlit as st
from PIL import Image
from ultralytics import YOLO

# Download model if not already present
model_path = "model/best.pt"
if not os.path.exists(model_path):
    os.makedirs("model", exist_ok=True)
    url = "https://drive.google.com/uc?id=10tdWPlq_UsjRrCxORsni4w_Wsj-thoeJ"  # Replace with your actual Google Drive link
    with open(model_path, "wb") as f:
        f.write(requests.get(url).content)

# Load your model
model = YOLO(model_path)  # Load the model after download

st.title("Sign Language Detection App")
st.write("Upload an image to detect sign language gestures.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Run detection
    st.write("Detecting signs...")
    results = model.predict(image)

    # Show results
    result_img = results[0].plot()
    st.image(result_img, caption="Detection Result", use_container_width=True)
