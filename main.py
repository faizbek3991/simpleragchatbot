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
    "what does farm stand for": "F = FastAPI, A = Async, R = React, M = MongoDB.",
    "what is fastapi": "FastAPI is a modern Python web framework for building fast, typed APIs with automatic docs at /docs.",
    "what is react": "React is a JavaScript library for building user interfaces from reusable components.",
    "what is mongodb": "MongoDB is a NoSQL database that stores data as flexible, JSON-like documents.",
    "what is async": "Async lets the server handle other requests while waiting on slow work like database or network calls.",
    "what is an api": "An API is a set of endpoints that lets the frontend and backend talk to each other, usually over HTTP with JSON.",
    "how do i run the backend": "Install the requirements, then run: uvicorn main:app --reload (it listens on port 8000).",
    "where can i see the api docs": "Open /docs on the running backend, e.g. http://localhost:8000/docs.",
    "how do i check if the api is running": "Open /health on the backend. It returns status ok and the number of FAQs loaded.",
    "how do i ask a question": "Type it in the box below and press Enter or click Ask.",
}

FALLBACK = "I do not know yet."


@app.get("/health")
def health():
    return {"status": "ok", "faq_count": len(FAQ)}


@app.post("/ask")
def ask(item: Question):
    key = item.question.lower().strip().rstrip("?").strip()
    return {"answer": FAQ.get(key, FALLBACK), "matched": key in FAQ}
