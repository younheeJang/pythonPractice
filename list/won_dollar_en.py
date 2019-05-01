# won -> dollar
def krw_to_usd(won):
    i = 0
    while i < len(won):
        won[i] = won[i] / 1000
        i = i + 1
    return won


# dollars -> en
def usd_to_jpy(dollars):
    i = 0
    while i < len(dollars):
        dollars[i] = (dollars[i] / 8) * 1000000
        i = i + 1
    return dollars
 

#
amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐: " + str(amounts))

print("미국 화폐: " + str(krw_to_usd(amounts)))

print("일본 화폐: " + str(usd_to_jpy(krw_to_usd(amounts))))