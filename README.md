# kodi notification for Home Assistant

Place the `kodi.py` file into your `/custom_components/notify/` folder

##Usage Example##

###configuration.yaml example###
```
# Example configuration.yaml entry
notify:
  platform: kodi
  name: kodi_test
  host: http://192.168.0.123
  port: 8080
  name: Kodi
  user: USERNAME
  password: PASSWORD
```
- **host** (*Required*): The host name or address of the device that is running XBMC/Kodi
- **port** (*Required*): The port number, *default 8080*
- **name** (*Optional*): Name displayed in the frontend.
- **username** (*Optional*): The XBMC/Kodi HTTP username.
- **password** (*Optional*): The XBMC/Kodi HTTP password.


###script.yaml example###
```
################################################################
## Script / Notify KODI
################################################################

kodi_test:
  sequence:
  - service: notify.kodi
    data:
      title: "Home Assistant"
      message: "Message to KODI from Home Assistant!"
```
