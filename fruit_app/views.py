from django.http import JsonResponse


def send_fruits(request):
    fruits = [
        {
            "name": "Apfel",
            "gewicht": 180,
            "farbe": "Rot",
        },
        {
            "name": "Banane",
            "gewicht": 120,
            "farbe": "Gelb",
        },
        {
            "name": "Orange",
            "gewicht": 200,
            "farbe": "Orange",
        },
        {
            "name": "Kiwi",
            "gewicht": 90,
            "farbe": "Braun",
        },
        {
            "name": "Traube",
            "gewicht": 8,
            "farbe": "Lila",
        },
    ]

    return JsonResponse(
        fruits, safe=False
    )  # erwartet standardmäßig ein Dictionary. Da wir eine Liste zurückgeben muss safe=False gesetzt werden.
