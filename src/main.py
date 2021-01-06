# Dołączanie modułu flask 

from flask import Flask
from flask_session import Session

# Tworzenie aplikacji
app = Flask("MapEvents")


# Uruchomienie applikacji w trybie debug
app.config.from_object(__name__)
app.run(debug = True)