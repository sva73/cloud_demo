from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.k8s import create_worker_pod
from app.jobs import create_worker_job

app = FastAPI()

# CORS für Vue Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "FastAPI Backend läuft"
    }

@app.get("/api/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/api/data")
def data():
    return {
        "items": [
            "Kubernetes",
            "FastAPI",
            "Vue",
            "Docker"
        ]
    }

@app.post("/api/start-worker")
def start_worker():

    pod_name = create_worker_pod()

    return {
        "status": "worker started",
        "pod": pod_name
    }

@app.post("/api/start-job")
def start_job():

    job_name = create_worker_job()

    return {
        "status": "job started",
        "job": job_name
    }