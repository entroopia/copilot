import matplotlib.pyplot as plt
import numpy as np

def draw_star_in_circle(radius=1, star_points=5):
    fig, ax = plt.subplots(figsize=(6, 6))
    # Draw the circle
    circle = plt.Circle((0, 0), radius, fill=False, color='black', linewidth=2)
    ax.add_artist(circle)

    if star_points == 6:
        # Draw two overlapping equilateral triangles (hexagram)
        angles1 = np.linspace(np.pi/2, np.pi/2 + 2 * np.pi, 3, endpoint=False)
        triangle1 = np.stack((radius * np.cos(angles1), radius * np.sin(angles1)), axis=1)
        angles2 = np.linspace(np.pi/2 + np.pi/6, np.pi/2 + np.pi/6 + 2 * np.pi, 3, endpoint=False)
        triangle2 = np.stack((radius * np.cos(angles2), radius * np.sin(angles2)), axis=1)
        # Close the triangles
        triangle1 = np.vstack([triangle1, triangle1[0]])
        triangle2 = np.vstack([triangle2, triangle2[0]])
        ax.plot(triangle1[:, 0], triangle1[:, 1], color='red', linewidth=2)
        ax.plot(triangle2[:, 0], triangle2[:, 1], color='red', linewidth=2)
    else:
        # Calculate star points for odd-pointed stars
        angles = np.linspace(0, 2 * np.pi, star_points, endpoint=False)
        points = np.stack((radius * np.cos(angles), radius * np.sin(angles)), axis=1)
        skip = star_points // 2
        star_indices = [(i * skip) % star_points for i in range(star_points + 1)]
        star_points_xy = points[star_indices]
        ax.plot(star_points_xy[:, 0], star_points_xy[:, 1], color='red', linewidth=2)

    # Set aspect and limits
    ax.set_aspect('equal')
    ax.set_xlim(-radius * 1.1, radius * 1.1)
    ax.set_ylim(-radius * 1.1, radius * 1.1)
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
        draw_star_in_circle(radius=1, star_points=6) # kommentaar
