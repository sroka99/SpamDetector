from joblib import load
clf = load('model/ml_model.joblib')

def mail_check(text:list)->str:
    if clf.predict(text)[0] == 0:
        return "ham"
    return "spam"
