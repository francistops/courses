def get_test_score(answer_sheet, student_answers):
    good_answer = 0
    for i in range(len(answer_sheet)):
        if answer_sheet[i] == student_answers[i]:
            good_answer += 1
    total = good_answer / len(answer_sheet) * 100

    return total
