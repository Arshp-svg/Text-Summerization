from fastapi import FastAPI
from textSummaizer.pipeline.stage04_model_trainer import TrainingPipeline
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
import os
import uvicorn
import sys
from starlette.responses import RedirectResponse
from textSummaizer.pipeline.prediction import PredictionPipeline


app = FastAPI()

@app.get("/",tags=["authentication"])
def index():
    return RedirectResponse(url="/docs")

@app.get("/train", tags=["training"])
async def train():
    try:
      os.system("python main.py")
      return Response(content="Training completed successfully.", media_type="text/plain")
    except Exception as e:
        return Response(content=f"Training failed: {str(e)}", media_type="text/plain")

@app.get("/predict", tags=["prediction"])
def predict(text: str):
    try:
        prediction_pipeline = PredictionPipeline()
        output = prediction_pipeline.predict(text)
        return output
    except Exception as e:
       raise e
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)