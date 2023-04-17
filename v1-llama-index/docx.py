import os
ROOT_DIR = os.path.abspath(os.curdir)
file_path = os.path.join(ROOT_DIR, 'luat-giao-thong-duong-bo-2008.docx')

from pathlib import Path
from llama_index import GPTSimpleVectorIndex, download_loader

DocxReader = download_loader("DocxReader")

loader = DocxReader()
documents = loader.load_data(file=file_path)

index = GPTSimpleVectorIndex.from_documents(documents)

# save to disk
index.save_to_disk('index.json')
# load from disk
index = GPTSimpleVectorIndex.load_from_disk('index.json')

# Querying the index
while True:
    prompt = input("Type prompt...\n")
    response = index.query(prompt)
    print(response)