#esse programa altera o ultimo keyframe de todas os efeitos de transformacoes que contiverem exatamente
#3 keyframes pelo primeiro keyframe da transformacao seguinte. A ideia de usar 3 keyframes eh que o primeiro
#represente a transformacao do clip atual e os dois seguintes para fazer a animacao da transicao. O problema
#eh que pela interface do kdenlive nao consigo uma maneira facil de copiar os parametros do primeiro keyframe
#da transformacao seguinte. Com esse programa agora tudo ficou mais simples e rapido!
import sys

f = open(sys.argv[1])

lines = []
rectLineIdx = []
rects = []

i = 0
for line in f:
	lines.append(line)
#	print(i, end='')
	if 'rect' in line:
		pattern1 = "rect\">"
		pattern2 = "</prop"
		idx0 = line.find(pattern1)+len(pattern1)
		idx1 = line.find(pattern2)
		trecho = line[idx0:idx1]
		rects.append(trecho.split(';'))
		rectLineIdx.append(i)
	i += 1

for j in range(i):
	if j in rectLineIdx:
		idx = rectLineIdx.index(j)
		r = rects[idx]
		if len(r) == 3:
			s = rects[idx+1]
			print('<property name="rect">', end='')
			for k in range(2):
				print(r[k] + ';', end='')
			print(r[2].split('=')[0] + '=' + s[0].split('=')[1], end='')
			print('</property>')
		else:
			print(lines[j])
	else:
		print(lines[j], end='')

f.close()
