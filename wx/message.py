#from xml.etree import ElementTree
from lxml import etree as ElementTree
class WxMsg():

    def __init__(self, msgSource=None):
        if not msgSource is None:
            self.parse(msgSource)
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
    def parse(self, msgSource):
        root = ElementTree.fromstring(msgSource)
        self.content = root.findtext("MsgSource")
        self.toUserName = root.findtext("ToUserName")
        self.fromUserName = root.findtext("FromUserName")
        self.msgId = root.findtext("MsgId")
        self.msgType = root.findtext("MsgType")
        self.createTime = root.findtext("CreateTime")
        self.content = root.findtext("Content")


    def toXML(self):
        root = ElementTree.Element("xml")
        toUserNameNode = ElementTree.SubElement(root,'ToUserName')
        toUserNameNode.text = ElementTree.CDATA(self.toUserName)
        fromUserNameNode = ElementTree.SubElement(root,"FromUserName")
        fromUserNameNode.text = ElementTree.CDATA(self.fromUserName)
        contentNode = ElementTree.SubElement(root,"Content")
        contentNode.text = ElementTree.CDATA(self.content)
        if not self.msgId.isspace():
            msgIdNode = ElementTree.SubElement(root,"MsgId")
            msgIdNode.text = self.msgId
        createTimeNode = ElementTree.SubElement(root,"CreateTime")
        createTimeNode.text = self.createTime
        msgTypeNode = ElementTree.SubElement(root,"MsgType")
        msgTypeNode.text = self.msgType
        return ElementTree.dump(root)


<<<<<<< HEAD


    def toXml(self) -> str:
        return None


=======
>>>>>>> 4eaab027c8d49f01f8e36d123d5eb7a52e094218
    def __str__(self):
        return "%s %s %s " % (self.msgId, self.msgType,self.fromUserName)

