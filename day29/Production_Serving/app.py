import time
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from telemetry_logger import TelemetryLogger

app = FastAPI(
    title="ML Model Production Serving API",
    description="High-performance asynchronous inference and telemetry endpoint.",
    version="1.0.0",
)

telemetry = TelemetryLogger()


class PredictionRequest(BaseModel):
    features: List[float] = Field(
        ...,
        json_schema_extra={"example": [0.54, -1.22, 0.88, 2.15]},
    )


class BatchPredictionRequest(BaseModel):
    instances: List[List[float]]


class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    latency_ms: float


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "ML Model Production Serving API",
        "documentation": "/docs",
        "health_check": "/health",
        "telemetry_metrics": "/telemetry",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "model-serving-api"}


@app.get("/telemetry")
def get_telemetry():
    return telemetry.get_metrics()


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    start_time = time.perf_counter()

    if not request.features:
        telemetry.log_inference(0.0, status_code=400)
        raise HTTPException(status_code=400, detail="Empty feature vector provided.")

    # Linear decision heuristic mapping features to probability
    score = sum(request.features)
    prob = 1.0 / (1.0 + (2.71828 ** (-score)))
    pred = 1 if prob >= 0.5 else 0

    latency_ms = (time.perf_counter() - start_time) * 1000.0
    telemetry.log_inference(latency_ms, status_code=200)

    return PredictionResponse(
        prediction=pred,
        probability=round(prob, 4),
        latency_ms=round(latency_ms, 3),
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)