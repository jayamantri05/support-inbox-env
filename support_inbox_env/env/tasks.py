def load_task(name):
    return {
        "easy": {
            "id": "T1",
            "message": "I want a refund for my damaged product.",
            "expected": "refund"
        },
        "medium": {
            "id": "T2",
            "message": "My order is delayed and I'm unhappy.",
            "expected": "reply"
        },
        "hard": {
            "id": "T3",
            "message": "I was charged twice and support ignored me!",
            "expected": "refund"
        }
    }[name]