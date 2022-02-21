# import main Flask class and request object

from xml.dom import ValidationErr
from flask import Flask, request
import os
import yaml

# create the Flask app
app = Flask(__name__)

@app.route('/cpu')
def cpu_load():

    """    app_dir = os.path.dirname(os.path.realpath(__file__))
    auth_file = os.path.join(os.path.expanduser('~'),'/home/aether/Music/flask_req_ex/hpa/config.yaml')

    with open("{}/book.txt".format(app_dir), 'r') as book:
        lines = book.readlines()

    with open("{}/config.yaml".format(app_dir), 'r') as stream:
        try:
            input = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise ValidationErr("Error when parsing config.yml: {}".format(exc))

    olines = []

    for l in lines:
        if input['search'] in l:
            olines.append(l)
        
    return str(len(olines))
"""
    return "CPU page"
    
@app.route('/mem')
def form_example():
    return 'Form Memory'


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True, port=8000)

