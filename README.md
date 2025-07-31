
---

### ✅ `README.md`

```markdown
# 🧠 MiniGPT - Fine-tune GPT-2 on Your Own Book

MiniGPT is a lightweight project that allows you to fine-tune a GPT-2 model on any book (PDF format).
You can train your own mini-language model using HuggingFace Transformers to generate text in the style or domain of your chosen book. This is ideal for learning how GPT models work or building specialized chatbots and text generators.
---

## 📦 Features

- Convert a PDF book to text
- Tokenize and prepare the dataset
- Fine-tune GPT-2 using HuggingFace Transformers
- Automatically saves and loads training checkpoints
- Easily customizable

---
````

## ⚙️ Setup

1. Clone the repo:

```bash
git clone https://github.com/Algon31/Gpt-mini.git
cd Gpt-mini
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📝 How to Use

### Step 1: Add Your Book

Place your `.pdf` file inside the `book/` folder.

Example:

```
book/my_book.pdf
```

---

### Step 2: Convert PDF to Text

Run the following to extract the book text:

```bash
python pdf_txt.py
```

This saves a raw `.txt` file inside the `tokenizing/` folder.

---

### Step 3: Tokenize the Text

Tokenize the extracted text using:

```bash
python tokenizer.py
```

This creates a `tokens.json` file inside `tokenizing/`.

---

### Step 4: Train the Model

Now fine-tune GPT-2 on your tokenized book data:

```bash
python train.py
```

Checkpoints and final model will be saved in the `models/` folder.
You can train half and try the model too


---

## ❗ GitHub Push Warning

Some large model files (`.bin`, `.pt`, `.safetensors`) are **not tracked** by Git. To avoid pushing huge files:

`.gitignore` includes:

❗ remeber to ignore these below, u dont want someone to have your trained model and tokens
```
models/
*.pt
*.bin
tokenizing/tokens.json
data/train_clean.txt
```

---

### Step 5: Finally, You can now run the generate.py 
this will give you a mini gpt based on the book


## 🧑‍💻 Author

Created by [Algon31](https://github.com/Algon31)

