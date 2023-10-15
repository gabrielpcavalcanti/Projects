from gtts import gTTS
import string
import random

language = 'de'

numbers = range(0,10)

text = "1, 2, 3, and go, "

for i in range(20):

    l = random.choice(numbers)

    text = ''.join((text, str(l) + ","))


speech = gTTS(text=text, lang=language, slow=False)

speech.save("sample.mp3")

print("Would you like to see the answer? type Y ou y for yes and N or n to no.")

answer = input()

if answer == 'y' or answer == 'Y':
    print(text)

else:
    print("run the code again")


