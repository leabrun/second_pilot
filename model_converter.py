from joblib import load


clf = load('model.joblib') 
result = clf.predict("Что делать, если я хочу изменить группу?")
print(result)
