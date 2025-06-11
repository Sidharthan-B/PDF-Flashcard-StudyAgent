from datetime import datetime, timedelta

def schedule_next_review(card, quality):
    ef = card.get("ef", 2.5)
    interval = card.get("interval", 1)
    repetitions = card.get("repetitions", 0)

    if quality < 3:
        repetitions = 0
        interval = 1
    else:
        if repetitions == 0:
            interval = 1
        elif repetitions == 1:
            interval = 6
        else:
            interval = int(interval * ef)

        ef = ef + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
        ef = max(1.3, min(ef, 2.5))
        repetitions += 1

    card["ef"] = ef
    card["interval"] = interval
    card["repetitions"] = repetitions
    card["next_review"] = (datetime.now() + timedelta(days=interval)).isoformat()
    return card
