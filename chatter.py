from mlx_lm import load, generate

#model, tokenizer = load("/Volumes/ST_USB/Meta-Llama-3.1-8B-Instruct-8bit")
#model, tokenizer = load("/Volumes/ST_USB/Meta-Llama-3.1-8B-Instruct-4bit")
model, tokenizer = load("/Volumes/ST_USB/Mistral-7B-v0.2-4bit")
#model, tokenizer = load("/Users/stan/Documents/Coding Projects/My Chatbot/Meta-Llama-3.1-8B-Instruct-4bit")
response = generate(model, tokenizer, prompt="Write me an essay about the meaning of life. The essay should be a minimum of 100 words long", verbose=False, max_tokens=50000)
print(response)





# import transformers
# import torch

# model_id = "/Users/stan/Documents/Coding Projects/My Chatbot/Meta-Llama-3.1-8B-Instruct"

# pipeline = transformers.pipeline(
#     "text-generation",
#     model=model_id,
#     model_kwargs={"torch_dtype": torch.bfloat16},
#     device_map="auto",
# )

# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]

# outputs = pipeline(
#     messages,
#     max_new_tokens=256,
# )
# print(outputs[0]["generated_text"][-1])