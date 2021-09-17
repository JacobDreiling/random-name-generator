from math import asin,pi
import time#,sound

f=lambda x:4*x*(1-x)  #Feigenbaum
g=lambda x:x*x-2      #Mandelbrot

seed=0.49128895947328405

while 1:
	for _ in range(10):seed=g(seed)
	#freq=[.8,1.1][round(.5+math.asin(2*seed-1)/math.pi)]
	#sound.play_effect('digital:Tone1',pitch=freq)
	print(.5+asin(seed/2)/pi)
	time.sleep(1.5)
