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