from fastapi import FastAPI, UploadFile, File, Form
from extract import extract_entities_from_pdf
from crawler import extract_entities_from_url
from graph import insert_entities, query_entities
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    entities = extract_entities_from_pdf(file)
    insert_entities(entities)
    return {"status": "Entities inserted", "entities": entities}

@app.post("/crawl_url/")
async def crawl_url(url: str = Form(...)):
    entities = extract_entities_from_url(url)
    insert_entities(entities)
    return {"status": "Entities inserted", "entities": entities}

@app.get("/search/")
def search(label: str):
    results = query_entities(label)
    return {"results": results}
