doc = """<com>
        <time>00-01-01 04:23:25</time>
        <log>2442</log>
        <channels>
                <ch1 pow="0.1">0.8</ch1>
                <ch2 pow="0.0">0.3</ch2>
                <ch3 pow="0.0">0.1</ch3>
                <ch4 pow="0.0">0.2</ch4>
        </channels>
</com>"""

doc2 =      """
                <channel_set name='gate_[00:13:a2:00:40:31:56:96]!.activate' value='On'/> 
            """



doc3 = """<?xml version="1.0" ?>
<zAppointments reminder="15">
    <appointment>
        <begin>1181251680</begin>        
        <uid>040000008200E000</uid>
        <alarmTime>1181572063</alarmTime>
        <state></state>
        <location></location>
        <duration>1800</duration>
        <subject>Bring pizza home</subject>
    </appointment>
</zAppointments>"""


import xml.dom.minidom



doc = xml.dom.minidom.parseString(doc2)
#nodes = doc.documentElement.childNodes
nodes = doc.getElementsByTagName("channel_set")
print len(nodes)       
#if node.nodeType == xml.dom.Node.ELEMENT_NODE:
#print 'Element name: %s' % node.nodeName
for node in nodes:
    print node.toxml()
    test = node.toxml()
    
    try:
        for (name, value) in node.attributes.items():
            print '    Attr -- Name: %s  Value: %s ' % (name, value)
            #if name == 'reminder':
             #   self.rem_value = value
    except:
        continue



def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


def handleXML(xml):
    #print "<html>"
    #print "time is"
    #handleTime(xml.getElementsByTagName("time")[0])
    #print "log number is"
    #handleLog(xml.getElementsByTagName("log")[0])
    data = xml.getElementsByTagName("data")[0]
    list = data.childNodes
    for i in list:
        print i
        print i.data
        #new = i.attributes()
        #for n in new:
            #print n
        #handleCh(xml.getElementsByTagName(chan)[0], chan)
        
    
    #handleChannels(channels)
    #handleSlides(slides)
    #print "</html>"


def handleCh(channel, name):
    print channel.attributes["pow"].value
    print getText(channel.childNodes)

def handleLog(log):
    print getText(log.childNodes)

def handleTime(time):
    print getText(time.childNodes)





#handleXML(dom)