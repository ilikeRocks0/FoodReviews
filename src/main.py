
import json
import regex
import spacy
import re
from reviewAI import ReviewAI

#dont use this
REVIEW_PATH = "assets\Yelp-JSON\Yelp JSON\yelp_dataset\yelp_academic_dataset_review.json"
#use this
REVIEW_TEST_PATH = "src/test_review.txt"
REVIEW_TEST_PATH2 = "src/test_review2.txt"
REVIEW_RIGGED_TEST_PATH2 = "src/test_rigged_reviews.txt"
NEW_REVIEW = "I WORST WORST PLACE!!!"
#when to print updates
PRINT_THRESHOLD = 100
#gets the model to read do advanced clean up of the reviews
nlp = spacy.load("en_core_web_sm")


#goes through each review and stores it clean version in reviews
def main():
    
    #hold each word that will later be turned into a vector
    reviews, stars = proccess_reviews()
    
    print("training AI...")
    aiModel = ReviewAI(reviews, stars)
    # print(stars, reviews)

    print(aiModel.predict_new_review(clean_text(NEW_REVIEW)))


#process review based on review test path
#returns processed reviews and star data
def proccess_reviews():
    reviews = []
    stars = []
    #counts what number we are reading
    count = 0


    with open(REVIEW_RIGGED_TEST_PATH2, encoding='utf-8') as f:
        line = f.readline()
        while (line != ""):
            count+=1
            r = json.loads(line.strip())
            words = r["text"]
            goodness = int(r["stars"])

            #storing values
            reviews.append(clean_text(words))
            if goodness >= 4: # if stars is greater than or equal to 4 then its good
                stars.append(1)
            else:
                stars.append(0)

            line = f.readline()

            if(count % PRINT_THRESHOLD == 0):
                print(f"read {count} reviews!")
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
    
    
    return " ".join(tokens)




if __name__ == "__main__":
    main()

