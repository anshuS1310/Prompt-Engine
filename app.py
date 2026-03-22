import torch
import gradio as gr
from PIL import Image
import whisper
from transformers import AutoProcessor, AutoModelForImageTextToText

processor = AutoProcessor.from_pretrained("deepseek-community/Janus-Pro-1B")
model = AutoModelForImageTextToText.from_pretrained("deepseek-community/Janus-Pro-1B")
whisper_model = whisper.load_model("base")

def build_instruction(user_text):
    return f"""
You are a professional AI prompt engineer.

Convert the input into a highly detailed AI generation prompt.

Include:
- Subject
- Environment
- Summary

Make it visually rich and optimized for all existing AI models.
The Prompt should e detailed prompt about words ranging from 50 to 70.

Input: {user_text}

Return only the final prompt.
"""
def text_to_prompt(user_text):
    instruction = build_instruction(user_text)
    
    inputs = processor(
        text=instruction,
        return_tensors="pt"
    ).to(model.device)

    input_len = inputs.input_ids.shape[1]
    output = model.generate(**inputs, max_new_tokens=150) 
    generated_tokens = output[0][input_len:]

    return processor.decode(generated_tokens, skip_special_tokens=True)

def image_text_to_prompt(image_path, user_text):
    image = Image.open(image_path)
    instruction = build_instruction(user_text)

    inputs = processor(
        images=image,
        text=instruction,
        return_tensors="pt"
    ).to(model.device)

    input_len = inputs.input_ids.shape[1]
    output = model.generate(**inputs, max_new_tokens=150)
    generated_tokens = output[0][input_len:]

    return processor.decode(generated_tokens, skip_special_tokens=True)

def audio_to_prompt(audio_path):
    result = whisper_model.transcribe(audio_path)
    text = result["text"]
    return text_to_prompt(text)

def generate_prompt_ui(input_type, text, image, audio):

    if input_type == "Text":
        return text_to_prompt(text)

    elif input_type == "Image + Text":
        if image is None:
            return "Please upload an image"
        return image_text_to_prompt(image, text)

    elif input_type == "Audio":
        if audio is None:
            return "Please upload audio"
        return audio_to_prompt(audio)

    return "Invalid input"

with gr.Blocks() as app:

    gr.Markdown("# 🧠 AI Prompt Generator")

    input_type = gr.Radio(
        ["Text", "Image + Text", "Audio"],
        label="Select Input Type"
    )

    text_input = gr.Textbox(label="Enter your idea/prompt")

    image_input = gr.Image(type="filepath", label="Upload Image")

    audio_input = gr.Audio(type="filepath", label="Upload Audio")

    output = gr.Textbox(label="Generated Prompt")

    generate_btn = gr.Button("Generate Prompt 🚀")

    def update_inputs(choice):
        return (
            gr.update(visible=(choice == "Text" or choice == "Image + Text")),
            gr.update(visible=(choice == "Image + Text")),
            gr.update(visible=(choice == "Audio"))
        )
    input_type.change(
        fn=update_inputs,
        inputs=input_type,
        outputs=[text_input, image_input, audio_input]
    )
    generate_btn.click(
        fn=generate_prompt_ui,
        inputs=[input_type, text_input, image_input, audio_input],
        outputs=output
    )

app.launch()