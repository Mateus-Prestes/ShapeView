import os

from flask import request, Response, redirect, url_for, render_template
from werkzeug.utils import secure_filename


from app import app

from app.geragrafico import grafico 

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'shapefiles')
@app.route('/uploads', methods=['POST'])
def upload():
  file = request.files['shapefiles']
  savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
  file.save(savePath)
  return "Tá rodando"


@app.route('/showgraphs', methods=['GET'])
def showGraphs():
    grafico()
    return Response(status = 201)
