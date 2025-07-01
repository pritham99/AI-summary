# 🚀 Quick Start Guide

Get your AI Research Assistant running in 5 minutes!

## ⚡ Super Quick Setup

### 1. Get Groq API Key (Free)
- Go to [Groq Console](https://console.groq.com/)
- Sign up for an account
- Get your API key from the dashboard

### 2. Set API Key
```toml
# .streamlit/secrets.toml
CROQAI_API_KEY = "your_groq_api_key_here"
```

### 3. Install & Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### 4. Start Researching!
- Open your browser to `http://localhost:8501`
- Enter any topic (e.g., "AI in Healthcare")
- Click "Generate Research Report"
- Get comprehensive insights! 📊

## 🌐 Deploy Online (Free)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2. Deploy on Streamlit Cloud
- Go to [Streamlit Cloud](https://streamlit.io/cloud)
- Connect your GitHub account
- Create new app → Select your repo → Deploy

### 3. Add API Key to Secrets
- In your deployed app → Settings → Secrets
- Add:
  ```toml
  CROQAI_API_KEY = "your_groq_api_key_here"
  ```

### 4. Share Your App! 🎉
Your app will be live at: `https://YOUR_APP_NAME-YOUR_USERNAME.streamlit.app`

## 🎯 Example Topics to Try

- "Artificial Intelligence in Healthcare"
- "Blockchain Technology Trends 2024"
- "Renewable Energy Solutions"
- "Cybersecurity Best Practices"
- "Machine Learning Applications"
- "Digital Transformation Strategies"

## 🆘 Need Help?

- Run `python deploy.py` for step-by-step guidance
- Check the full [README.md](README.md) for detailed instructions
- Make sure your Groq API key is valid and has quota

---

**Happy Researching! 🔍📚** 