from fastapi import FastAPI, UploadFile, File ,Request, Body,Form
from typing import List
import json
import tempfile

from helpers.custom_fields import add_custom_fields
from helpers.vector_store import vector_store_creation
from helpers.doc_creation import doc_creation


app = FastAPI()

@app.post("/process_pdfs/")
async def process_pdf(pdf_file: UploadFile = File(...), metadata: str = Form(...)):    

   
    documents = await doc_creation(pdf_file)
    

    custom_fields =  json.loads(metadata)
    documents_with_custom_fields = add_custom_fields(documents, custom_fields)

    vector_store_creation(documents_with_custom_fields)    

    return "ok"