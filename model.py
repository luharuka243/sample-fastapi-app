import random
import time

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Document Topic Matcher API",
    description="API for extracting topics from text and multimedia files and determining if they match",
)


TOPICS = {
    "Technology": [
        "Artificial Intelligence",
        "Cloud Computing",
        "Cybersecurity",
        "Blockchain",
        "Internet of Things",
        "Machine Learning",
    ],
    "Healthcare": [
        "Telemedicine",
        "Medical Research",
        "Public Health",
        "Healthcare Innovation",
        "Mental Health",
        "Pharmaceuticals",
    ],
    "Finance": [
        "Investment Strategies",
        "Cryptocurrency",
        "Banking",
        "Financial Planning",
        "Stock Market",
        "Economic Policy",
    ],
    "Education": [
        "E-Learning",
        "Higher Education",
        "K-12 Education",
        "Educational Technology",
        "Teaching Methods",
        "Curriculum Development",
    ],
    "Environment": [
        "Climate Change",
        "Renewable Energy",
        "Conservation",
        "Sustainability",
        "Environmental Policy",
        "Pollution Control",
    ],
}


@app.get("/health")
def health() -> JSONResponse:
    """Check if the API is running"""
    return JSONResponse(content={"status": "ok"}, status_code=200)


@app.get("/analyze")
def get_random_topic() -> JSONResponse:
    """Get a random topic and subtopic"""
    time.sleep(1)
    topic = random.choice(list(TOPICS.keys()))  # nosec
    subtopic = random.choice(TOPICS[topic])  # nosec
    return JSONResponse(
        content={"topic": topic, "subtopic": subtopic},
        media_type="application/json",
        status_code=200,
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # nosec
