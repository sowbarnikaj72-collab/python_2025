#quiz tezt

questions=[
    "1. Which of the following is the brain of the computer?",
    "2. Which of the following is an example of an input device?",
    "3. What does 'CPU' stand for?",
    "4. Which programming language is mainly used for web development?",
    "5. What is the full form of 'HTML'?",
    "6. Which storage device has no moving parts?",
    "7. Which company developed the Windows operating system?",
    "8. What does 'URL' stand for?"
    ]
options=[
    ["a) Hard Disk", "b) CPU", "c) Monitor", "d) RAM"],
    ["a) Printer", "b) Keyboard", "c) Speaker", "d) Monitor"],
    ["a) Central Processing Unit", "b) Central Power Unit", "c) Control Processing Unit", "d) Central Process Utility"],
    ["a) Python", "b) Java", "c) HTML", "d) C++"],
    ["a) Hyper Transfer Markup Language", "b) Hyper Text Markup Language", "c) High Text Machine Language", "d) Hyperlink and Text Management Language"],
    ["a) Hard Disk Drive", "b) Solid State Drive", "c) Compact Disk", "d) Magnetic Tape"],
    ["a) Apple", "b) Microsoft", "c) IBM", "d) Google"],
    ["a) Uniform Resource Locator", "b) Universal Reference Link", "c) Uniform Retrieval Locator", "d) Unified Resource Link"]]
guesses=[]
answers=["b", "b", "a", "c", "b", "b", "b", "a"]
question_num=0
score=0
print('___________________________________________________________________________________')
 
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option) 
    guess=input("Enter your answer:").lower()
    guesses.append(guess)
    if guess==answers[question_num]:
         print(f'your answer is correct') 
         score+=1
         print()
         
    else:
        print(f"incorrect, the correct iption is {answers[question_num]}")
    question_num+=1
    print()

print('_____________________________________________________________________________________')
print()
print(f" OUT OF {len(answers)} YOU GOT {score} RIGHT")
print(f' YOUR PERCENTAGE { score/len(answers) *100}%')
