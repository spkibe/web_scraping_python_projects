FROM python:3.10

ADD amazon_scrape.py .

RUN pip install requests bs4 pandas Pyarrow

CMD ["python", "./amazon_scrape.py"]