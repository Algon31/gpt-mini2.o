import json
import os
import torch
from transformers import (
    GPT2LMHeadModel,
    GPT2Tokenizer,
    Trainer,
    TrainingArguments,
    LineByLineTextDataset,
    DataCollatorForLanguageModeling
)


# Load tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token  # ✅ Fix padding token issue


# Prepare dataset
def load_dataset(file_path, tokenizer, block_size=128):
    # Load token list
    with open(file_path, "r", encoding="utf-8") as f:
        tokens = json.load(f)
    
    # Decode tokens into raw text
    text = tokenizer.decode(tokens)
    
    # Save decoded text to file for training
    os.makedirs("data", exist_ok=True)
    with open("data/train_clean.txt", "w", encoding="utf-8") as f:
        f.write(text)

    # Return dataset in required format
    return LineByLineTextDataset(
    tokenizer=tokenizer,
    file_path="data/train_clean.txt",
    block_size=block_size
)


# Load pre-trained GPT2 model
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Load tokenized dataset
dataset = load_dataset("./tokenizing/tokens.json", tokenizer)

# Prepare data collator
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Training configuration
training_args = TrainingArguments(
    output_dir="./models",               # where to save the model
    overwrite_output_dir=True,
    num_train_epochs=2,                 # how many times to go over the data
    per_device_train_batch_size=1,      # adjust based on GPU RAM
    save_steps=100,                     # save every 100 steps
    save_total_limit=1,                 # keep only the latest checkpoint
    logging_steps=10,
)

# Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=data_collator,
)

# Start training
trainer.train()

# Save final model and tokenizer
model_path = "./models/book-gpt"
trainer.save_model(model_path)
tokenizer.save_pretrained(model_path)

print("✅ Training completed and model saved to:", model_path)
