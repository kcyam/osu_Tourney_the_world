import string
import pycountry
from lxml import html
import requests

letters = list(string.ascii_uppercase)
letters.extend([i+b for i in letters for b in letters])
letters = letters[26:]

#country = 'MX'
#testCountry = pycountry.countries.get(alpha_2=country)
#print(testCountry.name)
#url = 'https://osu.ppy.sh/images/flags/MX.png'
#url2 = 'https://osu.ppy.sh/images/flags/cn.png'

#testRequest = requests.get(url)
#testPrint = testRequest.read()
#testHTML = html.fromstring(testRequest.content)
#print(str(testHTML).split()[1])

#file = open("sample_image.png", "wb")
#file.write(testRequest.content)
#file.close()

#testCountry = letters[30]
#testurl = 'https://osu.ppy.sh/images/flags/' + testCountry + '.png'
#print(testurl)

##country = pycountry.countries.get(alpha_2='AN')
##try:
##    countryName = country.name
##except:
##    countryName = "Test failed"
##
##    print(countryName)


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
