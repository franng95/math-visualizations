import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Original O2 vertices (bounding box corners)
original = np.array([
    [0, 0, 0],
    [8, 0, 64],
    [8, 64, 192],
    [0, 64, 128],
    [0, 0, 0]  # Close the box
])

# Rotated O2 vertices (45° about z-axis)
rotated = np.array([
    [0, 0, 0],
    [5.66, 5.66, 64],
    [-39.59, 50.90, 192],
    [-45.25, 45.25, 128],
    [0, 0, 0]  # Close the box
])

# Create figure with two subplots side by side
fig = plt.figure(figsize=(14, 6))

# ---- LEFT PLOT: Original O2 ----
ax1 = fig.add_subplot(121, projection='3d')

# Plot the quadrilateral
ax1.plot(original[:, 0], original[:, 1], original[:, 2], 
         'b-o', linewidth=2, markersize=8, label='Original O₂')

# Label vertices
ax1.text(0, 0, 0, '  P1(0,0,0)', fontsize=9)
ax1.text(8, 0, 64, '  P2(8,0,64)', fontsize=9)
ax1.text(8, 64, 192, '  P3(8,64,192)', fontsize=9)
ax1.text(0, 64, 128, '  P4(0,64,128)', fontsize=9)

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Original O₂', fontsize=14, fontweight='bold')
ax1.legend()
ax1.grid(True)

# ---- RIGHT PLOT: Rotated O2 ----
ax2 = fig.add_subplot(122, projection='3d')

# Plot the rotated quadrilateral
ax2.plot(rotated[:, 0], rotated[:, 1], rotated[:, 2], 
         'r-s', linewidth=2, markersize=8, label='Rotated O₂ (45°)')

# Label vertices
ax2.text(0, 0, 0, "  P1'(0,0,0)", fontsize=9)
ax2.text(5.66, 5.66, 64, "  P2'(5.66,5.66,64)", fontsize=9)
ax2.text(-39.59, 50.90, 192, "  P3'(-39.59,50.90,192)", fontsize=9)
ax2.text(-45.25, 45.25, 128, "  P4'(-45.25,45.25,128)", fontsize=9)

ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Rotated O₂ (45° about z-axis)', fontsize=14, fontweight='bold')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('rotation_O2.png', dpi=300, bbox_inches='tight')
print("✅ Rotation visualization saved as 'rotation_O2.png'")
# plt.show() removed to avoid display errors