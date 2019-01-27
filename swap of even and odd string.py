s =input()
t = list(s)
print(t)
t[::2], t[1::2] = t[1::2], t[::2]
print(''.join(t))
#player.da
