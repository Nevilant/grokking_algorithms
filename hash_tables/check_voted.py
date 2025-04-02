voted = {"Ivan": "Voted"}


def check_voted(name):
    if name in voted:
        print(f"{name} already voted")
    else:
        voted[name] = "Voted"
        print(f"{name} ready to vote")


# Вызываем функцию для обоих имен
check_voted("Ivan")
check_voted("Lev")
check_voted("Lev")

print(voted)
