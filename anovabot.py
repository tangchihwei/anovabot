from slackclient import SlackClient
import os
import time
import json
from pycirculate.anova import AnovaController
import datetime

token = "xxxxxxx"
ANOVA_MAC_ADDRESS = "xxxxxx"


# ctrl = AnovaController(ANOVA_MAC_ADDRESS)
# sc = SlackClient(token)
# if sc.rtm_connect():
#   while True:
#     response = sc.rtm_read()
#     for message_type in response:
#       if message_type.get('text'):
#         message = message_type.get('text')
#         print ctrl.set_temp(float(message))
#         print ctrl.start_anova()
#         print ctrl.set_timer(60)
# #        print ctrl.start_timer()
#     time.sleep(1)
# #    if ctrl.read_temp() == 147.2 and ctrl.rea:
#  #     print ctrl.start_timer()
#     print ctrl.anova_status()
# else:
#   print "connection failed, invalid token?"




class AnovaBot(AnovaController):
    def __init__(self, slack_token, ANOVA_BLE_ADDRESS, connect=True):
        self.MAC_ADDRESS = ANOVA_BLE_ADDRESS
        self.SLACK_CLIENT_TOKEN = slack_token
        self.is_connected = False
        if connect:
            self.connect()
    def hello(self):
        return 'hello world'

bot = AnovaBot(token, ANOVA_MAC_ADDRESS)
time.sleep(5)
print bot.hello()
bot.set_temp(147.2)
bot.start_anova()


