import json, logging, threading

from comps.lamps import error, status_spoiler

data = {}

def read_json():
  #ließt die json datei ein ...
    try:
        with open("./thorsten.json", "r") as read_file:
            global data
            data = json.load(read_file)


    except FileNotFoundError:
        logging.error("Config Datei kann nicht gefunden werden.")
        t1 = threading.Thread(target=error.seterrorled)
        t2 = threading.Thread(target=status_spoiler.setspoilererrorled)

        t1.start()
        t2.start()



