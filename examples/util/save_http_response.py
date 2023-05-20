import requests
import json

from lib.util.create_path_to_local_file import create_path_to_local_file

new_file_path = create_path_to_local_file(__file__, "response_fixture.json")
r = requests.get('https://xkcd.com/info.0.json')
text_file = open(new_file_path, "w")
n = text_file.write(json.dumps(r.json(), indent=4))
text_file.close()
