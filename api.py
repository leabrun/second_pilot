from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils import predict_answer, get_answer_from_db


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.post("/question/")
async def get_answer(question_str: str) -> dict:
    answer_id = predict_answer(question_str=question_str)
    answer_str = get_answer_from_db(id=answer_id[0])
    return {"answer": f"{answer_str}"}
