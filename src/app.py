# import functions
from utils.onvif import set_time

# config
import configparser
config = configparser.ConfigParser()
config.read('cams.conf')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "Add camera name to update time", 200

@app.route('/<cam>')
def update_cam(cam:str):
	if cam in config:
		t = set_time(
			config[cam]['host'],
			config[cam]['port'],
			config[cam]['user'],
			config[cam]['pass']
		)

		if t is None:
			return f"Unable to set time for cam '{cam}'", 500
		
		return f"Time for cam '{cam}' set to {t:%Y-%m-%d %H:%M:%S}", 200
	return f"Cam '{cam}' configuration not found", 404

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)