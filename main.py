from typing import Union
import atexit
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from neo4j import GraphDatabase
import requests
import os

MISTRAL_API_KEY = "Bim7zMxmJSVKzmjXPUmlOq3FIkLMfXbj"

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Establish connection to Mistral 7B
class PromptRequest(BaseModel):
    prompt: str

# Send request to Mistral 7B
@app.post("/generate_text/")
async def generate_text(request: PromptRequest):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-type": "application/json",
    }
    payload = {
        "model": "mistral-tiny", 
        "messages": [{"role":"user", "content": request.prompt}],
        "temperature": 0.7,
        "max_tokens": 200,
    }
    try:
        # Connect to Mistral 7B
        response = requests.post("https://api.mistral.ai/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status() # Raise an exception for HTTP errors
        generate_text = response.json()["choice"][0]["message"]["content"]
        return {"response": generate_text}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with Mistral API: {e}")


# Establish connection to Neo4j GDB
class GraphDB:

    def __init__(self):
        # Neo4j URI, username, password
        uri = "neo4j+s://7d002c1b.databases.neo4j.io"
        user = "neo4j"
        password = "ro3_6PfNiAyAaP1F38q7hB0o23Xy8jweDEPlhoZAMu4"
        # Connect to Neo4j GDB
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        print("Neo4j GDB address:", self.driver.get_server_info().address)
    
    def close(self):
        self.driver.close()

GDB = GraphDB()
session = GDB.driver.session(database="neo4j")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/subjects")
async def read_subjects():
    # The cypher query
    def get_subjects_name(ss):
        result = ss.run("""
            MATCH (p) 
            RETURN p.name as name;
            """)
        return list[result]
    return session.execute_read(get_subjects_name)

@app.get("/relationships")
async def read_relationships():
    # The cypher query
    def get_relationships(ss):
        result = ss.run("""
            MATCH (n1)-[r]->(n2) 
            RETURN type(r);
            """)
        return list[result]
    return session.execute_read(get_relationships)

@app.get("/relationship-node")
async def read_relationship_node():
    # The cypher query
    def get_relationship_subject(ss):
        result = ss.run("""
            MATCH (n)-[r]->(m)
            RETURN n, r, m
        """)
        return list[result]
    return session.execute_read(get_relationship_subject)

@app.get("/subjects/{subject_name}")
async def read_subject(subject_name: str, q: Union[str, None] = None):
    # The cypher query
    def get_subject_by_name(ss, subject_name):
        result = ss.run("""
            MATCH (n1{name: $subject_name})-[r]->(n2) 
            RETURN n1, r, n2;
        """,
        subject_name=subject_name
        )
        return list[result]
    return session.execute_read(get_subject_by_name, subject_name), {"q":q} # Error description


