from time import sleep

line_break = "=" * 53

questions = ["What is object oriented programming?"]
ans_correct = 0

def time():
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)

for num, question in enumerate(questions):
    print(line_break)
    print("The quiz will now start.")
    print(line_break)
    print(f"Question {num}: {question}")
    print("")
    time()
    print("")
    print("Did you get that right?")
    print(line_break)
    answer = input(">>>")
