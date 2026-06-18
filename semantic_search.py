import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading books...")
books = pd.read_csv("books.csv", on_bad_lines="skip")
print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
titles = books["title"].fillna("").tolist()
print("Generating embeddings...")
book_embeddings = model.encode(titles)

query = input("Search: ")
query_embedding = model.encode([query])

scores = cosine_similarity(query_embedding,book_embeddings)[0]

top_indices = scores.argsort()[-10:][::-1]

print("\nTop Matches:\n")
for idx in top_indices:
    print(books.iloc[idx]["title"],"-",books.iloc[idx]["authors"])



'''Current Pipeline
Title
↓
Embedding
↓s
Search
'''

'''Future Pipeline
Title+Description+Subjects+Keywords
↓
Embedding
↓
Search
'''