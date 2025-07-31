from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load model and tokenizer from local checkpoint
model_path = "./models/book-gpt"

tokenizer = GPT2Tokenizer.from_pretrained(model_path, local_files_only=True)
model = GPT2LMHeadModel.from_pretrained(model_path, local_files_only=True)

# Set pad token to eos token if missing (required for sampling)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
    model.resize_token_embeddings(len(tokenizer))


# Set to evaluation mode
model.eval()

# Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Inference loop
while True:
    user_input = input("\n📝 Enter a prompt (or type 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        break

    # Encode input and move to device
    input_ids = tokenizer.encode(user_input, return_tensors="pt").to(device)

    # Generate text
    output = model.generate(
        input_ids,
        max_length=100,
        num_return_sequences=1,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id,  # Avoid padding error
        early_stopping=True,
    )

    # Decode and display output
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(f"\n🤖 Generated:\n{generated_text}")
