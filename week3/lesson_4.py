with open("about_me.txt", "r", encoding="utf-8") as file:
     text = file.readlines()
for line in text :
     print(line.strip())

