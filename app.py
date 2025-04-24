<<<<<<< HEAD
import streamlit as st
from PIL import Image
from ultralytics import YOLO

# Load your model
model = YOLO('model/best.pt')  # Make sure your model file is in a "model" folder

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
=======
import streamlit as st
from PIL import Image
from ultralytics import YOLO

# Load your model
model = YOLO('model/best.pt')  # Make sure your model file is in a "model" folder

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
>>>>>>> bce392979b6fc5664e78516ffb28dc2fb18f8f96
