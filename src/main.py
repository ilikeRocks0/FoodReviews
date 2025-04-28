
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
NEW_REVIEW = "I HATE HATE UNHAPPY WORST WORST"
NEW_REVIEW2 = "I am a long term frequent customer of this establishment. I just went in to order take out (3 apps) and was told they're too busy to do it. Really? The place is maybe half full at best. Does your dick reach your ass? Yes? Go fuck yourself! I'm a frequent customer AND great tipper. Glad that Kanella just opened. NEVER going back to dmitris!"
NEW_REVIEW3 = "I HATE HATE HATE HATE HATE HATE HATE HATE UNHAPPY UNHAPPY UNHAPPY UNHAPPY UNHAPPY UNHAPPY WORST WORST WORST WORST WORST WORST"
NEW_REVIEW4 = "Service was crappy, and food was mediocre.  I wish I would have picked some other place for my last dinner in town."
NEW_REVIEW5 = "I LOVE THIS PLACE"
NEW_REVIEW6 = "HAPPY GOOD NICE EPIC COOL"
NEW_REVIEW7 = "Buckingham Pizza makes the best pizza around, particularly its plain pizza and a few of its specialities -- try the cool ranch pizza. This is a pizza parlor. Don't get fancy....order the pizzas and maybe some sides. While some of the entrees are good (chicken piccata), stay with the pizza and you'll love it."
NEW_REVIEW8 = "it was okay could be better"

#when to print updates
PRINT_THRESHOLD = 100
MAX_THRESHOLD = 25000
#gets the model to read do advanced clean up of the reviews
nlp = spacy.load("en_core_web_sm")


#goes through each review and stores it clean version in reviews
def main():
    
    #hold each word that will later be turned into a vector
    reviews, stars = proccess_reviews()
    
    print("training AI...")
    aiModel = ReviewAI(reviews, stars)
    # print(stars, reviews)

    print(aiModel.predict_new_review(clean_text(NEW_REVIEW)), NEW_REVIEW)
    print(aiModel.predict_new_review(clean_text(NEW_REVIEW2)), NEW_REVIEW2)
    print(aiModel.predict_new_review(clean_text(NEW_REVIEW3)), NEW_REVIEW3)
    print(aiModel.predict_new_review(clean_text(NEW_REVIEW4)), NEW_REVIEW4)
    print(aiModel.predict_new_review(clean_text(NEW_REVIEW)), NEW_REVIEW5)
    print(aiModel.predict_new_review(clean_text(NEW_REVIEW2)), NEW_REVIEW6)
    print(aiModel.predict_new_review(clean_text(NEW_REVIEW3)), NEW_REVIEW7)
    print(aiModel.predict_new_review(clean_text(NEW_REVIEW4)), NEW_REVIEW8)


#process review based on review test path
#returns processed reviews and star data
def proccess_reviews():
    reviews = []
    stars = []
    #counts what number we are reading
    count = 0


    with open(REVIEW_PATH, encoding='utf-8') as f:
        line = f.readline()
        while (line != "" and count <= MAX_THRESHOLD):
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

