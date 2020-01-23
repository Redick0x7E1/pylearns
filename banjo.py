def areYouPlayingBanjo(name):
    list = []
    for char in name:
        list.append(char)
    if list[0] == "R" or list[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print(areYouPlayingBanjo('Sophia'))