
import json
import regex
import spacy
import re


REVIEW_PATH = "Yelp-JSON\Yelp JSON\yelp_dataset\yelp_academic_dataset_review.json"
REVIEW_TEST_PATH = "test_review.txt"
reviews = []

nlp = spacy.load("en_core_web_sm")


def main():
    with open(REVIEW_TEST_PATH, encoding='utf-8') as f:
        line = f.readline()
        while (line != ""):
            r = json.loads(line.strip())
            words = r["text"]
            reviews.append(words)
            line = f.readline()

    print(reviews)
    
def clean_text(text):
    # Remove content inside brackets [] or ()
    text = re.sub(r'\[.*?\]|\(.*?\)', '', text)
    
    # Remove punctuation and numbers REGEX PATTERN RECOGNITION
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    text = text.lower()
    
    #tokenize it
    doc = nlp(text)
    tokens = []
    
    for token in doc:
        if not token.is_stop and token.is_alpha:
            tokens.append(token.lemma_)
    
    
    return " ".join(tokens)

# main()
print(clean_text("I [definitely] loved this place!!! (amazing food, 10/10)"))
# doc = nlp("I love eating Apples, my phone is Apple")
# for token in doc:
#     print(token.text, token.pos_, token.dep_, token.is_alpha)