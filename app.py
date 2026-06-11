import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

from fertilizer import recommend_fertilizer
from irrigation import irrigation_advice

# ==========================
# Load AI Model
# ==========================

model = tf.keras.models.load_model(
    "model/crop_disease_model.h5"
)

labels = [
    "Tomato Early Blight",
    "Tomato Late Blight",
    "Healthy"
]

# ==========================
# Disease Prediction
# ==========================

def predict(image):

    image = image.resize((128, 128))

    img = np.array(image) / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(
        img,
        verbose=0
    )

    predicted_class = np.argmax(prediction)

    disease = labels[predicted_class]

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


# ==========================
# Dashboard
# ==========================

with gr.Blocks(
    title="AgriSense AI"
) as demo:

    gr.Markdown(
        """
        # 🌾 AgriSense AI
        ## AI Powered Agriculture Intelligence Platform
        """
    )

    # ==========================
    # Disease Detection
    # ==========================

    with gr.Tab("🌱 Disease Detection"):

        image_input = gr.Image(
            type="pil",
            label="Upload Crop Leaf Image"
        )

        disease_output = gr.Textbox(
            label="Detected Disease"
        )

        recommendation_output = gr.Textbox(
            label="Recommendation"
        )

        detect_btn = gr.Button(
            "Analyze Crop"
        )

        detect_btn.click(
            fn=predict,
            inputs=image_input,
            outputs=[
                disease_output,
                recommendation_output
            ]
        )

    # ==========================
    # Fertilizer Advisor
    # ==========================

    with gr.Tab("🌾 Fertilizer Advisor"):

        nitrogen = gr.Number(
            label="Nitrogen (N)"
        )

        phosphorus = gr.Number(
            label="Phosphorus (P)"
        )

        potassium = gr.Number(
            label="Potassium (K)"
        )

        fertilizer_output = gr.Textbox(
            label="Recommendation"
        )

        fertilizer_btn = gr.Button(
            "Get Recommendation"
        )

        fertilizer_btn.click(
            fn=recommend_fertilizer,
            inputs=[
                nitrogen,
                phosphorus,
                potassium
            ],
            outputs=fertilizer_output
        )

    # ==========================
    # Irrigation Advisor
    # ==========================

    with gr.Tab("🌦 Irrigation Advisor"):

        city_input = gr.Textbox(
            label="Enter City Name"
        )

        irrigation_output = gr.Textbox(
            label="Irrigation Advice"
        )

        irrigation_btn = gr.Button(
            "Check Weather"
        )

        irrigation_btn.click(
            fn=irrigation_advice,
            inputs=city_input,
            outputs=irrigation_output
        )

# ==========================
# Launch App
# ==========================

demo.launch(
    auth=[
        ("admin", "admin123"),
        ("farmer1", "farmer123"),
        ("student1", "student123")
    ]
)