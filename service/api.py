from flask import request, jsonify
from service import app
from service.route import handle_pixels

@app.route("/", methods=["POST"])
def root():

    json=request.get_json(force=True, silent=True)
    pixels = json['instances'][0]
    pred = handle_pixels(pixels)

    return jsonify({
        'predictions': str(pred)
    })


@app.route("/healthcheck")
def healthcheck():
    return jsonify({
        'status': 'ok'
    })
