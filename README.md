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
- **Frontend**: Lynx
- **Backend**: FastAPI
- **LLM Integration**: Qwen 2.5 Coder

##  Prerequisites
Before you begin, ensure that you have the following installed:
- **npm** 
- **Python** 
- **pip** 



