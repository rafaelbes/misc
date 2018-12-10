import urllib2, base64, datetime, time
request = urllib2.Request("http://192.168.100.1/cgi-bin/status_cgi")
base64string = base64.b64encode('%s:%s' % ('admin', 'password'))
request.add_header('Authorization', 'Basic %s' % base64string)


for j in range(60):
    arq = open('relatorio.csv', 'a')
    intervalo = 3
    for i in range(int(60.0/intervalo)):
        time.sleep(intervalo)
        agora = datetime.datetime.now()
        s = urllib2.urlopen(request).read()
        c1 = s.find('Upstream 1')
        c2 = s.find('Upstream 3')
        c3 = s.find('Upstream 4')
        p1 = s[47+c1:c1+52]
        p2 = s[47+c2:c2+52]
        p3 = s[47+c3:c3+52]
        m1 = s[112+c1:c1+117]
        m2 = s[112+c2:c2+117]
        m3 = s[112+c3:c3+117]
        hora = str(agora.hour) + ':' + str(agora.minute) + ':' + str(agora.second)
        print hora, m1, p1, m2, p2, m3, p3
        arq.write(hora)
        arq.write(',' + m1 + ',' + p1)
        arq.write(',' + m2 + ',' + p2)
        arq.write(',' + m3 + ',' + p3 + '\n')
    print 'gravando no arquivo'
    arq.close()
