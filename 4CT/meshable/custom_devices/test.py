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


import xml.dom.minidom



dom = xml.dom.minidom.parseString(doc)

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


def handleXML(xml):
    #print "<html>"
    print "time is"
    handleTime(xml.getElementsByTagName("time")[0])
    print "log number is"
    handleLog(xml.getElementsByTagName("log")[0])
    for i in range(1, 5):
        chan = "ch" + str(i)
        print chan +" value is:"
        handleCh(xml.getElementsByTagName(chan)[0], chan)
    
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





handleXML(dom)