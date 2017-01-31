from slackclient import SlackClient
import os
import time
import json
from pycirculate.anova import AnovaController
import datetime

with open ("keys.txt") as f:
    keys = f.read().splitlines()

token = keys[0]
ANOVA_MAC_ADDRESS = keys[1]


class AnovaBot(AnovaController):
    annova_states = ['']
    slack_client_states
    def __init__(self, slack_token, ANOVA_BLE_ADDRESS, connect=True):
        self.MAC_ADDRESS = ANOVA_BLE_ADDRESS
        self.SLACK_CLIENT_TOKEN = slack_token
        self.is_connected = False
        if connect:
            self.connect()
            print "connect to Anova"
        sc = SlackClient(SLACK_CLIENT_TOKEN)

    def hello(self):
        return 'hello world'
    
    def start(self):
        while True:
            response = sc.rtm_read()
            for message_type in response:
                if message_type.get('text'):
                    


if __name__ == "__main__":

    bot = AnovaBot(token, ANOVA_MAC_ADDRESS)
    bot.start()



