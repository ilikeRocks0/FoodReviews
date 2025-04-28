
import json
import regex
import spacy
import re

#dont use this
REVIEW_PATH = "Yelp-JSON\Yelp JSON\yelp_dataset\yelp_academic_dataset_review.json"
#use this
REVIEW_TEST_PATH = "src/test_review.txt"


#gets the model to read do advanced clean up of the reviews
nlp = spacy.load("en_core_web_sm")


#goes through each review and stores it clean version in reviews
def main():
    #hold each word that will later be turned into a vector
    reviews, stars = proccess_reviews()
    print(stars, reviews)
    


#process review based on review test path
#returns processed reviews and star data
def proccess_reviews():
    reviews = []
    stars = []
    with open(REVIEW_TEST_PATH, encoding='utf-8') as f:
        line = f.readline()
        while (line != ""):
            r = json.loads(line.strip())
            words = r["text"]
            goodness = int(r["stars"])
            reviews.append(words)
            stars.append(goodness)
            line = f.readline()
    return reviews, stars


def clean_text(text) -> list: 
    # Remove content inside brackets [] or ()
    text = re.sub(r'\[.*?\]|\(.*?\)', '', text)
    
    # Remove punctuation and numbers REGEX PATTERN RECOGNITION
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    text = text.lower()
    
    #tokenize it
    doc = nlp(text)
    tokens = []
    
    # dont have stop words and lemmatize
    for token in doc:
        if not token.is_stop and token.is_alpha:
            tokens.append(token.lemma_)
    
    
    return tokens




if __name__ == "__main__":
    main()

