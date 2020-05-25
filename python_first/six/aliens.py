aliens = []

for alien_number in range(30):
    new_alien = { 'color': 'green', 'point': 5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15
# 显示前五个外星人
for alien in    aliens[0:5]:
    print(alien)
print('...')