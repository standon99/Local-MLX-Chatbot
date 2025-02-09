# Local MLX Chatbot

https://github.com/user-attachments/assets/1c0887e0-4c24-494a-b274-32ad125794c6

## What is this project?
This project is a locally hosted chatbot using the Meta LLAMA 3.X model, and designed as a utility and as an educational experience, to learn more about how to interface with LLMs, as well as utilise Apple's new MLX framework. 

The UI features a minimalist Matrix-eque text entry and response interface (inspired by the *Hello Neo* scene from the first movie.

## How do I run it?
**This app only works on Apple Silicon. I have tested this on an M2 Macbook Pro with 16GB unified memory.**

Models can be found on HuggingFace [here] (https://huggingface.co/meta-llama). I had success with the Meta LLAMA 2.1 8 billion param model, quantised down to 4-bit. Depending on hardware lower or higher quantisation may work for you (or even more params). You will need to set the checkpoint parameter in the backend.py file to correspond to the localtion you downloaded the model on your machine.

The conversation param can also be modified so the LLM has context of your name, or any other information you feel it needs from the get-go.

You may want to set up a virtual environment for running the backend.py Python file. A requirements.txt is included for the required packages. I had success using Python 3.10.12.

The backend.py file spawns the flask app used to process inputs on the local webpage (Templates > index.html). Running this script and then visiting 127.0.0.1:15000 will take you to the interface where you can talk to the chatbot 🤖.

I set an automation task to run the Python file on startup for my computer, and created a shortcut in my dock with the icon file provided, so the chatbot was always ready to go!




