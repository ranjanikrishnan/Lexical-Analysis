FROM python:3.7
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python ./mongo/seed_db.py 
CMD python ./src/app.py