# kodi notification for Home Assistant

Place the `kodi.py` file into your `/custom_components/notify/` folder

##Usage Example##

###configuration.yaml example###
```yaml
# Example configuration.yaml entry
notify:
  platform: kodi
  name: kodi_test
  host: http://192.168.0.123
  port: 8080
  name: Kodi
  username: USERNAME
  password: PASSWORD
```
Configuration variables:
- **host** (*Required*): The host name or address of the device that is running XBMC/Kodi
- **port** (*Required*): The port number, *default 8080*
- **name** (*Optional*): Name displayed in the frontend.
- **username** (*Optional*): The XBMC/Kodi HTTP username.
- **password** (*Optional*): The XBMC/Kodi HTTP password.

###script.yaml example###
```yaml
################################################################
## Script / Notify KODI
################################################################
kodi_notification:
  sequence:
  - service: notify.kodi
    data:
      title: "Home Assistant"
      message: "Message to KODI from Home Assistant!"
      data:
        displaytime: 20000
        icon: "warning"
```
message variables:
- **title** (*Optional*): Title that is displayed on the message.
- **message** (*Required*): Message to be displayed.
- **data** (*Optional*): Name displayed in the frontend.
  - **icon** (*Optional*): Kodi comes with 3 default icons: "info", "warning" and "error", url to an image is also valid. *Defaults to "info"*
  - **displaytime** (*Optional*): Length in milliseconds the message stays on screen. *Defaults to 10000s*
