import time
import threading
import pickle
from telegramParser import parser

# Parse
def parse():
    films = parser()
    return films

# Save
def saveCache(data):
    with open("cache.pkl", "wb") as f:
        pickle.dump((data, time.time()), f)

# Read
def loadCache():
    try:
        with open("cache.pkl", "rb") as f:
            data, timestamp = pickle.load(f)
            return data, timestamp
    except Exception:
        return None, None
    
# Background timer
def backgroundParse():
    while True:
        films = parser()
        saveCache(films)
        print("Cache updated!")
        time.sleep(3600)

threading.Thread(target=backgroundParse, daemon=True).start()

def getTop():
    data, timestamp = loadCache()
    if data is None:
        return "Data is not updated yet, wait please."
    lines = []
    for i, film in enumerate(data):
        name = film.get('name', 'No name')
        rating = film.get('rating', 'N/A')
        url = film.get('url', None)
        if url: 
            name = f'<a href="{url}">{name}</a>'
        lines.append(f"{i+1}. {name} - {rating}")
    return lines