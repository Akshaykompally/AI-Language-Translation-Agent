# 🌍 AI Language Translator using LangGraph & Mistral AI

An AI-powered language translation application built using **LangGraph**, **LangChain**, and **Mistral AI**. The application translates text into any target language, validates the meaning of the translation, performs grammar correction, and can read the translated text aloud using Text-to-Speech.

---

## 🚀 Features

- 🌐 Translate text into any language
- ✅ Verify translation meaning and tone
- ✍️ Automatically correct grammar and spelling
- 🔊 Text-to-Speech support using `pyttsx3`
- 🧠 Workflow orchestration with LangGraph
- ⚡ Powered by Mistral AI

---

## 🛠️ Tech Stack

- Python 3.10+
- LangChain
- LangGraph
- Mistral AI
- python-dotenv
- pyttsx3

---

## 📂 Project Structure

```
├── main.py             # Translation workflow
├── run.py              # Application runner
├── requirements.txt    # Project dependencies
├── .env                # Environment variables
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Akshaykompally/AI-Language-Translation-Agent.git
```

### 2. Create a virtual environment

Windows

```bash
python -m venv env
env\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_api_key_here
```

Get your API key from:

https://console.mistral.ai/

---

## ▶️ Running the Project

If using `run.py`

```bash
python run.py
```

Or import the translation function inside your own application.

---

## 🧠 Workflow

The application uses a LangGraph pipeline with three AI agents.

```
START
   │
   ▼
Translate Agent
   │
   ▼
Meaning & Tone Validator
   │
   ▼
Grammar Checker
   │
   ▼
END
```

### Step 1 — Translation Agent

- Translates the user's text into the target language.
- Preserves meaning and context.
- Returns only the translated text.

### Step 2 — Meaning & Tone Validation

- Compares the original sentence with the translated output.
- Corrects inaccurate translations.
- Ensures meaning is preserved.

### Step 3 — Grammar Checker

- Corrects grammar and spelling.
- Returns the final polished translation.

---

## 📌 Example

```python
from main import translate, speak

text = "How are you?"
language = "French"

result = translate(text, language)

print(result)

speak(result)
```

Output

```
Comment allez-vous ?
```

The translated text will also be spoken aloud.

---

## 📜 Core Functions

### translate()

```python
translate(user_input, language)
```

Parameters

| Parameter | Description |
|-----------|-------------|
| user_input | Text to translate |
| language | Target language |

Returns

```
Translated and grammar-corrected text
```

---

### speak()

```python
speak(text)
```

Uses `pyttsx3` to convert the translated text into speech.

---

## 📦 Requirements

```
langchain
langgraph
langchain-mistralai
python-dotenv
pyttsx3
```

Install them using

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

- 🎤 Speech-to-Text input
- 🌍 Automatic language detection
- 🖥️ Streamlit web interface
- 📱 Flask/FastAPI REST API
- 🗣️ Multiple voice options
- 📄 Translation history
- 📂 File translation support
- 🎧 Audio file generation

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed using **Python**, **LangGraph**, and **Mistral AI**.
