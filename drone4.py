#Drone moving to random position but random starting and ending point
import matplotlib.pyplot as plt
import numpy as np

class Drone:
    def __init__(self, grid_size, obstacles, starting_point, ending_point):
        self.grid_size = grid_size
        self.grid = np.zeros((grid_size, grid_size))
        for obstacle in obstacles:
            self.grid[obstacle[0], obstacle[1]] = 1
        self.starting_point = starting_point
        self.ending_point = ending_point
        self.grid[starting_point[0], starting_point[1]] = 2  # Represent starting point with a different value
        self.grid[ending_point[0], ending_point[1]] = 3  # Represent ending point with a different value
        self.x = starting_point[0]
        self.y = starting_point[1]
        self.crashed = False
        self.reached_end = False
    
    def move(self, dx, dy):
        if self.reached_end or self.crashed:
            return
        
        new_x = self.x + dx
        new_y = self.y + dy
        
        if self.is_valid_move(new_x, new_y):
            self.grid[self.x, self.y] = 0  # Clear the current position
            self.x = new_x
            self.y = new_y
            self.grid[self.x, self.y] = 2  # Mark the new position of the drone
            if (self.x, self.y) == self.ending_point:
                self.reached_end = True
        else:
            self.crashed = True
    
    def is_valid_move(self, x, y):
        return 0 <= x < self.grid_size and 0 <= y < self.grid_size and self.grid[x, y] != 1
    
    def plot(self):
        plt.clf()
        plt.imshow(self.grid, cmap='RdYlGn', origin='lower')
        plt.title('Surveillance Drone')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.xticks(np.arange(0, self.grid_size, 1))
        plt.yticks(np.arange(0, self.grid_size, 1))
        plt.grid(color='w', linestyle='-', linewidth=1)
        plt.scatter(self.y, self.x, color='b', label='Drone')
        plt.scatter(self.starting_point[1], self.starting_point[0], color='g', marker='o', s=200, label='Starting Point')  # Plot starting point
        plt.scatter(self.ending_point[1], self.ending_point[0], color='r', marker='*', s=200, label='Ending Point')  # Plot ending point
        plt.legend(loc='upper right')
        plt.draw()
        plt.pause(0.001)

def on_key(event):
    global drone
    if event.key == 'up':
        drone.move(-1, 0)
    elif event.key == 'down':
        drone.move(1, 0)
    elif event.key == 'left':
        drone.move(0, -1)
    elif event.key == 'right':
        drone.move(0, 1)
    
    if drone.crashed:
        print("CRASHED")
    elif drone.reached_end:
        print("CONGRATULATIONS")
    drone.plot()

# Define grid size and obstacles
grid_size = 10
obstacles = [(2, 3), (4, 5), (6, 7)]

# Generate random starting and ending points
starting_point = (np.random.randint(0, grid_size), np.random.randint(0, grid_size))
ending_point = (np.random.randint(0, grid_size), np.random.randint(0, grid_size))

# Ensure starting and ending points are not obstacles
while starting_point in obstacles or ending_point in obstacles:
    starting_point = (np.random.randint(0, grid_size), np.random.randint(0, grid_size))
    ending_point = (np.random.randint(0, grid_size), np.random.randint(0, grid_size))

# Create drone object
drone = Drone(grid_size, obstacles, starting_point, ending_point)

# Plot initial state
drone.plot()

# Connect keyboard event
plt.gcf().canvas.mpl_connect('key_press_event', on_key)

plt.show()
