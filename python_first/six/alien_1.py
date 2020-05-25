alien = {'color': 'green', 'speed': 'fast', 'y_position': 25}
if alien['speed'] is 'slow':
    x_increment = 1
    color = 'yellow'
elif alien['speed'] is 'medium':
    x_increment = 2
    color = 'blue'
elif alien['speed'] is 'fast':
    x_increment = 3
    color = 'black'

alien['x_position'] = 0

alien['x_position'] += x_increment

print("New x-position: " + str(alien['x_position']))
del alien['y_position']
print(alien)