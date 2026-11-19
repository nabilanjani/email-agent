
from datetime import datetime

from sklearn.metrics.pairwise import cosine_similarity

from src.tools.mock_email_tools import load_emails
from src.embedding import generate_embedding, generate_embeddings
from src.date_parser import get_date_range


CATEGORY_KEYWORDS = {
    "invoice": [
        "invoice", "tagihan", "billing", "pembayaran",
        "listrik", "internet", "air", "gas"
    ],
    "schedule": [
        "jadwal", "kunjungan", "vendor", "appointment"
    ],
    "meeting": [
        "meeting", "rapat", "pertemuan"
    ],
    "promotion": [
        "promo", "diskon", "belanja", "penawaran"
    ],
    "payment": [
        "pembayaran", "paid", "lunas", "transfer"
    ],
    "general": []
}


def matches_category(email, category):
    if not category or category == "general":
        return True

    keywords = CATEGORY_KEYWORDS.get(category, [])
    content = (
        email.get("subject", "") + " " +
        email.get("body", "")
    ).lower()

    return any(keyword in content for keyword in keywords)



def matches_status(email, status):
    if not status:
        return True

    content = (
        email.get("subject", "") + " " +
        email.get("body", "")
    ).lower()

    unpaid_keywords = [
        "belum dibayar",
        "belum dibayarkan",
        "belum lunas",
        "belum diterima",
        "unpaid"
    ]

    paid_keywords = [
        "sudah dibayar",
        "telah dibayar",
        "sudah lunas",
        "telah lunas",
        "paid"
    ]

    is_unpaid = any(
        keyword in content for keyword in unpaid_keywords
    )

    is_paid = (
        not is_unpaid
        and any(keyword in content for keyword in paid_keywords)
    )

    if status == "unpaid":
        return is_unpaid

    if status == "paid":
        return is_paid

    return True


def retrieve_emails(intent, top_k=5, threshold=0.25):
    emails = load_emails()

    # 1. Filter berdasarkan periode tanggal.
    start_date, end_date = get_date_range(
        intent.get("date_period", "unspecified")
    )

    candidates = []

    for email in emails:
        received_date = datetime.fromisoformat(
            email["received_at"]
        ).date()

        if start_date and received_date < datetime.fromisoformat(start_date).date():
            continue

        if end_date and received_date > datetime.fromisoformat(end_date).date():
            continue

        # 2. Filter kategori.
        if not matches_category(
            email,
            intent.get("category")
        ):
            continue

        # 3. Filter status.
        if not matches_status(
            email,
            intent.get("status")
        ):
            continue

        candidates.append(email)

    if not candidates:
        return []

    # 4. Siapkan teks email untuk embedding.
    email_texts = [
        f"{email.get('subject', '')}. {email.get('body', '')}"
        for email in candidates
    ]

    query = intent.get("search_query", "").strip()

    if not query:
        query = intent.get("category", "email")

    # 5. Hitung semantic similarity.
    query_vector = generate_embedding(query)
    email_vectors = generate_embeddings(email_texts)

    scores = cosine_similarity(
        query_vector.reshape(1, -1),
        email_vectors
    )[0]

    # 6. Urutkan dari similarity tertinggi.
    results = []

    for email, score in zip(candidates, scores):
        if score >= threshold:
            results.append({
                "email_id": email["email_id"],
                "sender": email["sender"],
                "subject": email["subject"],
                "received_at": email["received_at"],
                "similarity_score": round(float(score), 4)
            })

    results.sort(
        key=lambda item: item["similarity_score"],
        reverse=True
    )

    return results[:top_k]
