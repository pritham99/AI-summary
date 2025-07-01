#!/usr/bin/env python3
"""
Deployment Helper Script for AI Research Assistant
This script provides step-by-step instructions for deploying the app.
"""

import os
import sys
import subprocess
from pathlib import Path

def print_step(step_num, title, description):
    """Print a formatted step"""
    print(f"\n{'='*60}")
    print(f"STEP {step_num}: {title}")
    print(f"{'='*60}")
    print(description)
    print()

def check_prerequisites():
    """Check if prerequisites are met"""
    print_step(1, "Checking Prerequisites", "Verifying that all required tools are installed...")
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8+ is required")
        print(f"   Current version: {python_version.major}.{python_version.minor}.{python_version.micro}")
        return False
    else:
        print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro} is installed")
    
    # Check if requirements.txt exists
    if not Path("requirements.txt").exists():
        print("❌ requirements.txt not found")
        return False
    else:
        print("✅ requirements.txt found")
    
    # Check if app.py exists
    if not Path("app.py").exists():
        print("❌ app.py not found")
        return False
    else:
        print("✅ app.py found")
    
    return True

def install_dependencies():
    """Install Python dependencies"""
    print_step(2, "Installing Dependencies", "Installing required Python packages...")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True, text=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_api_key():
    """Check if OpenAI API key is configured"""
    print_step(3, "Checking API Key", "Verifying OpenAI API key configuration...")
    
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("✅ OpenAI API key found in environment variables")
        return True
    else:
        print("⚠️  OpenAI API key not found in environment variables")
        print("\nTo set up your API key:")
        print("1. Get a free API key from https://platform.openai.com/")
        print("2. Set it as an environment variable:")
        print("   Windows: set OPENAI_API_KEY=your_key_here")
        print("   macOS/Linux: export OPENAI_API_KEY=your_key_here")
        print("3. Or create a .env file with: OPENAI_API_KEY=your_key_here")
        return False

def test_local_run():
    """Test if the app runs locally"""
    print_step(4, "Testing Local Run", "Testing if the app can run locally...")
    
    print("Starting Streamlit app...")
    print("Press Ctrl+C to stop the test")
    
    try:
        # Start streamlit in a subprocess
        process = subprocess.Popen([sys.executable, "-m", "streamlit", "run", "app.py", "--server.headless", "true"])
        
        # Wait a few seconds to see if it starts successfully
        import time
        time.sleep(5)
        
        # Check if process is still running
        if process.poll() is None:
            print("✅ App started successfully")
            process.terminate()
            return True
        else:
            print("❌ App failed to start")
            return False
            
    except Exception as e:
        print(f"❌ Error testing app: {e}")
        return False

def deployment_instructions():
    """Provide deployment instructions"""
    print_step(5, "Deployment Instructions", "Follow these steps to deploy your app:")
    
    print("🌐 DEPLOYMENT TO STREAMLIT CLOUD")
    print("=" * 40)
    
    print("\n1. Create a GitHub repository:")
    print("   - Go to https://github.com/new")
    print("   - Create a new repository")
    print("   - Don't initialize with README (we already have one)")
    
    print("\n2. Push your code to GitHub:")
    print("   git init")
    print("   git add .")
    print("   git commit -m 'Initial commit'")
    print("   git branch -M main")
    print("   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git")
    print("   git push -u origin main")
    
    print("\n3. Deploy on Streamlit Cloud:")
    print("   - Go to https://streamlit.io/cloud")
    print("   - Sign in with your GitHub account")
    print("   - Click 'New app'")
    print("   - Select your repository and branch")
    print("   - Set main file path to: app.py")
    print("   - Click 'Deploy'")
    
    print("\n4. Configure secrets:")
    print("   - In your deployed app, go to Settings → Secrets")
    print("   - Add your OpenAI API key:")
    print("     [secrets]")
    print("     OPENAI_API_KEY = 'your_api_key_here'")
    
    print("\n5. Your app will be available at:")
    print("   https://YOUR_APP_NAME-YOUR_USERNAME.streamlit.app")

def main():
    """Main deployment helper function"""
    print("🚀 AI Research Assistant - Deployment Helper")
    print("=" * 50)
    
    # Check prerequisites
    if not check_prerequisites():
        print("\n❌ Prerequisites not met. Please fix the issues above and try again.")
        return
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Failed to install dependencies. Please check your internet connection and try again.")
        return
    
    # Check API key
    api_key_configured = check_api_key()
    
    # Test local run (only if API key is configured)
    if api_key_configured:
        test_success = test_local_run()
        if not test_success:
            print("\n⚠️  Local test failed. Please check the app configuration.")
    
    # Provide deployment instructions
    deployment_instructions()
    
    print("\n🎉 Deployment helper completed!")
    print("\nNext steps:")
    if not api_key_configured:
        print("1. Set up your OpenAI API key")
    print("2. Follow the deployment instructions above")
    print("3. Share your deployed app link with others!")

if __name__ == "__main__":
    main() 