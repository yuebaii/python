import sys
import itchat, time
from itchat.content import *


    
#实现微信消息的接受 然后发送消息！！
@itchat.msg_register([itchat.content.TEXT],isFriendChat=True)
def print_content(msg): 
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    print('他：%s'%msg['Text'].translate(non_bmp_map))
    #print(msg['Text'])
    
    if msg['Type'] == TEXT:
       # strs = input("input:")
        ReplyContent = 'I received picture: '+ msg['Content']
    if msg['Type'] == PICTURE:
        ReplyContent = 'I received picture: '+msg['FileName']
        
    msg['Content'] = input('我:')
    itchat.send_msg(msg['Content'],msg['FromUserName'])
   #return "I reveived: %s" % msg["Text"]

'''
#下载附件消息
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    itchat.send('@%s@%s' % (
        'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
        msg['FromUserName'])
   # return '%s received' % msg['Type']
'''
'''
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])

def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)
'''

'''
# 带参数注册，该类消息类型将调用该方法
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE])
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

'''   
'''
#实现微信消息的发送
itchat.send("hello world!", 'filehelper')
itchat.send("@fil@%s" %'C:/Users/Administrator/Desktop/score1.txt', 'filehelper')
itchat.send("@img@%s" %'C:/Users/Administrator/Desktop/epoll.png', 'filehelper')
time.sleep(20)

itchat.logout()
'''
def lc():
    print("finished login!")
    #查看好友列表
    '''
    lb = itchat.get_friends()
    count = 0
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    for zd in lb:
        count = count + 1
        print(zd['NickName'].translate(non_bmp_map)+':'+zd['Signature'].translate(non_bmp_map),count)
    '''
    
def ec():
    print("exit!")

if __name__ == '__main__':
    itchat.auto_login(hotReload=True,loginCallback=lc, exitCallback=ec)
    
    lb = itchat.search_friends(name='sb')
    count = 0
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    for zd in lb:
        for k,v in zd.items():
            print(k,v)
            
    itchat.run()



