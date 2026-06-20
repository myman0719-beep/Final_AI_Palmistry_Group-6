from flask import Flask
from flask import request
from flask import jsonify

from predict_palm import predict_palm

from flask import render_template

import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    filepath = os.path.join(
        "uploads",
        file.filename
    )

    file.save(filepath)

    print("Saved:", filepath)

    result = predict_palm(filepath)

    print(result)

    return jsonify(result)


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )