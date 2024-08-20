# ChatGPT-like Website
Simple Chatbot with Open Source LLMs using Python and Hugging Face
Flask is used for hosting the backend service.

 - `chatbot_InLine.py`: Chatbot based  in"[facebook/blenderbot-400M-distill](https://huggingface.co/facebook/blenderbot-400M-distill)". This choice is motivated because it has an open-source license and runs relatively fast
 - `chatbot_App.py`: Integration of the previous tool within a Flask-based web application. The folders `templates` and `static` contain the CSS, java, and html parts. 
 

For alternative models, check the Hugging Face options in the website https://huggingface.co/models


GenAI_2_WebChatbot
├── chatbot_App.py                 # The main Flask application script
├── chatbot_InLine.txt             # To run in terminal
├── templates/
│   └── index.html                 # The HTML template for the chat interface
└── static/
    ├── styles.css                 # CSS file for styling the interface
    └── scripts.js                 # JavaScript for handling user interactions

