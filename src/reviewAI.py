from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

TEST_SIZE = 1

class ReviewAI:
    vectorizer:CountVectorizer = None
    model:LogisticRegression = None

    #sets up and trains the model
    def __init__(self, reviews: list[list[str]], stars:list[int]):

        #takes all unique words and sticks them into an vector
        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(reviews)


        X_train, X_test, y_train, y_test = train_test_split(X, stars, test_size=TEST_SIZE)

        self.model = LogisticRegression()
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        print("Accurcy of model based on tests",accuracy_score(y_test, y_pred))

        

    #predicts new reivews
    def predict_new_review(self, review:str):
        if self.model == None or self.vectorizer == None:
            print("ERROR: Model not trained object creation did not work")
            return -1
        
        #need to put single item in a list
        r_list = [review]

        new_vector = self.vectorizer.transform(r_list)
        return self.model.predict(new_vector)