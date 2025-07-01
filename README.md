# 🔍 AI Research Assistant

A powerful AI-powered research assistant that uses LangChain, Groq, and web search to generate comprehensive research reports on any topic.

## ✨ Features

- **🔍 Web Search Integration**: Uses DuckDuckGo search to gather real-time information
- **🤖 AI-Powered Analysis**: Leverages Groq's LLMs for intelligent analysis
- **📊 Structured Reports**: Generates well-formatted reports with multiple sections
- **💾 Research History**: Saves and manages your research history
- **📥 Export Reports**: Download reports in Markdown format
- **🎨 Beautiful UI**: Modern, responsive interface built with Streamlit
- **🚀 Free Deployment**: Ready for deployment on Streamlit Cloud

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Fast, simple UI)
- **Backend**: Python + LangChain + Groq
- **Web Search**: DuckDuckGo Search (Free, no API key needed)
- **Deployment**: Streamlit Community Cloud (100% free)

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed on your system
2. **Groq API Key** (Get one at [Groq Console](https://console.groq.com/))

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Ai-Summary-Agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Groq API key**
   
   **Option A: Streamlit Secrets**
   - Create a file at `.streamlit/secrets.toml` and add:
     ```toml
     CROQAI_API_KEY = "your_groq_api_key_here"
     ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 🌐 Deployment to Streamlit Cloud

### Step 1: Push to GitHub

1. Create a new repository on GitHub
2. Push your code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository and branch
5. Set the main file path to `app.py`
6. Click "Deploy"

### Step 3: Configure Secrets

1. In your deployed app, go to Settings → Secrets
2. Add your Groq API key:
   ```toml
   CROQAI_API_KEY = "your_groq_api_key_here"
   ```

## 📖 How to Use

1. **Enter a Research Topic**: Type any topic you want to research (e.g., "Artificial Intelligence in Healthcare", "Climate Change Solutions")

2. **Generate Report**: Click the "Generate Research Report" button

3. **Wait for Processing**: The app will:
   - Search the web for relevant information
   - Analyze and synthesize the data
   - Generate a comprehensive report

4. **Review Results**: The report includes:
   - Executive Summary
   - Key Findings
   - Detailed Analysis
   - Current Trends
   - Future Outlook
   - Sources and References

5. **Download Report**: Click the download button to save the report as a Markdown file

6. **Access History**: Use the sidebar to view and access previous research reports

## 🎯 Example Topics

- "Artificial Intelligence in Healthcare"
- "Blockchain Technology Trends 2024"
- "Renewable Energy Solutions"
- "Cybersecurity Best Practices"
- "Machine Learning Applications"
- "Digital Transformation Strategies"
- "Sustainable Business Models"
- "Quantum Computing Developments"

## 🔧 Configuration

### Customizing the Model

You can modify the model settings in `app.py`:

```python
def groq_chat(messages, model="llama-2-70b-chat", ...):
    ...
```

### Adding More Search Tools

You can extend the search capabilities by adding more tools to the agent:

```python
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper

# Add Wikipedia tool
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
tools = [search_tool, wikipedia]
```

## 🛡️ Privacy & Security

- **No Data Storage**: Research history is stored only in session memory
- **API Key Security**: API keys are handled securely through Streamlit secrets
- **No Personal Data**: The app doesn't collect or store personal information

## 🐞 Troubleshooting

### Common Issues

1. **"Groq API key not found"**
   - Ensure your API key is set correctly in `.streamlit/secrets.toml`
   - Check that the key is valid and has sufficient quota

2. **"Error creating research agent"**
   - Check your internet connection
   - Ensure all dependencies are installed correctly

3. **"Search results not loading"**
   - DuckDuckGo search might be temporarily unavailable
   - Try again in a few minutes

### Getting Help

- Check the [Streamlit documentation](https://docs.streamlit.io/)
- Review [LangChain documentation](https://python.langchain.com/)
- Open an issue on GitHub for bugs or feature requests

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://langchain.com/)
- AI capabilities from [Groq](https://groq.com/)
- Web search powered by [DuckDuckGo](https://duckduckgo.com/)

---

**Happy Researching! 🔍📚** 