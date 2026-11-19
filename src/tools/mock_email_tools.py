
import json
from pathlib import Path
from datetime import datetime


# Lokasi database mock email
DATA_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "mock_emails.json"
)


def load_emails():
    """
    Membaca seluruh data email dari file JSON.
    """

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        emails = json.load(file)

    return emails


def list_emails(page=1, page_size=5):
    """
    Menampilkan daftar email menggunakan pagination.

    page       : halaman yang ingin ditampilkan
    page_size  : jumlah email per halaman
    """

    if page < 1 or page_size < 1:
        raise ValueError("Page dan page_size harus lebih dari 0")

    emails = load_emails()

    total_emails = len(emails)

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    selected_emails = emails[start_index:end_index]

    return {
        "page": page,
        "page_size": page_size,
        "total_emails": total_emails,
        "total_pages": (
            total_emails + page_size - 1
        ) // page_size,
        "emails": [
            {
                "email_id": email["email_id"],
                "sender": email["sender"],
                "subject": email["subject"],
                "received_at": email["received_at"]
            }
            for email in selected_emails
        ]
    }


def search_emails(
    query=None,
    start_date=None,
    end_date=None,
    page=1,
    page_size=5
):
    """
    Mencari email berdasarkan teks dan periode tanggal.

    query      : kata atau frasa pencarian
    start_date : tanggal awal, format YYYY-MM-DD
    end_date   : tanggal akhir, format YYYY-MM-DD
    """

    if page < 1 or page_size < 1:
        raise ValueError("Page dan page_size harus lebih dari 0")

    emails = load_emails()

    results = []

    for email in emails:

        received_date = datetime.fromisoformat(
            email["received_at"]
        ).date()

        # Filter tanggal awal
        if start_date:
            start = datetime.strptime(
                start_date, "%Y-%m-%d"
            ).date()

            if received_date < start:
                continue

        # Filter tanggal akhir
        if end_date:
            end = datetime.strptime(
                end_date, "%Y-%m-%d"
            ).date()

            if received_date > end:
                continue

        # Filter pencarian teks
        if query:
            searchable_text = " ".join([
                email["sender"],
                email["subject"],
                email["body"]
            ]).casefold()

            if query.casefold() not in searchable_text:
                continue

        results.append(email)

    total_results = len(results)

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    paginated_results = results[
        start_index:end_index
    ]

    return {
        "query": query,
        "total_results": total_results,
        "page": page,
        "page_size": page_size,
        "total_pages": (
            total_results + page_size - 1
        ) // page_size,
        "emails": [
            {
                "email_id": email["email_id"],
                "sender": email["sender"],
                "subject": email["subject"],
                "received_at": email["received_at"]
            }
            for email in paginated_results
        ]
    }


def read_email(email_id):
    """
    Membaca isi lengkap email berdasarkan email_id.
    """

    emails = load_emails()

    for email in emails:

        if email["email_id"] == email_id:
            return email

    return {
        "error": f"Email dengan ID {email_id} tidak ditemukan"
    }
