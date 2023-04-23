import matplotlib.pyplot as plt

# Load data from txt file
data = []
with open('HW3.txt') as file:
    for line in file:
        line = line.strip().split()
        mass, height = float(line[0]), float(line[1])
        data.append((mass, height))

# Extract mass and height from data
masses, heights = zip(*data)

# Create a scatter plot
plt.scatter(masses, heights)

# Set plot title and axis labels
plt.title('Mass-Height Scatter Plot')
plt.xlabel('Mass (kg)')
plt.ylabel('Height (cm)')

# Save plot to file
plt.savefig('HW3.png')