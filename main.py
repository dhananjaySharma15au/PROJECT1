print("You want to play")
answerWronged = 0
answerAsked = 0
choice = input().lower()
if choice == "no":
  quit()

print("let's start")

print("1. what is the capital of france")
answerAsked += 1
answer = input().lower()
if answer == "paris":
  print("correct")
else:
  print("incorrect")
  answerWronged += 1
  print("the correct answer is paris")

print("2. what is the capital of germany")
answerAsked += 1
answer = input().lower()
if answer == "berlin":
  print("correct")
else:
  print("incorrect")
  answerWronged += 1
  print("the correct answer is berlin")

print("3. what is the capital of italy")
answerAsked += 1
answer = input().lower()
if answer == "rome":
  print("correct")
else:
  print("incorrect")
  answerWronged += 1
  print("the correct is Rome")

print("4. what is the capital of spain")
answerAsked += 1
answer = input().lower()
if answer == "madrid":
  print("correct")
else:
  print("incorrect")
  answerWronged += 1
  print("the correct answer is madrid")

print("you got " + str(answerAsked - answerWronged) + " correct")

print(str((answerAsked - answerWronged) / answerAsked * 100) + "%")
