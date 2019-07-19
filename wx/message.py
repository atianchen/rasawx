from xml.etree import ElementTree
class WxMsg():

    def __init__(self, msgSource):
        self.analyze(msgSource)
    #解析微信内容
    """<xml>
      <ToUserName><![CDATA[toUser]]></ToUserName>
      <FromUserName><![CDATA[fromUser]]></FromUserName>
      <CreateTime>1348831860</CreateTime>
      <MsgType><![CDATA[text]]></MsgType>
      <Content><![CDATA[this is a test]]></Content>
      <MsgId>1234567890123456</MsgId>
    </xml>
    """
    def analyze(self, msgSource):
        root = ElementTree.fromstring(msgSource)
        self.content = root.findtext("MsgSource")
        self.toUserName = root.findtext("ToUserName")
        self.fromUserName = root.findtext("FromUserName")
        self.msgId = root.findtext("MsgId")
        self.msgType = root.findtext("MsgType")
        self.createTime = root.findtext("CreateTime")
        self.content = root.findtext("Content")

    def toXml(self) -> str:
        return None

    def __str__(self):
        return "%s %s %s " % (self.msgId, self.msgType,self.fromUserName)