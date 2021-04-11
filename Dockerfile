FROM python:3
ADD looper.sh /
ADD scraper.py /
RUN pip install fake_useragent python-pushover
CMD ["./looper.sh"]
