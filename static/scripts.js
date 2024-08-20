// static/scripts.js
const form = document.getElementById('chat-form');
const chatbox = document.getElementById('chatbox');

form.onsubmit = async (e) => {
    e.preventDefault();

    const userInput = document.getElementById('user_input').value;

    // Append user message to chatbox
    const userMessage = document.createElement('p');
    userMessage.className = 'user';
    userMessage.textContent = userInput;
    chatbox.appendChild(userMessage);

    // Scroll to the bottom of the chatbox
    chatbox.scrollTop = chatbox.scrollHeight;

    const response = await fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(new FormData(form))
    });

    const data = await response.json();

    // Append bot response to chatbox
    const botMessage = document.createElement('p');
    botMessage.className = 'bot';
    botMessage.textContent = data.response;
    chatbox.appendChild(botMessage);

    // Scroll to the bottom of the chatbox
    chatbox.scrollTop = chatbox.scrollHeight;

    // Clear input field
    form.reset();
};
