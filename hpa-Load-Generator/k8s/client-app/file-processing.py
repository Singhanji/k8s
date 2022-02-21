# import main Flask class and request object
from xml.dom import ValidationErr
import os
import yaml

# create the Flask app
#def query_example():
app_dir = os.path.dirname(os.path.realpath(__file__))
auth_file = os.path.join(os.path.expanduser('~'),'/home/aether/Music/flask_req_ex/hpa/config.yaml')

with open("{}/book.txt".format(app_dir), 'r') as book:
    print(book.read())

"""with open("{}/config.yaml".format(app_dir), 'r') as stream:
    try:
            input = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise ValidationErr("Error when parsing config.yml: {}".format(exc))

    return True
""""""    if input['search'] in lines:
        return lines
    else:
        return "No record found"
"""

#if __name__ == '__main__':
#    print(query_example)
