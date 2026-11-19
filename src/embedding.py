
import ollama
import numpy as np

MODEL_NAME = "nomic-embed-text"


def generate_embedding(text):
    response = ollama.embed(
        model=MODEL_NAME,
        input=text
    )

    return np.array(
        response["embeddings"][0],
        dtype=np.float32
    )


def generate_embeddings(texts):
    response = ollama.embed(
        model=MODEL_NAME,
        input=texts
    )

    return np.array(
        response["embeddings"],
        dtype=np.float32
    )
