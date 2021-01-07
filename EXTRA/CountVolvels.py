#This program Whill count number  of vowel and consonant in name.
name = "Vishal Kumar"
#lengthOfString = len(name)
#i = 0
countVowel = 0
countConsonant = 0
for i in name:
    print(i,end = '')
    if i == 'a' or i == 'A' :
        countVowel = countVowel + 1
    elif i == 'e' or i == 'E' :
        countVowel = countVowel + 1
    elif i == 'i' or i == 'I' :
        countVowel = countVowel + 1
    elif i == 'o' or i == 'O' :
        countVowel = countVowel + 1
    elif i == 'u' or i == 'U' :
        countVowel = countVowel + 1
    elif i == ' ':
        continue
    else:
        countConsonant = countConsonant + 1
print(f"You'r name contain {countVowel} vowel and {countConsonant} consonant")
