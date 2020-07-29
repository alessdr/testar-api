from flask import Flask, render_template, flash, request, redirect, send_file
from waitress import serve
import logging

LOG_FILE = 'testador_api.log'

app = Flask(__name__)
app.secret_key = "secret key"

logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/log')
def download_log():
    # Prepara o retorno
    retorno = send_file(LOG_FILE, mimetype=None, as_attachment=True, attachment_filename=LOG_FILE)
    return retorno


if __name__ == '__main__':
    app.run(debug=True, port=8011)
    #serve(app, host='0.0.0.0', port=8011, threads=10)
