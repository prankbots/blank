# -*- coding: utf-8 -*-
#Official BLACK OF GAMER
#CODING FROM PRANKBOTS
import PRANKBOTS
from PRANKBOTS.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,sys
import re,string,os
import os.path,sys,urllib,shutil,subprocess
PB = PRANKBOTS.LINE()
#===BUAT MASUKIN TOKEN DI TENGAH TENGAH TANDA KUTIP===#
PB.login(token="masukan toket disini")
#======================#
PB.loginResult()
print u"\n\nCREATOR:::ACIL\nULAH POHO DI SUBCRABE CHANNEL NA DAEK MAKE HUNGKUL RUJIITT\n\nPRANKBOT NGGES LOGINA GEURA DI PAKE ULAH BENGAL JANG"
reload(sys)
sys.setdefaultencoding('utf-8')
KAC=[PB]
mid = PB.getProfile().mid
Bots = [mid]
wait = {
    'autoAdd':True,
    'timeline':True,
    'message':"thanks thanks",
}
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 26:
            msg = op.message
        if op.type == 5:
            if wait["autoAdd"] == True:
                c = Message(to=op.param1, from_=None, text=None, contentType=13)
                c.contentMetadata = {'mid': "PRANKBOTS','"}
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    PB.sendText(op.param1,str(wait["message"]))
                    PB.sendMessage(c)
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "INI URL TIMELINE NYA\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "LINK TIMELINE NYA INI OM\n" + msg.contentMetadata["postEndUrl"]
                    PB.sendText(msg.to,msg.text)
        if op.type == 59:
            print op
    except Exception as error:
        print error
while True:
    try:
        Ops = PB.fetchOps(PB.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(PB.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            PB.Poll.rev = max(PB.Poll.rev, Op.revision)
            bot(Op)
