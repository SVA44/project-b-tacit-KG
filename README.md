# project-b-tacit-KG 
Project B main page. <br/>
The project pipeline: Interview Transcipts/Discussions -> Sentence synthesizing/labelling -> Translate into Cypher Query -> Set up KGs in Neo4j -> Show in frontend <br/>
Current plan: Manually separate sentences using a sample data source, then translate into Cypher queries. Automate the process using Mistral 7B and FastAPI <br/>
Mistral 7B full chat: https://chat.mistral.ai/chat/95f72a3d-8ad7-47a3-9d35-39233406e846 <br/>
ChatGPT full chat: https://chatgpt.com/c/68d6135b-3688-8323-ad9f-8c6e53076dfa
FastAPI App Experimental Prototype v1
<img width="1920" height="960" alt="image" src="https://github.com/user-attachments/assets/7c256728-5743-42a4-9ff0-6208e7ed452c" />
Mistral 7B response json
<img width="1919" height="960" alt="image" src="https://github.com/user-attachments/assets/f8f4138f-ecd4-49c4-a338-82ec1a241909" />
Note: Run Uvicorn server by executing "uvicorn test:app --reload" <br/>
Neo4j Knowledge Graph (KG) showing tacit fishing knowledge obtained from interviews and open discussions with fisherfolk in Indonesia and Bangladesh
<img width="1608" height="817" alt="image" src="https://github.com/user-attachments/assets/d87af86e-95f4-4fb3-bedd-6a99a39f9f47" />

