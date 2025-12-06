import gradio as gr
from PIL import Image
from inference import run_inference 

def classify(image):
    # Convert uploaded numpy image → PIL image
    pil_img = Image.fromarray(image)

    # Save temp image 
    pil_img.save("temp.png")
    pred = run_inference("temp.png")[0]
    return pred

ui = gr.Interface(
    fn=classify,
    inputs=gr.Image(type="numpy"),
    outputs="text",
    title="Traffic signs Classification",
    description="Upload an image to get the predicted class."
)

ui.launch()