# YOLOv5 PyTorch HUB Inference (DetectionModels only)
import torch
from PIL import Image
import streamlit as st

model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/best.pt')  # yolov5n - yolov5x6 or custom

#im = 'bottles.jpg'  # file, Path, PIL.Image, OpenCV, nparray, list

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Check if a file was uploaded
if uploaded_file is not None:
    # Process the uploaded file
    image = Image.open(uploaded_file)
    # Perform operations on the image, such as displaying or analyzing
    results = model(image)  # inference
    results.show()
    st.image(image, caption='Uploaded Image')

    if  str(results).find('plastic bottle') == -1:
        st.write('No Plastic Bottle Detected.')
        print('No Plastic Bottle Detected.')
    else:
        st.write('Plastic Bottle Detected!')
        print('Plastic Bottle Detected!')

    if str(results).find('paper') == -1:
        st.write('No Paper Detected.')
        print('No Paper Detected.')
    else:
        st.write('Paper Detected!')
        print('Paper Detected!')