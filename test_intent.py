
from src.intent_parser import parse_intent
from src.date_parser import get_date_range


requests = [
    "Tolong carikan email tagihan yang belum dibayar bulan ini.",
    "Ada jadwal kunjungan vendor minggu ini?",
    "Tampilkan seluruh daftar email saya.",
    "Cari informasi promo belanja.",
    "Baca email dengan ID E002."
]


for request in requests:

    print("\n" + "=" * 60)
    print("USER REQUEST:")
    print(request)

    try:
        intent = parse_intent(request)

        print("\nINTENT:")
        print(intent)

        date_range = get_date_range(
            intent["date_period"]
        )

        print("\nDATE RANGE:")
        print(date_range)

    except Exception as error:
        print("ERROR:", error)
