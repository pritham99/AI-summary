import streamlit as st
from langchain_community.tools import DuckDuckGoSearchRun
from datetime import datetime
from groq import Groq

# Page configuration
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Futuristic Custom CSS (with visible card instructions and colored name) ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f8fafc 0%, #e0e7ef 100%) !important;
        font-family: 'Segoe UI', 'Roboto', 'Arial', sans-serif;
    }
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #232526;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
        letter-spacing: 2px;
        text-shadow: 0 4px 32px #fff, 0 1.5px 0 #00fff7;
        animation: darkglow 2s infinite alternate;
    }
    @keyframes darkglow {
        from { text-shadow: 0 4px 32px #fff, 0 1.5px 0 #00fff7; }
        to { text-shadow: 0 4px 64px #00fff7, 0 1.5px 0 #fff; }
    }
    .sub-header {
        font-size: 1.3rem;
        color: #00fff7;
        text-align: center;
        margin-bottom: 1.5rem;
        letter-spacing: 1px;
    }
    .creator {
        font-size: 1.1rem;
        background: linear-gradient(90deg, #00fff7 0%, #ff00cc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        opacity: 1;
        letter-spacing: 1px;
        font-weight: bold;
        text-shadow: 0 2px 12px #00fff7;
    }
    .glass-card, .login-card {
        background: rgba(255, 255, 255, 0.85);
        color: #111;
        border-radius: 18px;
        box-shadow: 0 8px 32px 0 rgba(0, 255, 247, 0.18);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1.5px solid rgba(0, 255, 247, 0.18);
        padding: 2.2rem 2rem 1.5rem 2rem;
        margin-top: 1.5rem;
        margin-bottom: 2rem;
        transition: box-shadow 0.3s;
    }
    .glass-card:hover, .login-card:hover {
        box-shadow: 0 12px 48px 0 #00fff755;
    }
    .glass-instruction {
        color: #00fff7;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1.2rem;
        text-align: left;
    }
    .footer {
        font-size: 1rem;
        color: #00fff7;
        text-align: center;
        margin-top: 2.5rem;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
    }
    .stButton > button {
        background: linear-gradient(90deg, #36d1c4 0%, #5b86e5 100%);
        color: #fff;
        border-radius: 12px;
        font-size: 1.2rem;
        padding: 0.8rem 2.5rem;
        margin-top: 1.2rem;
        margin-bottom: 1.2rem;
        border: none;
        box-shadow: 0 2px 16px #5b86e544;
        transition: background 0.2s, box-shadow 0.2s;
        font-weight: 600;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #5b86e5 0%, #36d1c4 100%);
        box-shadow: 0 4px 32px #36d1c499;
    }
    .stTextInput > div > div > input {
        background: rgba(0, 255, 247, 0.10);
        color: #111;
        border-radius: 8px;
        border: 1.5px solid #00fff799;
        font-size: 1.1rem;
    }
    hr {
        border: 0;
        height: 1.5px;
        background: linear-gradient(90deg, #00fff7 0%, #232526 100%);
        margin: 1.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'research_history' not in st.session_state:
    st.session_state.research_history = []
if 'current_report' not in st.session_state:
    st.session_state.current_report = None

# Use Streamlit secrets for your API key
client = Groq(api_key=st.secrets["CROQAI_API_KEY"])

def create_research_agent():
    """Create a research agent with web search capabilities"""
    try:
        search_tool = DuckDuckGoSearchRun()
        return search_tool
    except Exception as e:
        st.error(f"Error creating research agent: {str(e)}")
        return None

def generate_research_report(topic, search_tool):
    """Generate a comprehensive research report using Groq LLM and DuckDuckGo search"""
    system_prompt = (
        "You are an expert research assistant. Your task is to:\n"
        "1. Research the given topic thoroughly using web search\n"
        "2. Gather comprehensive information from multiple sources\n"
        "3. Analyze and synthesize the information\n"
        "4. Create a well-structured research report with the following sections:\n"
        "   - Executive Summary\n"
        "   - Key Findings\n"
        "   - Detailed Analysis\n"
        "   - Current Trends\n"
        "   - Future Outlook\n"
        "   - Sources and References\n\n"
        "Be thorough, accurate, and provide actionable insights. Use markdown formatting for better readability."
    )
    try:
        with st.spinner("🔍 Researching your topic..."):
            search_results = search_tool.run(topic)
        with st.spinner("📝 Generating comprehensive report..."):
            prompt = (
                f"{system_prompt}\n\n"
                f"Based on the research findings: {search_results}\n\n"
                f"Generate a comprehensive research report on: {topic}"
            )
            report = get_groq_response(prompt)
        return report, search_results
    except Exception as e:
        st.error(f"Error generating report: {str(e)}")
        return None, None

def save_report_to_history(topic, report):
    """Save report to session history"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_entry = {
        "topic": topic,
        "report": report,
        "timestamp": timestamp
    }
    st.session_state.research_history.append(report_entry)

def display_report(report, topic):
    """Display the research report in a formatted way"""
    #st.markdown(f"<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='glass-card'><h3>📊 Research Report: {topic}</h3>", unsafe_allow_html=True)
    st.markdown(report, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Add download button
    report_text = f"# Research Report: {topic}\n\n{report}"
    st.download_button(
        label="📥 Download Report (Markdown)",
        data=report_text,
        file_name=f"research_report_{topic.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
        mime="text/markdown"
    )

def get_groq_response(prompt, model="llama3-70b-8192"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def login():
    st.markdown('<div class="login-card"><h2>🔒 Login</h2>', unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")
    st.markdown("</div>", unsafe_allow_html=True)
    if login_btn:
        # Simple demo: username = pritham, password = aiagent
        if username == "pritham" and password == "aiagent":
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials. Try username: pritham, password: aiagent")
    return st.session_state.get("logged_in", False)

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if not st.session_state.logged_in:
        if not login():
            st.stop()

    st.markdown('<div class="main-header">🤖 AI Research Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Powered by Groq + DuckDuckGo</div>', unsafe_allow_html=True)
    st.markdown('<div class="creator">Created by Pritham Jujjavarapu</div>', unsafe_allow_html=True)

    if 'research_history' not in st.session_state:
        st.session_state.research_history = []

    # --- Research Report Search Bar ---
   # st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<div class='glass-instruction'>🧠 For detailed research reports, use this section. Enter a topic and get a comprehensive, multi-section report with web search.</div>", unsafe_allow_html=True)
    st.markdown("### 🧠 Research Assistant", unsafe_allow_html=True)
    topic = st.text_input("Enter your research topic:", key="research_input")
    if st.button("Generate Research Report", key="research_btn"):
        search_tool = create_research_agent()
        if not search_tool:
            st.markdown("</div>", unsafe_allow_html=True)
            return
        report, search_results = generate_research_report(topic, search_tool)
        if report:
            display_report(report, topic)
            save_report_to_history(topic, report)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Q&A Search Bar ---
    #st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<div class='glass-instruction'>💬 For quick answers or short questions, use this section. Ask anything and get a concise answer from the AI.</div>", unsafe_allow_html=True)
    st.markdown("### 💬 Q&A Assistant", unsafe_allow_html=True)
    user_input = st.text_input("Ask anything:", key="qa_input")
    if st.button("Ask", key="qa_btn") and user_input:
        try:
            with st.spinner("Groq is thinking..."):
                answer = get_groq_response(user_input)
            st.markdown(f"<div style='margin-top:1rem; color:#111;'><b>Groq's answer:</b><br>{answer}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error getting answer: {e}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Show research history
    if st.session_state.research_history:
        st.markdown("<h4 style='color:#00fff7;'>🕑 Research History</h4>", unsafe_allow_html=True)
        for entry in reversed(st.session_state.research_history):
            with st.expander(f"{entry['topic']} ({entry['timestamp']})"):
                st.markdown(entry['report'], unsafe_allow_html=True)

    st.markdown('<div class="footer">© 2024 Pritham Jujjavarapu. All rights reserved.</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 