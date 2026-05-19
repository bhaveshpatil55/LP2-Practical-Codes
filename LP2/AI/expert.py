# ============================================
#  AI Practical - Expert System
#  Application: Help Desk Management System
#  SPPU TE Computer - Artificial Intelligence
# ============================================

# Knowledge Base - Problems and Solutions
problem_dict = {
    "Printer not working"           : "Check printer power and network connection.",
    "Can't log in"                  : "Check your username and password.",
    "Software not installing"       : "Check system requirements and storage space.",
    "Internet connection not working": "Restart your modem or router.",
    "Email not sending"             : "Check email server settings and internet connection."
}

# Function to handle user request
def handle_request(user_input):
    if user_input.lower() == "exit":
        return "Goodbye!"
    elif user_input in problem_dict:
        return problem_dict[user_input]
    else:
        return "Sorry! Solution not available."

# Main Program
print("=== Help Desk Management System ===")
print("Available Problems:")
for i, problem in enumerate(problem_dict.keys(), 1):
    print(f"  {i}. {problem}")

# Main Loop
while True:
    user_input = input("\nEnter your problem (or type exit): ")
    response = handle_request(user_input)
    print("Solution:", response)
    if user_input.lower() == "exit":
        break