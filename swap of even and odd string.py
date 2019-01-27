s =input()
t = list(s)
t[::2], t[1::2] = t[1::2], t[::2]
print(''.join(t))
#player.da
