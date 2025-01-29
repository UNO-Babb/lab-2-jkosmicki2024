#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
answers = ["Yes.", "No", "Don't count on it.", "Do count on it", "Ask later.", "Unclear.", "For sure.", "Look inside yourself."]
  #Answer question randomly with one of the options from your earlier list.

num = random.random()
num = num * 11
num = int(num) 
num = num % 20 # 0 - 19
question = input("Ask me a question.")
print(answers[num]) 


if __name__ == '__main__':
  main()
