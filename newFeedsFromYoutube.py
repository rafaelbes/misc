import xml.etree.ElementTree as ET, sys

if len(sys.argv) < 3:
    print 'Usage: python newFeedsFromYoutube.py readerFile.opml youtubeFile.opml'
    print 'This program writes on output.opml entries from youtubeFile.opml that arent in readerFile.opml'
    exit(-1)

treeReader = ET.parse(sys.argv[1])
treeYoutube = ET.parse(sys.argv[2])

rootReader = treeReader.getroot()
rootYoutube = treeYoutube.getroot()
rootOutput = ET.Element("opml", version="1.1")
bodyOutput = ET.SubElement(rootOutput, "body")

outlinesReader = []
outlinesYoutube = []

def processNode(node, outlines):
    if 'xmlUrl' in node.attrib:
        outlines.append(node.attrib)
    for n in node:
        processNode(n, outlines)

processNode(rootReader, outlinesReader)
processNode(rootYoutube, outlinesYoutube)

for i in outlinesYoutube:
    check = False
    for j in outlinesReader:
        if i['xmlUrl'] == j['xmlUrl']:
            check = True
            break
    if not check:
        #print i
        ET.SubElement(bodyOutput, "outline", i)

treeOutput = ET.ElementTree(rootOutput)
treeOutput.write('output.opml')
