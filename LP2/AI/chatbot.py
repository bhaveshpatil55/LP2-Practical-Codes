# ============================================
#  AI Practical - Elementary Chatbot
#  SPPU TE Computer - Artificial Intelligence
# ============================================

# Function to greet user
def greet(bot_name, birth_year):
    print("Hello! My name is", bot_name)
    print("I was created in", birth_year)

# Function to ask user's name
def remind_name():
    print("Please tell me your name:")
    name = input()
    print("Nice to meet you,", name)

# Function to guess age
def guess_age():
    print("Let me guess your age.")
    print("Enter remainder of your age when divided by 3:")
    rem3 = int(input())
    print("Enter remainder when divided by 5:")
    rem5 = int(input())
    print("Enter remainder when divided by 7:")
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is", age)

# Function for counting
def count():
    print("Enter a number:")
    num = int(input())
    counter = 0
    while counter <= num:
        print(counter)
        counter += 1

# Function for quiz
def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat statements")
    print("2. To divide program into small parts")
    print("3. To stop program")
    print("4. To find errors")
    answer = 2
    guess = int(input())
    while guess != answer:
        print("Wrong answer. Try again.")
        guess = int(input())
    print("Correct Answer!")

# Ending function
def end():
    print("Congratulations!")
    print("Have a nice day.")

# ---- Main ----
greet("TE-Chatbot", "2022")
remind_name()
guess_age()
count()
test()
end()
