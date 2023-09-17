import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier


notifier = ToastNotifier()


def get_data(url):
    req = requests.get(url)
    return req.text

html_data = get_data("https://weather.com/en-IN/weather/today/l/a46f6935eccacff15f256a4231321d692d5bd9199469f8341f4f7c22fc2c9ef4")

bSoup = BeautifulSoup(html_data, "html.parser")
# print(bSoup.prettify())
# exit()

current_temp = bSoup.find("span", class_="CurrentConditions--tempValue--MHmYY").text
city = bSoup.find("h1", class_="CurrentConditions--location--1YWj_").text

time = bSoup.find("span", class_="CurrentConditions--timestamp--1ybTk").text

temp = (str(current_temp))
city = str(city)
time = str(time)

result = temp + "  in "+ city + " " + time

notifier.show_toast("Weather update", result, duration = 10)
