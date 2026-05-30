import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained model
model = tf.keras.models.load_model(
    "model/crop_disease_model.h5"
)

# Disease labels
labels = [
    "Tomato Early Blight",
    "Tomato Late Blight",
    "Healthy"
]

# Prediction function
def predict(image):

    image = image.resize((128,128))

    img = np.array(image) / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    predicted_class = np.argmax(prediction)

    disease = labels[predicted_class]

    # Recommendation system
    if disease == "Tomato Early Blight":
        recommendation = (
            "Use fungicide and avoid overwatering."
        )

    elif disease == "Tomato Late Blight":
        recommendation = (
            "Remove infected leaves immediately."
        )

    else:
        recommendation = (
            "Crop appears healthy."
        )

    return disease, recommendation

# Gradio Interface
interface = gr.Interface(
    fn=predict,

    inputs=gr.Image(type="pil"),

    outputs=[
        gr.Textbox(label="Detected Disease"),
        gr.Textbox(label="Recommendation")
    ],

    title="AgriSense AI",

    description="AI Powered Agriculture Intelligence App"
)

# Launch app
interface.launch()