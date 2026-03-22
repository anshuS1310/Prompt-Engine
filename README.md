# 🧠 Prompt Engine

A powerful AI-based system that converts **text, image, and audio inputs** into **high-quality, structured prompts** for generative AI models like Stable Diffusion, Midjourney, and DALL·E.

---

## 🚀 Features

* ✍️ **Text → Prompt**
  Refines and extends simple prompts into detailed, high-quality prompts.

* 🖼️ **Image + Text → Prompt**
  Understands an image and user intent to generate a descriptive prompt.

* 🎧 **Audio → Prompt**
  Converts speech into text and then generates a refined prompt.

* 🧠 **Multimodal AI (Janus-Pro-1B)**
  Uses a vision-language model for intelligent prompt generation.

* 🎨 **Gradio UI**
  Interactive web interface for easy usage.

---

## 🧩 Architecture

```
Input (Text / Image / Audio)
        ↓
Preprocessing Layer
  (Whisper for audio)
        ↓
Instruction Builder (Prompt Engineering)
        ↓
Janus-Pro-1B Model
        ↓
Post-processing (clean output)
        ↓
Final AI Prompt
```

---

## 🛠️ Tech Stack

* **Python**
* **HuggingFace Transformers**
* **DeepSeek Janus-Pro-1B**
* **OpenAI Whisper (Speech-to-Text)**
* **Gradio (UI)**
* **PyTorch**

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/prompt-generator.git
cd prompt-generator
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the application

```bash
python app.py
```

---

## 🧪 Usage

1. Open the Gradio UI in your browser
2. Select input type:

   * Text
   * Image + Text
   * Audio
3. Provide input
4. Click **Generate Prompt 🚀**
5. Get your refined AI prompt

---

## 🧠 Example

### Input:

```
boy in forest
```

### Output:

```
A cinematic scene of a young boy standing in a dense forest, soft sunlight filtering through tall trees, atmospheric fog, ultra-detailed, 4k, depth of field, masterpiece
```

---

## 📁 Project Structure

```
project/
│
├── app.py                
├── requirements.txt
└── README.md
```

---

## ⚙️ Core Functions

* `text_to_prompt()`
* `image_text_to_prompt()`
* `audio_to_prompt()`
* `generate_universal_prompt()`

---

## ⚠️ Limitations

* Requires GPU for best performance
* Video input not supported (yet)
* Output quality depends on prompt instruction

---

## 🔮 Future Improvements

* 🎥 Video input support
* 🎨 Style selection (anime, cinematic, realistic)
* 📊 Prompt scoring system
* ☁️ Deployment on HuggingFace Spaces

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

---

## 📜 License

This project is open-source under the MIT License.

---

## 👨‍💻 Author

**Anshu Singh**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

