FROM nexus.petrobras.com.br:5000/python:3.7

WORKDIR /usr/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/app

EXPOSE 8011

CMD [ "python", "app.py" ]