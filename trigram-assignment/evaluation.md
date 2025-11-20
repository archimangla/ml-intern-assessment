Evaluation Summary

This document gives a short overview of the approach I followed while implementing the trigram model.

Model Design

I used two dictionaries:

- one for bigram counts `(w1, w2)`
- one mapping each bigram to its possible next words with their counts

`defaultdict` helped keep the updates simple without extra condition checks.  
To handle sentence boundaries, I added `<s>` as the start token (twice) and `</s>` as the end token.

Training Steps

During training:

1. The input text is lowercased and tokenized.
2. I prepend two start tokens and append an end token.
3. I scan through the tokens in windows of three and update trigram and bigram counts.

This straightforward method ensures consistent trigram formation.

Generation Logic

Text generation begins with the two start tokens.

At each step, the model:

- finds the possible next words for the current bigram
- converts counts into sampling weights
- picks a word using `random.choices`
- shifts the window forward

Generation stops either when the end token appears or when the maximum length is reached.

Testing

The provided tests check whether training and generation behave correctly, including boundary cases.  
With the current setup (using `pytest.ini` to fix import paths), all tests pass.

Notes

The focus was on clarity and correctness.  
The implementation remains close to the standard trigram approach and fits fully within the `trigram-assignment` directory structure.
