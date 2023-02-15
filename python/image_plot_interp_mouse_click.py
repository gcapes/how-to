import numpy as np
import matplotlib.pyplot as plt
import scipy
from mpl_point_clicker import clicker

def profile_from_coords(x0, y0, x1, y1, num_points, data):
    x = np.arange(data.shape[1])
    y = np.arange(data.shape[0])
    xvalues = np.linspace(x0, x1, num_points)
    yvalues = np.linspace(y0, y1, num_points)
    f = scipy.interpolate.RectBivariateSpline(x, y, data)
    profile = f(xvalues, yvalues)
    return profile

# Make some data
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
data = np.sin(R)


# Image plot of the data
fig, ax = plt.subplots()
ax.imshow(data.T, origin="lower", interpolation="nearest")

klicker = clicker(ax, ["event"], markers=["x"], linestyle="--")
plt.show()

# Get coordinates from mouse clicks
coords = klicker.get_positions()['event']
cx0 = coords[0][0]
cy0 = coords[0][1]
cx1 = coords[1][0]
cy1 = coords[1][1]

# Make new plot of the data, with the clicked profile
click_profile = profile_from_coords(cx0, cy1, cx1, cy1, 1000, data)
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.title.set_text("Image data")
ax1.imshow(data.T, origin="lower", interpolation="nearest")
ax1.plot([cx0, cx1], [cy0, cy1], marker="o")

click_diag = np.diag(click_profile)
ax2.title.set_text("Profile")
ax2.set_ylabel("z value")
ax2.set_xlabel("point number")
ax2.plot(np.arange(click_diag.shape[0]), click_diag)
fig.tight_layout()
plt.show()
