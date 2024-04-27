from fastapi import FastAPI 


app = FastAPI()


@app.post("/question/")
async def get_answer(question_str: str) -> dict:
    # bla bla
    return {"answer": f"{question_str}"}
