def get_test_score(answer_sheet, student_answers):
    good_answers = 0
    for i in range(len(answer_sheet)):
        if answer_sheet[i] == student_answers[i + 1]:
            good_answers += 1
    score = good_answers / len(answer_sheet) * 100
    return student_answers[0], score
