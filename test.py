from util import get_limits


yellow = [0, 255, 255]  # yellow in BGR colorspace
colors = [(0, 255, 255)]
colors = [get_limits(i) for i in colors]
print(colors)