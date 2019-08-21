import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('demo.csv', 'w'))
f.writerow(['Place', 'City', 'State', 'Country', 'About', 'More About Place'])

pages = []
for i in range(1, 10, 1):
    url = "https://www.holidify.com/places/shimla/mall-road-shimla-sightseeing-350" + str(i) + '.html'
    pages.append(url)
    for item in pages:
        page = requests.get(item)
        soup = BeautifulSoup(page.text, 'html.parser')
        Place = list(soup.find(class_="col-md-10 col-xs-10 nopadding"))[1].get_text()
        City = list(soup.find_all(class_="smallerText"))[1].get_text()
        State = list(soup.find_all(class_="smallerText"))[2].get_text()
        Country = list(soup.find_all(class_="smallerText"))[3].get_text()
        About = list(soup.find_all(class_="biggerTextOverview"))[0].get_text()
        more_About = list(soup.find_all(class_="objHeading smallerText"))[0].get_text()
        Weather = soup.find(class_="currentWeather").get_text()
        f.writerow([Place, City, State, Country, About, more_About])

'''demo = pd.DataFrame({"Place": Place, "City": City, "State": State, "Country": Country, "About": About,
                     "More About Places": more_About}, index=[0])
demo.to_csv('demo.csv', index=False, encoding='utf-8', mode = 'a') '''

#Time_Required = soup.find(class_="objText").get_text()
# print(City)
# print(State)
# print(Country)
# print(About)
# print(more_About)
# print(Weather)
# print(Time_Required)
# html = list(soup.children)[2]
# print(list(html.children))
# print([type(item) for item in (list(soup.children))])
# print(list(soup.children))
# col_6=soup.find_all(class_="col-md-6 col-xs-12")
# print(col_6)
# seven_day = soup.find(id="seven-day-forecast")
# forecast_item = soup.find_all(class_="tombstone-container")
# overnight = forecast_item[0]
# print(overnight)

