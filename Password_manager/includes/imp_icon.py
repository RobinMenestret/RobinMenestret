import requests
import shutil
from copy import copy

def save_icon(url:str, name=""):
    if name == "":
        name = copy(url)
    response = requests.get("https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url="+ url +"&size=256", stream = True)

    with open('favicons/' + name + '.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

if __name__ == "__main__":
    save_icon(url = "https://pypi.org/", name = "Pypi")