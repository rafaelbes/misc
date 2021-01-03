import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
import sys

Fs, data = read('output.wav')
data = np.array(data[:,0])
y = []
d = []
n = len(data)
#print(n)

freq = 32000
delta = freq*1
t = 0
for i in range(0, n, delta):
	m = np.max(np.abs(data[i:i+delta]))
	if m < 5000:
		d.append(t)
	t += 1
	y.append(m)

ss = 0
e = []
qtd = 0
for k in range(len(d)):
	if d[k] - ss != 0:
		e.append((ss, d[k]-ss))
#		print(f'ffmpeg -i input.mp4 -vf trim={ss}:{d[k]-1} -acodec copy -vcodec copy output{qtd}.avi')
		print(f'ffmpeg -i input.avi -ss {ss} -to {d[k]} -acodec copy -vcodec copy output{qtd}.avi')
		qtd += 1
	ss = d[k]+1
	if k > 50:
		break

#print(d)
#print(e)
#plt.plot(d)
#plt.show()
