import string
import pycountry
from lxml import html
import requests

letters = list(string.ascii_uppercase)
letters.extend([i+b for i in letters for b in letters])
letters = letters[26:]

for letter in letters:
    url = 'https://osu.ppy.sh/images/flags/' + letter + '.png'
    request = requests.get(url)
    tempHTML = html.fromstring(request.content)
    if str(tempHTML).split()[1] == 'p':
        country = pycountry.countries.get(alpha_2=letter)
        try:
            countryName = country.name
        except:
            countryName = letter
            
        destinationImage = open(countryName + ".png", "wb")
        destinationImage.write(request.content)
        destinationImage.close()
        
    else:
        print ("Letters did not have a country: " + letter)
