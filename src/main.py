
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
    word_bucket = []
    reviews = proccess_reviews()
    print(reviews)
    for review in reviews:
        #concatenates lists together
        word_bucket += clean_text(review)
    
    #so we can see the words
    print(word_bucket)


#process review based on review test path
def proccess_reviews():
    reviews = []
    with open(REVIEW_TEST_PATH, encoding='utf-8') as f:
        line = f.readline()
        while (line != ""):
            r = json.loads(line.strip())
            words = r["text"]
            reviews.append(words)
            line = f.readline()
    return reviews


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

