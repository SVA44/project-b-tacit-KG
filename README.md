# project-b-tacit-KG 
Project B main page. <br/>
The project pipeline: Interview Transcipts/Discussions -> Sentence synthesizing/labelling -> Translate into Cypher Query -> Set up KGs in Neo4j -> Show in frontend <br/>
Current plan: Manually separate sentences using a sample data source, then translate into Cypher queries. Compare to manually extracting data using Mistral 24B, ChatGPT and DeepSeek<br/>
Mistral 7B full chat: https://chat.mistral.ai/chat/95f72a3d-8ad7-47a3-9d35-39233406e846 <br/>
Facts and Relationships Extraction using LLMs: <br/>
ChatGPT full chat: https://chatgpt.com/c/68d6135b-3688-8323-ad9f-8c6e53076dfa <br/>
Mistral 24B full chat: https://chat.mistral.ai/chat/1418cb7b-8726-4256-be41-d592ea34a1fc <br/>
DeepSeek full chat: https://chat.deepseek.com/a/chat/s/50765af3-e2b1-41c6-a74f-26358db70b4e <br/>
FastAPI App Experimental Prototype v1
<img width="1920" height="960" alt="image" src="https://github.com/user-attachments/assets/7c256728-5743-42a4-9ff0-6208e7ed452c" />
Mistral 24B response json
<img width="1920" height="956" alt="image" src="https://github.com/user-attachments/assets/f7bf3560-95b6-44a4-a868-808e14378f79" />
Note: Run Uvicorn server by executing "uvicorn test:app --reload" <br/>
Neo4j Knowledge Graph (KG) showing tacit fishing knowledge obtained from interviews and open discussions with fisherfolk in Indonesia and Bangladesh
<img width="1608" height="817" alt="image" src="https://github.com/user-attachments/assets/d87af86e-95f4-4fb3-bedd-6a99a39f9f47" />

