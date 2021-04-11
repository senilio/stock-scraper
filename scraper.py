import requests
import pushover
import json
import fake_useragent

def send_push(title, message, token, key):
    pushover.init(token)
    pushover.Client(key).send_message(
            message,
            title=title)

def generate_headers():
    return {
        'User-Agent': ua.random,
        'Referrer': 'https://google.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Pragma': 'no-cache'
    }

def checker(url, keyword):
    r = requests.get(url, headers=generate_headers(), timeout=5)
    if 'CAPTCHA' in r.text:
        print("You may have hit the CAPTCHA on %s" % url)
    if (reverse_search == True and not keyword in r.text) or (reverse_search == False and keyword in r.text):
        print("There is a hit on " + url)
        return ':)'

def main():
    # Global variables
    global reverse_search
    global ua

    # Fetch some User Agent string from the internet
    ua = fake_useragent.UserAgent()

    # Open our config file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Loop through the web pages listed in the config file
    for i in config['Sites']:
        try:
            reverse_search = config['Sites'][i]['Reverse search']
        except KeyError:
            reverse_search = False

        result = checker(
                config['Sites'][i]['URL'],
                config['Sites'][i]['Keyword'])

        if result == ':)':
            send_push(
                    "Check out " + i,
                    config['Sites'][i]['URL'],
                    config['Settings']['Pushover token'],
                    config['Settings']['Pushover key'])

if __name__ == '__main__':
    main()
