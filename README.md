# ChatGPT-like Website
Simple Chatbot with Open Source LLMs using Python and Hugging Face
Flask is used for hosting the backend service.


Check the Hugging Face models in the website https://huggingface.co/models
Here we use "facebook/blenderbot-400M-distill" because it has an open-source license and runs relatively fast.

## Install requeriments
python3 -m pip install transformers==4.30.2 torch

## Execute
python3.9 chatbot_InLine.py # Run on terminal

python3.9 chatbot_App.py # Run on web service


running on  http://127.0.0.1:5000

