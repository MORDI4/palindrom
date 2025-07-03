def palindorm_check(word):
    for i in range(round(len(word)/2)):
        if word[i] != word[(len(word)-1)-i]:
            return False
    return True

print(palindorm_check("kajak"))
print(palindorm_check("statek"))