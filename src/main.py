from connection import session
from models import Connexion
from datetime import datetime
from pathlib import Path
    
import socket

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

import time

while True:
    if is_connected():
      connexion = Connexion(source='application', status='connected', checked_at=datetime.now())
      session.add(connexion)
      session.commit()
    else:
        print("Internet perdu")

    time.sleep(10)
    