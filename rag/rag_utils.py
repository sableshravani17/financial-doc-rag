from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import PyPDF2

model = None

dimension = 384
index = faiss.IndexFlatL2(dimension)

documents = []
doc_ids = []


def get_model():
    global model
    if model is None:
        print("Loading model...")
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


def extract_text(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text


def chunk_text(text, chunk_size=300):
    sentences = text.split(".")
    chunks = []
    current = ""

    for sentence in sentences:
        if len(current) + len(sentence) < chunk_size:
            current += sentence + "."
        else:
            chunks.append(current.strip())
            current = sentence + "."

    if current:
        chunks.append(current.strip())

    return chunks


def index_document(file_path, document_id):
    model = get_model()

    text = extract_text(file_path)
    chunks = chunk_text(text)

    vectors = []

    for chunk in chunks:
        if chunk.strip():
            emb = model.encode(chunk)
            vectors.append(emb)
            documents.append(chunk)
            doc_ids.append(document_id)

    if len(vectors) > 0:
        index.add(np.array(vectors))


def search_documents(query):
    model = get_model()

    if len(documents) == 0:
        return ["No documents indexed"]

    q_emb = model.encode([query])

   
    D, I = index.search(q_emb, k=20)
    candidates = [documents[i] for i in I[0]]

    
    scored = []
    for chunk in candidates:
        emb = model.encode(chunk)
        score = np.dot(q_emb[0], emb)
        scored.append((chunk, score))

  
    scored.sort(key=lambda x: x[1], reverse=True)

    
    return [s[0] for s in scored[:5]]



def get_context_by_doc(doc_id):
    return [d for d, i in zip(documents, doc_ids) if i == doc_id]



def remove_document_by_id(doc_id):
    global documents, doc_ids

    new_docs = []
    new_ids = []

    for d, i in zip(documents, doc_ids):
        if i != doc_id:
            new_docs.append(d)
            new_ids.append(i)

    documents[:] = new_docs
    doc_ids[:] = new_ids