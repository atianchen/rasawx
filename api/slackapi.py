import slack
from api.settings import *

class SlackApi():
    def init(self):
        self.client = slack.WebClient(
            token=CONFIG["token"],
            run_async=True
        )

    def send(self,msg):
        return self.client.chat_postMessage(
            channel=msg.channel,
            text=msg.content
        )

    @slack.RTMClient.run_on(event='message')
    def say_hello(**payload):
        data = payload['data']
        web_client = payload['web_client']
        rtm_client = payload['rtm_client']
        if 'Hello' in data['text']:
            channel_id = data['channel']
            thread_ts = data['ts']
            user = data['user']
            web_client.chat_postMessage(
                channel=channel_id,
                text=f"Hi <@{user}>!",
                thread_ts=thread_ts
            )

    def startLisen(self,callback):
        self.rtm_client = slack.RTMClient(token=CONFIG["token"])
        self.rtm_client.start()

    def stopListen(self):
        if getattr(self, "rtm_client", None) is not None:
            self.rtm_client.stop()
            self.rtm_client = None

