
# 🧠 Medical Chatbot with LLaMA

This project is a two-part web application that allows users to upload a **medical image** and ask a **natural language question**. The app uses **Meta's LLaMA-4** model via **GROQ API** to generate insightful and context-aware responses by combining image understanding and text interpretation.

## 📸 Key Features

* Upload **medical images** (X-rays, MRIs, scans, etc.)
* Ask natural language **queries** related to the image
* Get intelligent responses from the **LLaMA-4** Vision-Language model
* Beautiful and intuitive **Streamlit frontend**
* Robust **FastAPI backend** for handling image-query communication

---

## Demo
![image](https://github.com/user-attachments/assets/8493965f-1497-46ed-a6e8-2cac195554f4)

![image](https://github.com/user-attachments/assets/088f5382-a56c-4f1d-82a0-5dc5b0a06220)



## 🖼️ Frontend: Streamlit (`app.py`)

* Upload image and input query
* Sends data to backend (`/upload_and_query`) using HTTP POST
* Displays cleaned markdown responses in a readable format

---

## 🧠 Backend: FastAPI (`api.py`)

* Receives image and query via POST
* Verifies image format and base64 encodes it
* Sends request to **GROQ’s LLaMA-4** Vision-Language API
* Returns structured JSON response back to the frontend

---

## 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/KaanSezen1923/medical-chatbot-llama.git
cd medical-chatbot-llama
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set your environment variables**

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
```

4. **Run the backend (FastAPI)**

```bash
uvicorn api:app --reload --port 8000
```

5. **Run the frontend (Streamlit)**

```bash
streamlit run app.py
```

---

## 🗂️ Project Structure

```
medical-chatbot-llama/
├── app.py               # Streamlit frontend
├── api.py               # FastAPI backend
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🧪 Sample Usage

1. Upload a medical image (e.g., MRI scan).
2. Enter a query like:
   **“What abnormalities do you notice in this scan?”**
3. View the AI-generated analysis based on the image and query.






## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

MIT License – see the [LICENSE](LICENSE) file for details.

---

