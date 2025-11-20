Trigram Language Model

This repository contains my implementation of a simple trigram-based language model for the AI/ML intern assignment.
The model learns from text by counting word triples and then uses those statistics to generate new text.

Installation

Install all required dependencies:

pip install -r requirements.txt

Project Structure

```
trigram-assignment/
│
├── src/
│   ├── ngram_model.py     # main model implementation
│   ├── generate.py
│   └── utils.py
│
├── tests/
│   └── test_ngram.py
│
├── data/
│   └── example_corpus.txt
│
├── pytest.ini
└── evaluation.md
```


Usage Example
from src.ngram_model import TrigramModel

model = TrigramModel()
model.fit("your training text here")
print(model.generate(max_length=40))

Running Tests

Run the test suite from inside the trigram-assignment folder:

pytest


All tests should pass with the current model.
