import os
import flask
from flask import request, jsonify
import json

import ocr

app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/ocr/v1/url', methods=['POST'])
def url():

    img_url = request.json['url']
    language = request.json['language']

    text = ocr.img_to_text(img_url, language)
    
    response = dict()
    if not text == None:
        response = jsonify(dict(success=True, text=text))
    else:
        response = jsonify(dict(success=False))

    return response