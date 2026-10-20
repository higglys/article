word = input("Enter word: ")

with open("article.txt", "r", encoding="utf-8") as file:
    text = file.readlines()

count = 0

for line in text:
    if word.lower() in line.lower():
        count += 1

print("Number of lines:", count)
