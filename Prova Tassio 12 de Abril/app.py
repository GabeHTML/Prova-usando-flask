from flask import Flask, render_template
from categoria import Categoria
from video import Video

app = Flask(__name__)

video_zoeira = [video(1 'zoeira')]
video_react = [video(2 'react')]
video_tiktok = [video(3 'tiktok')]

categoria_list = []
categoria_list.append(Categoria(1, 'zoeira', video_zoeira))
categoria_list.append(Categoria(2, 'react', video_react))
categoria_list.append(Categoria(3, 'tiktok', video_tiktok))

@app.route("/")
def index():
    return render_template("index.html", categoria_list = categoria_list)

@app.route("/video/<id>")
def react(id):
    for categoria in categoria_list:
        for video in categoria.get_video_list():
            if str(video.get_id()) == id:
                return render_template("react.html", video = video)
    return render_template("index.html", categoria_list = categoria_list)

@app.route("/video/<id>")
def zoeira(id):
    for categoria in categoria_list:
        for video in categoria.get_video_list():
            if str(video.get_id()) == id:
                return render_template("zoeira.html", video = video)
    return render_template("index.html", categoria_list = categoria_list)

@app.route("/video/<id>")
def tiktok(id):
    for categoria in categoria_list:
        for video in categoria.get_video_list():
            if str(video.get_id()) == id:
                return render_template("tiktok.html", video = video)
    return render_template("index.html", categoria_list = categoria_list)