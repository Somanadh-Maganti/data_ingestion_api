import faiss , os
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

from uuid import uuid4
from langchain_core.documents import Document



def vector_store_creation(documents_with_custom_fields):

    index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))

    vector_store = FAISS(
        embedding_function=embeddings,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={},
    )

    uuids = [str(uuid4()) for _ in range(len(documents_with_custom_fields))]
    vector_store.add_documents(documents=documents_with_custom_fields, ids=uuids)

    save_directory = r"C:\Users\somanadhmaganti\Desktop\projects\Data_ingestion\development\data_ingestion_api\new_index"

    # Ensure the directory exists
    os.makedirs(save_directory, exist_ok=True)

    # Save the vector store to the specified directory
    vector_store.save_local(save_directory)
    docs = vector_store.similarity_search("qux")
    print(len(docs))



