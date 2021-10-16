import urllib.request
import json

phone = input("Enter phone: ")

getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone

try:
    infoPhone = urllib.request.urlopen(getInfo)
except:
    print("\n[!] - Phone not found - [!]\n")

infoPhone = json.load( infoPhone )

print( u"Номер сотового --->", "+" + phone )
print( u"Страна ---> ", infoPhone["country"]["name"] )
print( u"Регион ---> ", infoPhone["region"]["name"] )
print( u"Округ ---> ", infoPhone["region"]["okrug"] )
print( u"Оператор ---> ", infoPhone["0"]["oper"] )
print( u"Часть света ---> ", infoPhone["country"]["location"] )