from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/random")
def getNumber():
    return {"number": random.randint(0, 100)}


dossier_static = Path(__file__).parent / "static"
app.mount("/", StaticFiles(directory=dossier_static, html=True), name="static")
