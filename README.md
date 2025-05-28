# 🧠 AutoFanfic - AI-Powered Fan Fiction Image Generator

AutoFanfic is an open-source, AI-powered application that generates high-quality fictional images based on user-written prompts. It combines advanced AI technologies to create engaging fan fiction visuals with minimal user input.

---

## 🚀 Features

- ✍️ **Prompt Input**: Write a short scene idea or story.
- 👥 **Character Detection**: Automatically extracts names and topics from the prompt.
- 🖼️ **Image Creation**: Produces high-quality visuals using Stable Diffusion.
- 🧑‍🎨 **Avatar to Anime**: Transform your photo into an anime-style avatar (experimental).

---

## 📁 Folder Structure

```
autofanfic-image-generator/
├── backend/
│   ├── app.py                  # FastAPI entry point
│   ├── routes.py               # API endpoints
│   ├── generator/
│   │   ├── sd_client.py        # Stable Diffusion logic
│   │   ├── image_generator.py  # Image creation logic
│   │   └── test.py             # Unit tests
│   ├── utils/
│   │   ├── text_utils.py       # Text processing utilities
│   │   └── file_handler.py     # File management utilities
├── frontend/
│   └── streamlit_app.py        # Streamlit-based user interface
├── static/
│   ├── img/                    # Generated images
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

---

## 🛠️ Installation

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/serdarzuli/autofanfic-image-generator.git
   cd autofanfic-image-generator
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### 1. Start the Backend

Navigate to the `backend` folder and run the FastAPI server:
```bash
cd backend
uvicorn app:app --reload
```

### 2. Start the Frontend

Navigate to the `frontend` folder and launch the Streamlit app:
```bash
cd frontend
streamlit run streamlit_app.py
```

---

## ✅ Requirements

- Python 3.10+
- torch (with or without CUDA)
- diffusers
- transformers
- fastapi
- streamlit
- PIL, numpy, OpenCV
- ImageMagick (system tool)

---

## 📷 Example Prompt

> "Goku and Naruto floating above the clouds."
<img width="345" alt="Screenshot 2025-04-28 163101" src="https://github.com/user-attachments/assets/97934696-b18a-4d97-a6ac-6b78d7425b1a" />

---

## 📌 Future Ideas

- 🔁 Random Fanfic Story Generator
- 🧑‍🎨 Upload Avatar and Animate
- 🌍 Choose Background Themes

---

## 🤝 Contributing

Contributions are welcome! Please open an issue to discuss your ideas or submit a pull request.

---

## 🔒 License

This project uses open-source tools such as:
- [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) — Open license
- CodeFormer (Face Restoration) — **Licensed under S-Lab License 1.0**

---

## 🌐 Author

Created with ❤️ by Serdar Zuli — Powered by Open Source AI ✨

