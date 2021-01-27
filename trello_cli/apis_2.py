from pprint import pprint
import requests
import private

def request_demo():
    """Explore how web request work"""
    url = "https://raw.githubusercontent.com/alissa-huskey/python-class/master/hello.txt"
    response = requests.get(url)

    # this shows us the body of the response
    print(response.text)


def request_astros():
    """Print out the astronauts currently in space using NASAs astros API
    https://api.nasa.gov/
    """

    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)

    # this shows us the body of the response
    print(response.text)


def request_hello():
    """Say "hello" in another language using the hellosalut API
    https://fourtonfish.com/hellosalut/hello/
    """
    url = "https://fourtonfish.com/hellosalut/"
    response = requests.get(url, params={'lang': 'de'})
    data = response.json()
    # print(data)
    print(data['hello'])


def request_activity():
    url = "https://www.boredapi.com/api/activity"
    response = requests.get(url, params={'participants': 1})
    data = response.json()
    print(data['activity'])


# request_demo()
# request_astros()
# request_hello()
request_activity()

print("latitude:", private.LAT)
print("longitude:", private.LNG)


