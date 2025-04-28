from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def review_reviewer(reviews: list[list[str]], stars:list[int]):

    #takes all unique words and sticks them into an vector
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(reviews)


    X_train, X_test, y_train, y_test = train_test_split(X, stars, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)

    print(accuracy_score(y_test, y_pred))
