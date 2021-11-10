"""
password : acs662week4
paraview

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs


# given value
f = np.loadtxt('coord.out', skiprows=1, dtype='float')
x = f[:, 4]
xp = f[:, 5]
alpha_x = 0.399
beta_x = 0.0109


# calculate
large_x = x / beta_x**(1/2)
large_xp = (alpha_x * x + beta_x * xp) / beta_x**(1/2)

bins = 128
hist_xxp = np.histogram2d(x, xp, bins=bins)
hist_lxxp = np.histogram2d(large_x, large_xp, bins=bins)


# prob1 plot
prob1 = plt.figure(figsize=(10, 8))
grid = gs.GridSpec(2, 2, height_ratios=[1, 3], width_ratios=[3, 1])

hist_x = plt.subplot(grid[0])
hist_x.hist(x, bins=bins)

hist_y = plt.subplot(grid[3])
hist_y.hist(xp, bins=bins, orientation='horizontal')

contour_xy = plt.subplot(grid[2])
contour_xy.contourf(hist_xxp[1][:bins], hist_xxp[2][:bins], hist_xxp[0],
                    levels=np.linspace(0, 25, bins), cmap='jet')

plt.tight_layout()
plt.show()


# prob2 plot
prob2 = plt.figure(figsize=(10, 8))

# scatter
scatter1 = plt.subplot(2, 2, 1)
plt.scatter(x, xp, s=1)
plt.title("(x,x')")
plt.xlabel("x")
plt.ylabel("x'")

scatter2 = plt.subplot(2, 2, 2)
plt.scatter(large_x, large_xp, s=1)
plt.title("(X,X')")
plt.xlabel("X")
plt.ylabel("X'")


# density
density1 = plt.subplot(2, 2, 3)
plt.contourf(hist_xxp[1][:bins], hist_xxp[2][:bins], hist_xxp[0],
             levels=np.linspace(0, 25, bins), cmap='jet')
plt.title("(x,x')")
plt.xlabel("x")
plt.ylabel("x'")

density2 = plt.subplot(2, 2, 4)
plt.contourf(hist_lxxp[1][:bins], hist_lxxp[2][:bins], hist_lxxp[0],
             levels=np.linspace(0, 25, bins), cmap='jet')
plt.title("(X,X')")
plt.xlabel("X")
plt.ylabel("X'")


plt.tight_layout()
plt.show()
