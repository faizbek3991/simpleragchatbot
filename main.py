from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Module 0 FAQ Bot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Question(BaseModel):
    question: str


FAQ = {
    "what is farm": "FARM combines FastAPI, Async, React and MongoDB.",
    "who is the trainer": "The trainer is Muhammad Faiz.",
    "what time does class start": "The class starts at 9:00 AM.",
}

FALLBACK = "I do not know yet."


@app.get("/health")
def health():
    return {"status": "ok", "faq_count": len(FAQ)}


@app.post("/ask")
def ask(item: Question):
    key = item.question.lower().strip().rstrip("?").strip()
    return {"answer": FAQ.get(key, FALLBACK), "matched": key in FAQ}
