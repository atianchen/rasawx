import slack
from api.settings import *
class slackClient():
    def init(self):
        self.client = slack.WebClient(
            token=CONFIG["token"],
            run_async=True
        )

    def startLisen(self):
        self.rtm_client = slack.RTMClient(token=CONFIG["token"])
        self.rtm_client.start()

    def stopListen(self):
        self.rtm_client.stop();

