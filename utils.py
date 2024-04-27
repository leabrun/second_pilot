from joblib import load
import json


def predict_answer(question_str: str) -> int:
    model = load("model.joblib") 

    if model.predict_proba([question_str]).max() < 0.3:
        return [-1]
    
    return model.predict([question_str])


def get_answer_from_db(id: int) -> str:
    if id == -1:
        return "Не совсем Вас понимаю. Ожидайте подключение оператора."

    with open("answers.json") as janswers:
        danswers = json.load(janswers)
            
    return danswers[str(id)]
