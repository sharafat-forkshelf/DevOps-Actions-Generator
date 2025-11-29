# DevOps Actions Generator 🚀

**DevOps Actions Generator** is a powerful, AI-driven tool designed to streamline the creation of GitHub Actions workflows. Built with [Streamlit](https://streamlit.io/) and powered by Google's [Gemini API](https://deepmind.google/technologies/gemini/), this application scans your local project directory, intelligently identifies the technology stack, and generates tailored CI/CD workflows to automate your development pipeline.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/467ad5cf-35c3-481b-ac75-f2b4132b9e0f" />

## ✨ Features

-   **📂 Smart Directory Scanning**: Automatically scans your project's file structure to understand its context.
-   **🧠 AI-Powered Stack Identification**: Uses Gemini to analyze your codebase and detect the programming language, framework, and key tools (e.g., Python, Node.js, Docker).
-   **⚡ Instant Workflow Generation**: Generates ready-to-use GitHub Actions YAML files for various scenarios:
    -   **CI (Continuous Integration)**: Run tests and builds on every push.
    -   **Linting**: Enforce code quality and style guides.
    -   **Security Audit**: Check for vulnerabilities in dependencies.
    -   **Docker Build & Push**: Automate container image creation and registry pushing.
    -   **Release**: Automate versioning and release management.
-   **🖥️ User-Friendly Interface**: A clean and intuitive GUI for easy navigation and configuration.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

-   **Python 3.8+**
-   A **Google Gemini API Key** (Get one [here](https://aistudio.google.com/app/apikey))

## 🚀 Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/devops-actions-gen.git
    cd devops-actions-gen
    ```

2.  **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables**
    Create a `.env` file in the root directory and add your Gemini API key:
    ```env
    GEMINI_API_KEY=your_actual_api_key_here
    ```

## 📖 Usage

1.  **Start the Application**
    Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2.  **Navigate the UI**
    -   **Configuration**: Check the sidebar to confirm your API key is loaded.
    -   **Select Directory**: Use the directory picker to navigate to the root of the project you want to generate actions for.
    -   **Scan Project**: Click the "Scan Project" button. The AI will analyze your files.
    -   **Generate Workflows**: Once the stack is identified, select a workflow type (e.g., "CI", "Docker") and click "Generate YAML".
    -   **Download**: Review the generated YAML code and click "Download YAML" to save it to your machine.

## 📂 Project Structure

```
devops-actions-gen/
├── app.py              # Main Streamlit application entry point
├── logic.py            # Core logic for Gemini API interaction
├── utils.py            # Utility functions for file system scanning
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (API Key)
└── README.md           # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.
