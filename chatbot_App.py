#########################
#  chatbot_App.py      #
########################

from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Initialize Flask app
app = Flask(__name__)

# Load model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize conversation history
conversation_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user input from the form
        user_input = request.form["user_input"]

        # Update conversation history
        conversation_history_string = "\n".join(conversation_history)
        
        # Tokenize the input text and history
        inputs = tokenizer.encode_plus(conversation_history_string, user_input, return_tensors="pt")

        # Generate the response from the model
        outputs = model.generate(**inputs)

        # Decode the response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # Add interaction to conversation history
        conversation_history.append(user_input)
        conversation_history.append(response)

        # Return the response to the user in JSON format
        return jsonify({"response": response})

    return render_template("index.html")


@app.route("/reset", methods=["POST"])
def reset_conversation():
    global conversation_history
    conversation_history = []
    return jsonify({"status": "Conversation reset."})


# Run the app
if __name__ == "__main__":
    print("Start")
    app.run(debug=True)
