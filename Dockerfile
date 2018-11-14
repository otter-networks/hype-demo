FROM python
WORKDIR /elementsapp

COPY . /elementsapp

RUN pip install -r requirements.txt

EXPOSE 8080

CMD python app.py