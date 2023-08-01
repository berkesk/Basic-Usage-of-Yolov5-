!pip install -q gradio
!pip install -U ultralytics

import cv2
import torchvision.transforms as transforms
import gradio as gr
import cv2
import numpy as np
import torch
def predict(image):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    x = model(image)
    x.print()
    x.show()  
 
app = gr.Interface(
    fn=predict,
    inputs=gr.inputs.Image(type='filepath', label="Image"),
    outputs=gr.outputs.Image(type="filepath", label="Detection"),
    title="Image Detection"
)

app.launch()

