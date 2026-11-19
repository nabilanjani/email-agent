
import ollama # Import library untuk komunikasi dgn Ollama


MODEL_NAME = "qwen3:0.6b" # Nama model Ollama


def ask_llm(prompt, system_message=None):
    """
    Mengirim prompt dari Python ke model Ollama.
    """

    messages = [] # Percakapan untuk LLM

    if system_message:
        messages.append({
            "role": "system",
            "content": system_message
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    # Mengirim permintaan ke model lokal
    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages,
        options={
            "temperature": 0
        }
    )

    # Mengambil jawaban model
    return response.message.content
