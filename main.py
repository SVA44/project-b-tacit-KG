from typing import Union
import atexit
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from neo4j import GraphDatabase

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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

@app.get("/nodes")
async def read_nodes():
    # The cypher query
    def get_nodes_name(ss):
        result = ss.run("""
            MATCH (p) 
            RETURN p.name as name;
            """)
        return list[result]
    return session.execute_read(get_nodes_name)
    

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
