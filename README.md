# onvif-time-sync
Set cameras time via ONVIF

# Configuration
Use the [cams.conf](cams.conf)-file to configure access to all cameras.
For every camera, provide a block as follows:
```conf
[CameraName]
host: <ip adress of camera>
port: <onvif port e.g 2020>
user: <http basic auth user>
pass: <http basic auth password>
```

# Running the API
The API can be launched in two ways: either directly via python or via docker.

## Python
Install the requirements from [src/requirements.txt](src/requirements.txt).

One option is to create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r src/requirements.txt
```

Then you can simply run the [src/app.py](src/app.py)
```bash
python3 src/app.py
```

## Docker
To launch the app in a docker container, there is the [compose.yaml](compose.yaml).

Start the docker container by executing the following command in the working directory:
```bash
docker-compose up -d
```

This will build the docker image and launch a container on port 5000.
Modify the [compose.yaml](compose.yaml) as needed.

This will launch the API on port 5000.