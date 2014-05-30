import time 
import colorsys
import random

hue = hyperion.args.get('hue',  random.random())
increment = hyperion.args.get('increment', 0.618033988749895)
sleepTime =  hyperion.args.get('time', 5.0)

# Start the write data loop
while not hyperion.abort():
	hue = (hue + increment) %1
	color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
	colorLedsData = bytearray(hyperion.ledCount * (int(255*color[0]), int(255 * color[1]), int(255*color[2])))
	hyperion.setColor(colorLedsData)
	time.sleep(sleepTime)
