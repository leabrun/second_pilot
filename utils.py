from joblib import load


def predict_answer(question_str: str) -> int:
    loaded_vectorizer = load('tfid_vector_model.joblib')

    params = loaded_vectorizer.transform([question_str])

    clf = load("model.joblib")
    result = clf.predict(params)

    return result


def get_answer_from_db(id: int) -> str:
    pass
