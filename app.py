import os
import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

DOG_API = "https://dog.ceo/api/breeds/image/random"
CAT_API = "https://api.thecatapi.com/v1/images/search"

idioma = dict()



@app.route("/")
def index():
    animal = os.getenv("ANIMAL", "dog").lower()

    if animal == "cat":
        response = requests.get(CAT_API)
        image_url = response.json()[0]["url"]
        title = idioma["gato"]
    else:
        response = requests.get(DOG_API)
        image_url = response.json()["message"]
        title = idioma["perro"]

    return render_template(
        "index.html",
        image_url=image_url,
        title=title,
        button_msg=idioma["boton"]
    )

if __name__ == "__main__":
    
    idiomas = {
        "español": {
            "perro": "🐶 Perrito random",
            "gato": "🐱 Gatito random",
            "boton": "Otra foto"
        },

        "ingles": {
            "perro": "🐶 Random dog",
            "gato": "🐱 Random cat",
            "boton": "Another image"
        }
    }

    try:
        with open("appconf.json") as file:
            idioma = idiomas[json.load(file)["idioma"]]
    
    except:
        idioma = idiomas["ingles"]
    

    app.run(debug=True)

