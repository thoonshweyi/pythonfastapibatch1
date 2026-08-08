import os
import uuid
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load .env
load_dotenv()

# Hugging Face client
client = InferenceClient(
    api_key="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"
)

# Image output folder
output_dir = Path("generated_images")
output_dir.mkdir(exist_ok=True)


def generate_image(prompt: str):
    try:
        # Generate image
        image = client.text_to_image(
            prompt=prompt,
            model="black-forest-labs/FLUX.1-schnell"
        )

        # Generate unique filename
        filename = f"{uuid.uuid4()}.png"

        # Full path
        file_path = output_dir / filename

        # Save image
        image.save(file_path)

        # Return saved file path
        return str(file_path)

    except Exception as e:
        print("Error:", e)
        return None


# -----------------------------
# Example
# -----------------------------

prompt = "A cute cat sitting in a coffee shop"

file_path = generate_image(prompt)

if file_path:
    print("Image generated successfully!")
    print("File:", file_path)
