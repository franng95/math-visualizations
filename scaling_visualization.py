import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Original O1 vertices
original = np.array([
    [0, 0, 0],
    [5, 3, 31],
    [8, 0, 64],
    [0, 0, 0]  # Close the triangle
])

# Scaled O1 vertices
scaled = np.array([
    [0, 0, 0],
    [20, 9, 31],
    [32, 0, 64],
    [0, 0, 0]  # Close the triangle
])

# Create figure with two subplots side by side
fig = plt.figure(figsize=(14, 6))

# ---- LEFT PLOT: Original O1 ----
ax1 = fig.add_subplot(121, projection='3d')

# Plot the triangle
ax1.plot(original[:, 0], original[:, 1], original[:, 2], 
         'b-o', linewidth=2, markersize=8, label='Original O₁')

# Label vertices
ax1.text(0, 0, 0, '  A(0,0,0)', fontsize=10)
ax1.text(5, 3, 31, '  B(5,3,31)', fontsize=10)
ax1.text(8, 0, 64, '  C(8,0,64)', fontsize=10)

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Original O₁', fontsize=14, fontweight='bold')
ax1.legend()
ax1.grid(True)

# ---- RIGHT PLOT: Scaled O1 ----
ax2 = fig.add_subplot(122, projection='3d')

# Plot the scaled triangle
ax2.plot(scaled[:, 0], scaled[:, 1], scaled[:, 2], 
         'r-s', linewidth=2, markersize=8, label='Scaled O₁ (4x, 3y)')

# Label vertices
ax2.text(0, 0, 0, "  A'(0,0,0)", fontsize=10)
ax2.text(20, 9, 31, "  B'(20,9,31)", fontsize=10)
ax2.text(32, 0, 64, "  C'(32,0,64)", fontsize=10)

ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Scaled O₁ (4× in x, 3× in y)', fontsize=14, fontweight='bold')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('scaling_O1.png', dpi=300, bbox_inches='tight')
print("✅ Scaling visualization saved as 'scaling_O1.png'")
plt.show()