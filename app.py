# YOLOv5 PyTorch HUB Inference (DetectionModels only)
import torch
from PIL import Image
import streamlit as st
import base64
import io

@st.cache_resource
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/best.pt')  # yolov5n - yolov5x6 or custom
    return model

model = load_model()

def string_to_pil_image(image_string):
    decoded_data = base64.b64decode(image_string)
    image_bytes = io.BytesIO(decoded_data)
    pil_image = Image.open(image_bytes)
    return pil_image

def handle_file_upload():
    uploaded_file = st.text_area('Insert Image String')

    # Check if a file was uploaded
    if uploaded_file is not None and uploaded_file!='hello':
        # Process the uploaded file
        try:
            image = string_to_pil_image(uploaded_file)
            results = model(image)  # inference

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
            st.image(image, caption='Uploaded Image')

        except Exception as e:
            print(e)
        
handle_file_upload()