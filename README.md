# QueryCraft: Text-to-SQL using Gemini API

A GenAI-based Streamlit app that converts natural language queries into SQL using Google's Gemini model.

---

## 🚀 Features

- 🔍 Converts text queries into SQL using Gemini Pro
- 🧠 Integrates Google Generative AI (gemini-pro) API
- 🖥️ Built with Streamlit for a clean web interface
- 🔒 Keeps API keys secure using `.env` and `.gitignore`

---

## 📁 Project Structure
gen ai project
├── app.py # Main Streamlit app
├── image/ # Folder containing UI-related images
├── requirements.txt # Python dependencies
├── .env # API Key (not pushed to GitHub)
├── .gitignore # Prevents pushing sensitive files like .env


---

## 🔧 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/mohan-lakshmi-reddy/querycraft-text2sql-using-gemini.git
cd querycraft-text2sql-using-gemini

2. Create .env File
   
GOOGLE_API_KEY=your_gemini_api_key

3.Install Dependencies

pip install -r requirements.txt

▶️ Run the App

streamlit run app.py

🤖 Tech Stack

Python
Streamlit
Google Generative AI (Gemini Pro)
dotenv

## 📜 License

This project is for educational and demonstration purposes only.
