# TikTokTechJam2025

# CAPΔ

## Overview
**CAPΔ** is an AI-powered chatbot that helps developers detect and fix privacy issues in their code. By scanning user-submitted code, **CAPΔ**
identifies all sensitive data present within the code, such as API keys and emails. **CAPΔ** then presents the user with potential privacy fixes,
improving the security and compliance of the code

After reviewing the changes given by **CAPΔ**, users are able to provide additional instructions for which fixes they want implemented, or give
additional suggestions and feedback. 

## Features
- **PII & Sensitive Data Detection**: Identifies API keys, access tokens, emails, credit card numbers, and other personally identifiable information.
- **Automatic Privacy Fixes**: Redacts or masks sensitive information to prevent leaks into repositories or cloud services.
- **Interactive Chatbot**: Users can suggest improvements, and the chatbot will dynamically adjust its output to better fit the user's needs

## Architecture
The application follows a modern web architecture with:
- **Frontend**: Lynx, Typescript
- **Backend**: FastAPI
- **LLM Integration**: Qwen 2.5 Coder

##  Prerequisites
Before you begin, ensure that you have the following installed:
- **npm** 
- **Python** 
- **pip** 
- **typescript**
- **Lynx**

## Installation
1. Clone the repository
```sh
git clone https://github.com/IanCheah/TikTokTechJam2025.git
```

2. Navigate to the project directory:
```sh
cd CAP
```

## Setting up the Front end
1. From the root project directory, navigate to the frontend directory:
```sh
cd frontend
```

2. Install dependencies
```sh
cd npm install
```

3. Run the development server
```sh
cd npm run dev
```

4. Access the front end at ___

## Setting up the backend
1. Navigate to the backend directory:
```sh
cd backend
```

2. Create a Python virtual environment:
```sh
python -m venv venv
```

3. Activate the virtual environment:
```sh
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

4. Install dependencies:
```sh
pip install -r requirements.txt
```

5. Run the backend server:
```sh
uvicorn backend.main:app --reload
```

## Project Structure
```sh
TIKTOKTECHJAM/
├── .vscode/                 # VSCode settings
│   └── settings.json        # Editor configuration
├── backend/                 # FastAPI backend
│   ├── __init__.py          # Package initializer
│   ├── chat.py              # Chatbot conversation handling
│   ├── llm.py               # Qwen Coder model integration
│   ├── main.py              # FastAPI application entry point
│   ├── memory.py            # Session and conversation memory
│   ├── prompt.py            # Prompt templates and formatting
│   ├── service.py           # Core chatbot services
│   ├── utils.py             # Utility/helper functions
│   └── views.py             # API routes and endpoints
├── frontend/                # Lynx frontend
│   ├── src/                 # Frontend source code
│   ├── .gitignore           # Ignore rules for frontend
│   ├── biome.json           # Linter/formatter config
│   ├── lynx.config.ts       # Lynx configuration
│   ├── package.json         # Node.js dependencies
│   ├── package-lock.json    # Node.js lock file
│   ├── pnpm-lock.yaml       # pnpm lock file
│   ├── README.md            # Frontend documentation
│   ├── tsconfig.json        # TypeScript configuration
│   ├── vitest.config.ts     # Testing configuration
│   └── node_modules/        # Installed dependencies
├── venv/                    # Python virtual environment
├── .gitignore               # Git ignore rules
├── package.json             # Root Node.js dependencies
├── package-lock.json        # Root Node.js lock file
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Using CAPΔ
CAPΔ is an AI powered chatbot that fixes privacy issues. To interact with it:

1. Select whether you want to input code or a suggestion
2. Type in your input
3. Watch the magic happen!

Try out CAPΔ, and make your code safer today!