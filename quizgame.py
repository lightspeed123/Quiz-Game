##### 1. QUIZ GAME 

questions = [
    {
    "Prompt" : "Q1) What is the capital of France?",
    "Options"  : " A. Berlin, B. London,  C. Paris,  D. Madrid ",
    "Answer" : "A"
    },
    {
    "Prompt" : "Q2) Which language is primarily spoken in Brazil? " ,
    "Options": " A. Spanish,  B. Portuguese,  C. English,  D. French " ,
    "Answer" : "B"
    },
    {
    "Prompt" : "Q3) What is the smallest prime number?",
    "Options": "A. 2,   B. 3,  C. 1,  D. 5" ,
    "Answer": "B"
    },
    {
    "Prompt": "Q4) Who wrote To Kill a Mockingbird? ",
    "Options" :"A. Harper Lee, B. Mark Twain, C. J.K. Rowling,  D. Ernest Hemingway ",
    "Answer": "A"
    }
]
Score = 0
for question in questions:
    print(question["Prompt"])
    print(question["Options"])
    user_answers = input("Enter your answer (A/B/C/D) : ").upper()
    if user_answers == question["Answer"]:
        print("Correct answer\n")
        Score += 1
    else:
        print(f"Sorry! Wrong Answer, the correct answer is {question["Answer"]} \n")
print("Quiz Completed Successfully \n")
print("Your score is : ", Score)
                