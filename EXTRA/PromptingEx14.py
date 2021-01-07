from sys import argv
script,userName = argv

prompt = "-->"
print("Hi ",userName,f"I'm the {script} script")
print("I'd like to ask you a few quetion.")
print(f"Do you like me {userName}")
likes = input(prompt)

print(f"Where do you live {userName}")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright , so you said {likes} about liking me,
You live in {lives} Not sure where that is.
And you have a {computer} computer. Nice
""")
