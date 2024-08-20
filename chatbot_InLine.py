################
#  chatbot.py  #
################

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# model ::  Instance of the class AutoModelForSeq2SeqLM, which allows you to interact with your chosen language model.
# tokenizer :: Instance of the class AutoTokenizer, which optimizes your input and passes it to the language model efficiently.
#              It does so by converting your text input to “tokens”, which is how the model interprets the text.

conversation_history = []

history_string = "\n".join(conversation_history)

input_text ="hello, how are you doing?"
#print("\n input_text")
#print(input_text)
inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
#print("\n inputs encoded")
#print(inputs)

tokenizer.pretrained_vocab_files_map

# Generate answer
outputs = model.generate(**inputs)
#print("\n outputs")
#print(outputs)

# Decode answer
response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
#print("\n output decoded")
#print(response)

# Update conversation history
conversation_history.append(input_text)
conversation_history.append(response)
#print("\n conversation_history")
print(conversation_history)

# do it on a loop
while True:
    # Create conversation history string
    history_string = "\n".join(conversation_history)
    # Get the input data from the user
    input_text = input("> ")
    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
    # Generate the response from the model
    outputs = model.generate(**inputs)
    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    print(response)
    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)