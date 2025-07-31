from transformers import GPT2Tokenizer
import os

# Create directory if it doesn't exist
os.makedirs("models/checkpoint-1110", exist_ok=True)

# Download and save tokenizer files into the checkpoint directory
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.save_pretrained("models/checkpoint-1100")
