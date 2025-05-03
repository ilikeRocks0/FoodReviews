import time
import json
import spacy
import re
REVIEW_PATH = "assets\Yelp-JSON\Yelp JSON\yelp_dataset\yelp_academic_dataset_review.json"
MAX_THRESHOLD = 25000
PRINT_THRESHOLD = 100

# from other file
nlp = spacy.load("en_core_web_sm")
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
    
    
    return " ".join(tokens)

#very functional paradigm of me
def main():
    # Reading in reviews from the file
    start = time.time()
    reviews = read_in_reviews()
    end = time.time()
    print(f"Reading Execution time: {end - start:.6f} seconds")

    #turning reviews into json
    start = time.time()
    reviews = json_reviews(reviews)
    end = time.time()
    print(f"Jsoning Execution time: {end - start:.6f} seconds")

    #filtering out reviews to star 1 and star 2
    start = time.time()
    reviews = filter_reviews(reviews)
    end = time.time()
    print(f"Filtering Execution time: {end - start:.6f} seconds")

    # cleaning out reviews to ai understandable text
    start = time.time()
    reviews = clean_reviews(reviews)
    end = time.time()
    print(f"Cleaning Execution time: {end - start:.6f} seconds")


# reads in each review from the file
def read_in_reviews():
    reviews = []
    #counts what number we are reading
    count = 0

    with open(REVIEW_PATH, encoding='utf-8') as f:
        line = f.readline()
        while (line != "" and count <= MAX_THRESHOLD):
            reviews.append(line)
            count+=1
            line = f.readline()
    return reviews

# jsons each review
def json_reviews(reviews):
    new_reviews = []
    for review in reviews:
        r = json.loads(review.strip())
        new_reviews.append(r)
    return new_reviews

#filters out to only 1 star and 5 star
def filter_reviews(reviews):
    new_reviews = []
    for review in reviews:
        star = int(review["stars"])
        if star == 1 or star == 5:
            new_reviews.append(review)
    return new_reviews

# cleans each review
def clean_reviews(reviews):
    new_reviews = []
    for review in reviews:
        r = clean_text(review["text"])
        new_reviews.append(r)
    return new_reviews

if __name__ == "__main__":
    main()

