current_sentence = input('Entrez une phrase (ou "stop" pour terminer) : ')
while current_sentence != "stop":
    with open("phrases.txt", "a") as my_file:
        my_file.write(current_sentence + "\n")
    current_sentence = input('Entrez une phrase (ou "stop" pour terminer) : ')

print("\nVoici ce que vous avez écrit :")
with open("phrases.txt", "r") as my_file:
    print(my_file.read())