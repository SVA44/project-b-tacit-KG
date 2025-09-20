from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Union
import atexit
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from neo4j import GraphDatabase
import requests
import os

MISTRAL_API_KEY = "Bim7zMxmJSVKzmjXPUmlOq3FIkLMfXbj"

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "My FastAPI HTML App", "name": "World"}
    )
# Establish connection to Mistral 7B
class PromptRequest(BaseModel):
    prompt: str

# Send request to Mistral 7B
@app.post("/submit-prompt")
async def generate_text(prompt: str = Form(...)):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-type": "application/json",
    }
    payload = {
        "model": "mistral-tiny", 
        "messages": [{"role":"user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 200,
    }
    try:
        # Connect to Mistral 7B
        response = requests.post("https://api.mistral.ai/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status() # Raise an exception for HTTP errors
        # generate_text = response.json()["choice"][0]["message"]["content"]
        return {"response": response}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with Mistral API: {e}")

@app.get("/greet/{name}", response_class=HTMLResponse)
async def greet_user(request: Request, name: str):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": f"Hello {name}!", "name": name}
    )