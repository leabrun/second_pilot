from joblib import load
import json


def predict_answer(question_str: str) -> int:
    model = load("model.joblib") 
    arr = [question_str]

    if model.predict_proba(arr).max() < 0.1:
        proba = model.predict_proba(arr)
    
        dictionary = {}
        for value in proba:
            for index,j in enumerate(value):
    
                dictionary[j] = index
        
            sort_proba = sorted(value, reverse=True)
        
        pred_val = sort_proba[:3]
    
    
        predict = []
        for i in pred_val:
            predict.append(int(dictionary[i]))
        return predict
    
    return model.predict(arr)


def get_answer_from_db(id_list: list) -> str:
    with open("answers.json") as janswers:
        danswers = json.load(janswers)
    
    if len(id_list) > 1:
        message = "Попробуйте переформулировать вопрос. Возможно, Вы хотели задать вопрос по одной из этих тем:\n"
        for id in id_list:
            message += f"\n - {danswers[str(id)]['title']}"
        
        return message    
            
    return danswers[str(*id_list)]["text"]
