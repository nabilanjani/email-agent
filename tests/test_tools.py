
from src.tools.mock_email_tools import (
    list_emails,
    search_emails,
    read_email
)


def test_list_emails():
    result = list_emails(page=1, page_size=5)

    assert result["total_emails"] == 10
    assert len(result["emails"]) == 5


def test_search_emails():
    result = search_emails(query="internet")

    assert result["total_results"] == 2


def test_search_by_date():
    result = search_emails(
        start_date="2026-11-01",
        end_date="2026-11-30"
    )

    assert result["total_results"] == 9


def test_read_email():
    result = read_email("E001")

    assert result["email_id"] == "E001"
    assert result["subject"] == "Invoice Gas Rumah November 2026"


def test_read_nonexistent_email():
    result = read_email("E999")

    assert "error" in result
