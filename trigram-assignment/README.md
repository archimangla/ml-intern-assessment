Trigram Model — AI/ML Intern Assignment

This project implements a simple trigram language model capable of training on text and generating new text based on trigram probabilities.

Installation

Install dependencies using:

pip install -r requirements.txt

Project Structure
trigram-assignment/
│
├── src/
│   ├── ngram_model.py  
│   ├── generate.py     
│   └── utils.py
│
├── tests/
│   └── test_ngram.py    
│
├── data/
│   └── example_corpus.txt
│
├── README.md
└── evaluation.md

How to Run the Model
Train + Generate (inside Python)
from src.ngram_model import TrigramModel

model = TrigramModel()
model.fit("your training text here")

print(model.generate(max_length=50))

Running Tests

From inside the trigram-assignment folder:

pytest


Pytest configuration (pytest.ini) ensures that tests only run inside the tests/ directory.

Notes for Reviewers

The trigram model uses start/end tokens to support generation.

Probabilities are computed from raw counts using normalized trigram frequencies.

Random sampling uses weighted probabilities to select the next word.
