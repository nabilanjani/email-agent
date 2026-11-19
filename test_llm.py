
from src.llm_client import ask_llm


response = ask_llm(
    prompt="Jelaskan apa itu email invoice dalam satu kalimat.",
    system_message="Kamu adalah asisten AI yang menjawab dengan singkat."
)

print("Jawaban LLM:")
print(response)
