
from src.embedding import generate_embeddings
from sklearn.metrics.pairwise import cosine_similarity

sentences = [
    "Tagihan listrik bulan November belum dibayar.",
    "Invoice listrik November masih memiliki tunggakan.",
    "Saya ingin membeli pakaian dengan diskon."
]

vectors = generate_embeddings(sentences)

similarity = cosine_similarity(vectors)

print("Vector shape:", vectors.shape)
print("\nSimilarity Matrix:")

for i in range(len(sentences)):
    for j in range(len(sentences)):
        print(
            f"Kalimat {i + 1} vs {j + 1}: "
            f"{similarity[i][j]:.4f}"
        )
