
import json
from src.models.schemas import validate_intent
from src.llm_client import ask_llm


SYSTEM_PROMPT = """
Kamu adalah intent parser untuk AI Email Agent.

Tugasmu adalah memahami permintaan pengguna
dan mengubahnya menjadi JSON.

Gunakan kategori berikut:
- invoice
- schedule
- meeting
- promotion
- payment
- general

Gunakan action berikut:
- search_emails
- list_emails
- read_email

Gunakan status berikut:
- unpaid
- paid
- null

Gunakan date_period berikut:
- this_month
- last_month
- this_week
- next_week
- today
- all_time
- unspecified

Aturan:
1. Pahami maksud pengguna, bukan hanya keyword.
2. Jangan mengarang informasi email.
3. Jika pengguna meminta pencarian email, gunakan search_emails.
4. Jika pengguna meminta seluruh daftar email, gunakan list_emails.
5. Jika pengguna menyebut ID email tertentu untuk dibaca,
   gunakan read_email.
6. Jika kategori tidak jelas, gunakan general.
7. Jika periode tidak disebutkan, gunakan unspecified.
8. Output harus berupa JSON valid tanpa markdown.

Gunakan struktur berikut:

{
    "action": "search_emails",
    "category": "invoice",
    "status": "unpaid",
    "date_period": "this_month",
    "search_query": "tagihan belum dibayar",
    "needs_clarification": false
}
"""


def parse_intent(user_request):

    prompt = f"""
    Pahami permintaan pengguna berikut.

    Permintaan:
    {user_request}

    Berikan hasil dalam format JSON sesuai instruksi.
    """

    response = ask_llm(
        prompt=prompt,
        system_message=SYSTEM_PROMPT
    )

    try:
        intent = json.loads(response)

    except json.JSONDecodeError:
        raise ValueError(
            "LLM tidak menghasilkan JSON yang valid."
        )

    validated_intent = validate_intent(intent)

    return validated_intent