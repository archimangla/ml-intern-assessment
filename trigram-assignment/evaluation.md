This document summarizes the design choices made while implementing the trigram language model for the AI/ML intern assignment.

1. Model Design
Data Structures

defaultdict(lambda: defaultdict(int)) for trigram counts

Keys: (w1, w2) bigram context

Values: mapping of possible w3 → count

defaultdict(int) for bigram counts

Used for probability normalization

These structures were chosen to keep indexing simple, avoid key errors, and ensure constant-time insertions.

Padding Tokens

Two special tokens were added:

<s> for start

</s> for end

Padding with two start tokens (<s> <s>) allows the model to generate proper beginnings.

2. Training Logic

Training consists of:

Lowercasing and tokenizing text using a regex (\b\w+\b)

Padding tokens with <s> <s> at the start and </s> at the end

Counting trigrams of the form (w1, w2 → w3)

This ensures consistent sequence boundaries and predictable trigram formation.

3. Generation Logic

Text generation is iterative:

Start from context (<s>, <s>)

Look up possible next words for the current context

Sample the next token using random.choices() with probability weights

Slide window: (w1, w2) → (w2, w3)

Stop at </s> or when max_length is reached

Weighted sampling ensures realistic, probability-driven generation.

4. Testing and Validation

All tests are executed using:

pytest


Pytest configuration is handled through pytest.ini, ensuring:

only tests/ is scanned

src/ is added to the Python path

The model passes all provided tests.

5. Notes for Evaluators

Implementation sticks to classical trigram modeling principles.

No external NLP libraries were used; everything is implemented from scratch.

The code is modular and uses a helper function (_next_word) for clarity.

Behavior matches the expectations defined in test_ngram.py.
