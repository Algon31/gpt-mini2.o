from transformers import GPT2Tokenizer
import json

# Load GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Load your book text
with open("./data/train_clean.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Tokenize the text
tokens = tokenizer(text, return_tensors="pt", truncation=False)

# Save the token IDs (input_ids) to file for training
input_ids = tokens["input_ids"][0].tolist()

with open("tokens.json", "w") as f:
    json.dump(input_ids, f)

print(f"Tokenized {len(input_ids)} tokens.")
