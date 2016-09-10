"""
Kodi notification service.

For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/notify.kodi/

notify:
  platform: kodi
  host: http://192.168.0.123    (Required)
  port: 8080                    (Required)
  name: Kodi                    (Optional)
  username: USERNAME            (Optional)
  password: PASSWORD            (Optional)
"""
import logging
import urllib

from homeassistant.components.notify import (ATTR_TITLE, ATTR_TITLE_DEFAULT,
                                             ATTR_DATA,
                                             BaseNotificationService, DOMAIN)

_LOGGER = logging.getLogger(__name__)
REQUIREMENTS = ['jsonrpc-requests==0.3']

ATTR_DISPLAYTIME = 'displaytime'
ATTR_ICON = 'icon'


def get_service(hass, config):
    """Return the notify service."""
    url = '{}:{}'.format(config.get('host'), config.get('port', '8080'))

    jsonrpc_url = config.get('url')  # deprecated
    if jsonrpc_url:
        url = jsonrpc_url.rstrip('/jsonrpc')

    auth = (config.get('username', ''),
            config.get('password', ''))

    return KODINotificationService(
        config.get('name', 'Kodi'),
        url,
        auth
    )


# pylint: disable=too-few-public-methods
class KODINotificationService(BaseNotificationService):
    """Implement the notification service for Kodi."""
    def __init__(self, name, url, auth=None):
        """Initialize the service."""
        import jsonrpc_requests
        self._name = name
        self._url = url
        self._server = jsonrpc_requests.Server(
            '{}/jsonrpc'.format(self._url),
            auth=auth,
            timeout=5)

    def send_message(self, message="", **kwargs):
        """Send a message to Kodi."""
        try:
            data = kwargs.get(ATTR_DATA)
            displaytime = 10000
            icon = "info"

            if data is not None and ATTR_DISPLAYTIME in data:
                displaytime = data.get(ATTR_DISPLAYTIME, 10000)

            if data is not None and ATTR_ICON in data:
                icon = data.get(ATTR_ICON, "info")

            title = kwargs.get(ATTR_TITLE, ATTR_TITLE_DEFAULT)
            self._server.GUI.ShowNotification(title, message, icon,
                                              displaytime)
        except ErrorException as exception:
            _LOGGER.warning('Unable to fetch kodi data, "%s"', exception)
