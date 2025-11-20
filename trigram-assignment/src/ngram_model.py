import random
import re
from collections import defaultdict

class TrigramModel:
    def __init__(self):
        """
        Initializes the TrigramModel.
        """
        #TODO: Initialize any data structures you need to store the n-gram counts.
        self.trigram_counts = defaultdict(lambda: defaultdict(int))
        self.bigram_counts = defaultdict(int)
        self.START = "<s>"
        self.END = "</s>"
        pass

    def fit(self, text):
        """
        Trains the trigram model on the given text.

        Args:
            text (str): The text to train the model on.
        """
        # TODO: Implement the training logic.
        # This will involve:
        # 1. Cleaning the text (e.g., converting to lowercase, removing punctuation).
        text = text.lower()

        # 2. Tokenizing the text into words.
        tokens = re.findall(r"\b\w+\b", text)

        # 3. Padding the text with start and end tokens.
        tokens = [self.START, self.START] + tokens + [self.END]


        # 4. Counting the trigrams.
        for i in range(len(tokens) - 2):
            w1, w2, w3 = tokens[i], tokens[i+1], tokens[i+2]
            self.bigram_counts[(w1, w2)] += 1
            self.trigram_counts[(w1, w2)][w3] += 1

        pass

    def _next_word(self, w1, w2):
            """
            Choose the next word based on trigram probabilities.
            """
            candidates = self.trigram_counts.get((w1, w2), None)
            if not candidates:
                return self.END

            words = list(candidates.keys())
            counts = list(candidates.values())

            total = sum(counts)
            probabilities = [c / total for c in counts]

            return random.choices(words, probabilities)[0]
    
    def generate(self, max_length=50):
        """
        Generates new text using the trained trigram model.

        Args:
            max_length (int): The maximum length of the generated text.

        Returns:
            str: The generated text.
        """

        w1, w2 = self.START, self.START
        output = []

        for _ in range(max_length):
            w3 = self._next_word(w1, w2)

            if w3 == self.END:
                break

            output.append(w3)
            w1, w2 = w2, w3

        return " ".join(output)
        # TODO: Implement the generation logic.
        # This will involve:
        # 1. Starting with the start tokens.
        # 2. Probabilistically choosing the next word based on the current context.
        # 3. Repeating until the end token is generated or the maximum length is reached.
        pass
