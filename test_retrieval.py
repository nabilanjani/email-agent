
from src.retrieval import retrieve_emails

test_intents = [
    {
        "category": "invoice",
        "status": "unpaid",
        "date_period": "this_month",
        "search_query": "tagihan yang belum dibayar bulan ini"
    },
    {
        "category": "meeting",
        "status": None,
        "date_period": "this_month",
        "search_query": "jadwal rapat atau meeting"
    },
    {
        "category": "promotion",
        "status": None,
        "date_period": "this_month",
        "search_query": "promo diskon belanja"
    }
]

for index, intent in enumerate(test_intents, start=1):
    print("\n" + "=" * 60)
    print(f"TEST CASE {index}")
    print("Query:", intent["search_query"])

    results = retrieve_emails(
        intent=intent,
        top_k=5,
        threshold=0.25
    )

    if not results:
        print("Tidak ada email yang ditemukan.")
        continue

    for result in results:
        print(
            result["email_id"],
            "|",
            result["subject"],
            "| Score:",
            result["similarity_score"]
        )
