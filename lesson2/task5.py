
def calculate_avg_score(scores):
    return round(sum(scores) / len(scores))


if __name__ == '__main__':

    SCHOOL_CLASSES = [
        {'school_class': '4a', 'scores': [5, 5, 5, 5, 5]},
        {'school_class': '5a', 'scores': [2, 2, 2, 2, 2]},
        {'school_class': '6a', 'scores': [3, 4, 4, 5, 2]}
    ]

    all_school_scores = []

    for school_class in SCHOOL_CLASSES:
        scores = school_class.get('scores')
        all_school_scores.extend(scores)
        avg_score = calculate_avg_score(scores)

        print("Средний балл класса {school_class}: " "{avg_score}".format(
            school_class=school_class.get('school_class'), avg_score=avg_score))

    avg_school_score = calculate_avg_score(all_school_scores)
    print("Средний балл школы {avg_school_score}".format(
        avg_school_score=avg_school_score))
