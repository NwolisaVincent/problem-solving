celebrity_list = [
    ["Beyonce", 6, 7],
    ["Taylor", 7, 9],
    ["Brad", 10, 11],
    ["Tom", 8, 10],
    ["Drake", 9, 11],
    ["Alica", 6, 8]
]


def celeb(celebrities):
    timeline = {}
    for celebrity in celebrities:
        name, arrive, leave = celebrity
        for time in range(arrive, leave + 1):
            if time in timeline:
                timeline[time] += 1
            else:
                timeline[time] = 1

    max_count = max(timeline.values())
    best_times = [time for time, count in timeline.items() if count == max_count]
    print("Best time(s) to come to the party to meet most celebrities: ")
    for t in best_times:
        print(f"Time: {t}:00, Celebrities present: {max_count}")


celeb(celebrity_list)





