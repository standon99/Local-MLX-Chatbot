from flask import Flask, request, Response, render_template
import time
import os
from mlx_lm import load, generate, stream_generate
import time

app = Flask(__name__)

conversation = [{"role": "user", "content": "Call me Siddhant. When asked something that requires up-to-date information such as weather, news etc., you must just output the phrase 'API NEEDED- with the type of info (weather:location, news) needed following hypen'. If you don't know where I am ask first before outputting the weather command"}, {"role": "assistant", "content": "Hello Siddhant"}]
running = False

# Specify the checkpoint
#checkpoint = "gemma-2-27b-it-4bit"
checkpoint = "/Users/stan/Documents/CodingProjects/MyChatbot/Meta-Llama-3.1-8B-Instruct-8bit"
#checkpoint = "/Users/stan/Documents/CodingProjects/MyChatbot/Llama-3.2-3B-Instruct"
# Load the corresponding model and tokenizer
model, tokenizer = load(path_or_hf_repo=checkpoint)
#model, tokenizer = load("mlx-community/Llama-3.3-70B-Instruct-4bit")

def generate_text(prompt):
    global running, model, tokenizer
    if running is False:
        running = True
        global conversation
        start_time = time.time()

        # Specify the prompt
        conversation.append({"role": "user", "content": prompt}) #= [{"role": "user", "content": conversation_history_user}, {"role": "assistant", "content": conversation_history_jarvis}]

        # Transform the prompt
        prompt = tokenizer.apply_chat_template(
            conversation, tokenize=False, add_generation_prompt=True
        )

        # Specify the maximum number of tokens
        max_tokens = 2000

        # Specify if tokens and timing information will be printed
        verbose = True

        generation_step_args = {
            "temp": 0.05,
            "repetition_penalty": 1.2,
            "repetition_context_size": 20,
            "top_p": 0.95,
        }

        response = ""
        for t in stream_generate(model, tokenizer, prompt, max_tokens, **generation_step_args):
            response = response + t
            yield t
        
        #append_to_history('assistant', response)
        conversation.append({"role": "assistant", "content": response})
            
        print(conversation)
        #print(str(response))
        end_time = time.time()
        print('********************************************')
        print(f'Time taken to execute: {end_time-start_time} seconds')
        print('********************************************')
        running = False
    else:
        print("WARNING: You can only process one prompt at a time, wait till the extant request is complete before continuing")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    return Response(generate_text(prompt), mimetype='text/plain')

# Serve the HTML file
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port="15000")