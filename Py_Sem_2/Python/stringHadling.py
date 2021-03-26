message = 'Say Hello' \
          ' there! are more lines'
print(message)
print(len(message))
print('Hello' in message)

message1 = "Hello there, how do you do?"
print(len(message1))

newMessage = message1[0:message1.index(',')]
print(newMessage)

# to remove white space from start and end of the string
greeting = " Good Morning      "
print(greeting.upper())
print(greeting.lower())
print(greeting.split('o'))
print(greeting.replace('o', '0'))

age = 21
name = 'Vishal Kumar'
print(f"Employee name is {name} and he is  {age} year's old!")

firstName = "Vishal"
secondName = "Kumar"
fullName = firstName+" "+secondName

message3 = 'Hello there, what\'s your name?'
print(message3)
print(fullName)