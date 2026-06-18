import pandas as pd
books = pd.read_csv("books.csv", on_bad_lines="skip")

query = input("Search book: ")
results = books[books["title"].str.contains(
    query,
    case=False,
    na=False,
    regex=False
)]

print(results[["title", "authors"]].head(20))
