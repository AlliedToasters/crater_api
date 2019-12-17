import numpy as np
import subprocess
import json

def get_sub_imgs(img):
    scale = img.shape[0]
    sf = scale//32
    sub_images = []
    for i in range(sf):
        for j in range(sf):
            sub_image = img[j::sf,i::sf]
            sub_image = sub_image.reshape(1, -1)
            sub_images.append(sub_image)
    sub_images = np.concatenate(sub_images)
    return sub_images

def make_request(array):
    data = {
        "instances":array.tolist()
    }
    data_json = json.dumps(data)
    path = './tmp.json'
    with open(path, 'w') as f:
        f.write(data_json)

    base_url = "http://localhost:8501/v1/models/craters:predict"
    cmd = f"curl -d '@{path}' -X POST {base_url}"
    response = subprocess.check_output(cmd, shell=True).decode()
    response_data = eval(response)
    return response_data

def parse_predictions(predictions, sf):
    pred = np.array([np.array(x) for x in predictions])
    pred = pred.mean(axis=0)
    pred = pred * sf
    return pred

def handle_pixels(px):
    allowed = [1024,  4096, 16384, 65536]
    dim = len(px)
    if dim not in allowed:
        raise Exception('Unable to parse dim; array should have length of: ' + str(allowed))
    scale = int(np.sqrt(dim))
    sf = scale//32
    img = np.array(px).reshape(scale, scale)
    sub_imgs = get_sub_imgs(img)
    response = make_request(sub_imgs)
    predictions = response['predictions']
    pred = parse_predictions(predictions, sf)
    return pred
