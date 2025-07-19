def palindrom_check(word):
    cleaned = [i.lower() for i in word if i.isalnum()]
    for i in range(round(len(cleaned)/2)):
        if cleaned[i] != cleaned[(len(cleaned)-1)-i]:
            return False   
    return True

print(palindrom_check("kajak"))
print(palindrom_check("Kobyla ma maly bok"))
print(palindrom_check("statek"))
