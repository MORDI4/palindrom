def palindorm_check(word):
    w = ''
    for i in word:
        if i.isalnum():
            w += i.lower()
    print(w)
    for i in range(round(len(w)/2)):
        if w[i] != w[(len(w)-1)-i]:
            return False   
    return True

print(palindorm_check("kajak"))
print(palindorm_check("Kobyla ma maly bok"))
print(palindorm_check("statek"))
