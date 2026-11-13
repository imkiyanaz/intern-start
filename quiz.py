score = 0

answer = input("What is 2 + 3? ")
if answer == "5":
    score += 1

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    score += 1

answer = input("What is 4 * 2? ")
if answer == "8":
    score += 1

print("Your score:", score, "/3")