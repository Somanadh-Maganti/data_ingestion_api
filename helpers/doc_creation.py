import tempfile
from langchain.document_loaders import PDFPlumberLoader

async def doc_creation(pdf_file):
    # Read the content of the uploaded file (await the async method)
    pdf_content = await pdf_file.read()

    # Create a temporary file to store the PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        tmp_pdf.write(pdf_content)
        tmp_pdf_path = tmp_pdf.name

    # Load the PDF document
    loader = PDFPlumberLoader(tmp_pdf_path)
    documents = loader.load()
    
    return documents
