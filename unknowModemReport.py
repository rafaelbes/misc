import urllib2, base64, datetime, time
request = urllib2.Request("http://192.168.100.1/cgi-bin/status_cgi")
base64string = base64.b64encode('%s:%s' % ('admin', 'password'))
request.add_header('Authorization', 'Basic %s' % base64string)

s = urllib2.urlopen(request).read()

if False:
    for j in range(60):
        arq = open('relatorio.csv', 'a')
        intervalo = 0.2
        for i in range(int(60.0/intervalo)):
            time.sleep(intervalo)
            agora = datetime.datetime.now()
            s = urllib2.urlopen(request).read()
            x = s.find('dBmV', 4160)
            y = s.find('Modulation', 4100)
            sy = y+23
            end = s[sy:].find('</td>')
            power = float(s[x-5:x])
            mod = s[sy:sy+end]
            hora = str(agora.hour) + ':' + str(agora.minute) + ':' + str(agora.second)
            print hora, mod, power
            arq.write(hora + ',' + mod + ',' + str(power) +'\n')
        print 'gravando no arquivo'
        arq.close()
