#Exercise : 14

#Promoting and Passing

from sys import argv
argv[0] = "Alexa"
bot, user_name = argv
prompt = '-->'
print(f"hi {user_name}, I am {bot} your assistant.")
print("i 'd like to ask some questions.")
print(f"do you like me {user_name}?")
like = input(prompt)
print(f"where do you live {user_name}?")
lives = input(prompt)
print(f"what kind of computer you have?")
computer = input(prompt)
print(f"""
Alright, so you said {like} about liking me.
you live in {lives}. 
and you have a {computer} computer.
""")
