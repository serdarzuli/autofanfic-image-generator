# 🧠 AutoFanfic - AI-Powered Fan Fiction Video Generator

AutoFanfic is an open-source, AI-powered application that generates short fictional videos based on user-written prompts. It extracts characters, generates dialogues, creates high-quality images (via Stable Diffusion), and assembles everything into a complete video with captions using MoviePy.

---

## 🚀 Features

- ✍️ **Prompt Input**: User writes a short scene idea or story
- 👥 **Character Detection**: Automatically extracts names and topics
- 🗨️ **Dialogue Generation**: AI writes conversations
- 🖼️ **Image Creation**: High-quality character visuals via Stable Diffusion
- 🎞️ **Video Composition**: Combines visuals + dialogues + subtitles
- 🧑‍🎨 **Avatar to Anime**: Upload your own photo and turn into an anime version (experimental)

---

## 📁 Folder Structure (Clean Architecture)

```
autofanfic-video-generator/
├── backend/
│   ├── app.py                  # FastAPI entry point
│   ├── routes.py               # API endpoints
│   ├── generator/
│   │   ├── sd_client.py        # Stable Diffusion logic
│   │   ├── dialogue_creator.py
│   │   ├── image_generator.py
│   │   ├── video_composer.py
│   │   └── test.py
│   ├── utils/
│   │   ├── text_utils.py
│   │   └── file_handler.py
│   └── animegan/
│       ├── infer.py            # Avatar conversion logic
├── frontend/
│   └── streamlit_app.py        # Streamlit UI
├── static/
│   ├── images/                 # Generated images
│   └── videos/                 # Final video outputs
├── models/                     # AnimeGAN models, etc.
├── requirements.txt            # Dependencies
├── .gitignore
└── README.md
```

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/autofanfic-video-generator.git
cd autofanfic-video-generator
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## ▶️ Usage

**1. Start backend**
```bash
cd backend
uvicorn app:app --reload
```

**2. Start frontend**
```bash
cd frontend
streamlit run streamlit_app.py
```

---

## ✅ Requirements

- Python 3.10+
- torch (with or without CUDA)
- diffusers
- moviepy
- transformers
- fastapi
- streamlit
- PIL, numpy, OpenCV
- ImageMagick, FFmpeg (system tools)

---

## 🔒 License

This project uses open-source tools such as:
- [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) — Open license
- CodeFormer (Face Restoration) — **Licensed under S-Lab License 1.0**

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss what you would like to change.

---

## 📷 Example Prompt

> "Goku and Naruto talk to each other while floating above the clouds."

---

## 📌 Future Ideas

- 🔁 Random Fanfic Story Generator
- 🧑‍🎨 Upload Avatar and Animate
- 🌍 Choose Background Themes
- 🎙️ Add Voice-to-Caption / Dubbing Option

---

## 🌐 Author

Created with ❤️ by Serdar Zuli — Powered by Open Source AI ✨

