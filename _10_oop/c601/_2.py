from _10_oop.c601.unit import Engine, Aircond, Sound

e1 = Engine(1600)
print('1600 cost: ' + str(e1.get_cost()))
e2 = Engine(2000)
print('2000 cost: ' + str(e2.get_cost()))
a1 = Aircond('auto')
print('Auto: ' + str(a1.get_cost()))
a2 = Aircond('manual')
print('Manual: ' + str(a2.get_cost()))
s = Sound()
print('Stereo: ' + str(s.get_cost()))
