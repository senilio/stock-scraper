# stock-scraper
This thing was created as I was trying to get my hands on a PS5. It will scan your defined sites periodically, and let you know via Pushover when you have a hit.

## config.json
```
{
  "Sites": {
    "Amazon1": {
      "Keyword": "exports_desktop_qualifiedBuybox_priceInsideBuyBox",
      "URL": "https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG"
    },
    "Amazon2": {
      "Keyword": "Currently unavailable.",
      "Reverse search": true,
      "URL": "https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG"
    }
  },
  "Settings": {
    "Pushover token": "abcdefghijklmnopqstuvwxyz12345",
    "Pushover key": "abcdefghijklmnopqstuvwxyz12345"
  }
}
```

The sites section contains one entry per site. Keyword and URL are mandatory.
The scraper will trigger when Keyword is found in the URL HTML code. The "Reverse search" variable is optional, and will reverse the search conditions, meaning that the scraper will trigger when the Keyword is NOT found in the URL HTML code.

## Run standalone
1. `pip install fake_useragent python-pushover`
2. Edit your config.json. This may take some trial and error to get right.
3. Either run the script from crontab, or use looper.sh to trigger the scraper at a reasonable interval.
4. Wait

## Run in Docker
1. Build the container: `docker build -t stock-scraper .`
2. Run the container using docker up or docker-compose. I prefer the later: `docker-compose up`.
