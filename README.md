# Twitterviews

This repository contains a Python module (`polarity_analyser.py`) and a Flask application (`app.py`) for sentiment analysis of twitter data. The module and application can help you analyze the sentiment behind tweets for user reviews.

## Module: `polarity_analyser.py`

### Features

- Tokenization of text into words.
- Replacement of contractions and abbreviations with their expanded forms (e.g., "won't" becomes "will not").
- Identification of antonyms using WordNet.
- Calculation of text polarity using predefined sentiment analysis rules.
- Regular expression-based term search in files.
- List creation and manipulation functions.

### Usage

To use the `polarity_analyser` module for sentiment analysis, you can import it into your Python script. Here's an example of how to perform sentiment analysis:

```python
import polarity_analyser

# Sample tweet for sentiment analysis
text = "I love Samsung Galaxy S23 Ultra 5G! It's amazing."

# Calculate polarity
polarity = polarity_analyser.polarity_finder(polarity_analyser.replacement_patterns(polarity_analyser.tokenize_words(text)))


