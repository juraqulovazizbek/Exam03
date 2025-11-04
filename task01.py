ism = input("Ismingizni kiriting: ")
yosh = input("Yoshingizni kiriting: ")


with open("data.txt ", "a") as f:
    f.write(f"{ism} - {yosh} yosh\n")

