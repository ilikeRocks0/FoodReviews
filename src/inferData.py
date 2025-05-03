import re
import json
REVIEW_PATH = "assets\Yelp-JSON\Yelp JSON\yelp_dataset\yelp_academic_dataset_review.json"
REVIEW_TEST_PATH = "src/test_review.txt"
MAX_THRESHOLD = 25000
PRINT_THRESHOLD = 100

#clean text without tokenization
# nlp = spacy.load("en_core_web_sm")
def clean_text(text) -> list: 
    # Remove content inside brackets [] or ()
    text = re.sub(r'\[.*?\]|\(.*?\)', '', text)
    
    # Remove punctuation and numbers REGEX PATTERN RECOGNITION
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    text = text.lower()
    
    #tokenize it
    # doc = nlp(text)
    # tokens = []
    
    # # dont have stop words and lemmatize
    # for token in doc:
    #     if not token.is_stop and token.is_alpha:
    #         tokens.append(token.lemma_)

    return text
    
#very functional paradigm of me
def main():
    # Reading in reviews from the file
    reviews = read_in_reviews()

    #turning reviews into json
    reviews = json_reviews(reviews)

    #filtering out reviews to star 1 and star 2
    reviews = filter_reviews(reviews)
    
    #clean reviews
    reviews = clean_reviews(reviews)

    good, bad, freq = organize_reviews(reviews)
    print(f"good words: {good}")
    print(f"bad words: {bad}")
    print(f"word freq: {freq}")

# reads in each review from the file
def read_in_reviews():
    reviews = []
    #counts what number we are reading
    count = 0

    with open(REVIEW_TEST_PATH, encoding='utf-8') as f:
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

#cleans texts
def clean_reviews(reviews):
    new_reviews = []
    for review in reviews:
        r = clean_text(review["text"])
        new_reviews.append((r, review["stars"]))
    return new_reviews

def organize_reviews(reviews):
    wordFreq = {}
    goodReview = set()
    badReview = set()

    for review in reviews:
        new_set = harvest_words(review[0], wordFreq)
        if review[1] == 5:
            goodReview = goodReview.union(new_set)
        else:
            badReview = badReview.union(new_set)

    good = goodReview.difference(badReview)
    bad = badReview.difference(goodReview)
    return good, bad, wordFreq

def harvest_words(review:str, wordFreq):
    words = review.split()
    for word in words:
        if word not in wordFreq:
            wordFreq[word] = 0
        wordFreq[word]+=1 
    return set(words)
    
if __name__ == "__main__":
    main()

