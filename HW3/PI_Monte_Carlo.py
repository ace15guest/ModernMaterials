"""
The relationship b/w A of a sphere inscribed inside a square is A_circ=πr^2 and
A_square=(2r)^2 Assuming we don't know pi we can write A_circ = cr^2. Taking
the ratio of these to gives A_circle_to_square = c/4. Say we blindly throw darts
at the area inscribed by the square (which contains the circle) We will have some
that are inside the circle but all must be inside the square.
So c/4 = pts_in_cirle/pts_in_square.We can extend this to larger dimensions by
taking the ratios of volumes or take it down one dimension by using the ratio
of perimeters to calculate pi.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

pi = []
x_random_sample = []
y_random_sample = []
sample_runs = np.arange(1 , 7, .5)
for r in sample_runs:
    # Number of random samples we will take
    samples = int(10**r)
    # All points will be inside the square, so it will just equal the sample size
    pts_in_square = samples
    # Create a set of random (x,y) points that will fall onto the plot
    x_random_sample = np.random.uniform(-1, 1, size=samples)
    y_random_sample = np.random.uniform(-1, 1, size=samples)
    # Distance from the center of the plot
    dist_from_center = np.sqrt(x_random_sample ** 2 + y_random_sample ** 2)
    # Counting the points that are inside the circle with radius one only
    pts_in_circle = len([i for i in dist_from_center if i <= 1])
    # Using the ratio from the initial notes we can calculate pi
    pi.append(4*pts_in_circle/pts_in_square)

fig, ax = plt.subplots()
fig1, ax1 = plt.subplots()
# Plotting square l=2 and circle r=1
rect = patches.Rectangle((-1, -1), 2, 2, linewidth=1, edgecolor='r', facecolor='none')
circle1 = plt.Circle((0, 0), 1, color='r', alpha=.2)
ax.scatter(x_random_sample, y_random_sample)
ax.add_patch(rect)
ax.add_patch(circle1)
# Show the randomly sampled points

ax1.set(xlabel='Sample Size (#)', ylabel='Error $(\pi - \pi_{MonteCarlo})$', title="Monte Carlo Estimation Error | Best Run: " + str(pi[-1]))
ax.set(xlabel='[L]', ylabel='[L]', title="Circle (r=1), Square($\ell=1$), Random Points (x,y)")
ax1.plot(10**sample_runs, np.pi - np.asarray(pi))
# Set limits
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

plt.show()



# for i in range(samples):
#
#     # Randomly generated x and y values from a
#     # uniform distribution
#     # Range of x and y values is -1 to 1
#     rand_x = random.uniform(-1, 1)
#     rand_y = random.uniform(-1, 1)
#
#     # Distance between (x, y) from the origin
#     origin_dist = rand_x ** 2 + rand_y ** 2
#     ax.scatter(rand_x, rand_y, color='black')
#
#     # Checking if (x, y) lies inside the circle
#     if origin_dist <= 1:
#         circle_points += 1
#
#     square_points += 1
#
#     # Estimating value of pi,
#     # pi= 4*(no. of points generated inside the
#     # circle)/ (no. of points generated inside the square)
# pi = 4 * circle_points / square_points



##    print(rand_x, rand_y, circle_points, square_points, "-", pi)
# print("\n")
