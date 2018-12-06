print("Answer the following algebra question: ")

question_list = [
    {
        "question": {
            "1": "Answer the following algebra question:",
            "2": "If x = 8, then what is the value of 4(x + 3) ?"
        },
        "answer": {
            "1.": 35,
            "2.": 36,
            "3.": 40,
            "4.": 44
        },
        "correct_answer": 4
},
    {   
        "question": {
            "1": "Estimate this answer (exact calculation not needed): ",
            "2": "Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean? "
        },
        "answer": {
            "1.": "About 55",
            "2.": "About 65",
            "3.": "About 75",
            "4.": "About 85"
        },
        "correct_answer": 2
}
]

correct_answer = 0
for i in question_list:
    quest = i["question"]
    ans = i["answer"]
    quest = dict(quest)
    for j in quest.values():
        print(j)
    for k,v in ans.items():
        print(k,v)
        
    user_choice = int(input("Your choice: "))
    if user_choice == i["correct_answer"]:
        correct_answer += 1
        print("Bingo")
    else:
        print(":(")

print("Your correctly answer", correct_answer, "out of 2 questions")