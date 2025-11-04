from fastapi import FastAPI
from pydantic import BaseModel
from nltk.sentiment import SentimentIntensityAnalyzer 
from loguru import logger
from sys import stderr

sia = SentimentIntensityAnalyzer()
app = FastAPI()


logger.add(stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add("logs/sentiment_api.log")

logger.debug("L'API est en cours de démarrage...")

def interpret_sentiment(compound: float):
    if compound > 0.05:
        return "Positif", "😊"
    elif compound < -0.05:
        return "Negative", "😢"
    else:
        return "Neutral", "😐"

@app.get("/")
async def homepage():
    return {"message": "Hello World"}

class AnalyseSentimentInput(BaseModel):
    text: str

@app.post("/analyse_sentiment")
async def analyse_sentiment(input: AnalyseSentimentInput):
    result = sia.polarity_scores(input.text)
    compound = result["compound"]
    label, emoji = interpret_sentiment(compound)
    return {
        "raw": {
            "neg": result["neg"],
            "neu": result["neu"],
            "pos": result["pos"],
            "compound": compound
        },
        "interpretation": {
            "label": label,
            "emoji": emoji  
        }  
    }