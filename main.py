from typing import Union

from fastapi import FastAPI

from neo4j import GraphDatabase

app = FastAPI()

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j+s://7d002c1b.databases.neo4j.io"
AUTH = ("neo4j", "ro3_6PfNiAyAaP1F38q7hB0o23Xy8jweDEPlhoZAMu4")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

# Establish driver, session
driver = GraphDatabase.driver(URI, auth=AUTH)
session = driver.session(database="neo4j")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/nodes")
async def read_nodes():
    records = session.run("""
    MATCH (p)
    RETURN p.name AS name
    """
    )
    print(records)
    return "success"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# session/driver usage

session.close()
driver.close()