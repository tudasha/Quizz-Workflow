"""FSG 2023 quiz, problem 616: camera pixel + distance -> point in the vehicle frame.

Givens (question text):
    vehicle frame: right-handed, x forward, z up (so y points left)
    camera position t = (500, 160, 1140) mm in the vehicle frame
    camera orientation, Euler ZY'X'' (intrinsic): roll = 100 deg, pitch = 0 deg,
        yaw = 90 deg  ->  R = Rz(yaw) * Ry(pitch) * Rx(roll)
    no distortion; cx = 636 px, cy = 548 px, fx = 241 px, fy = 238 px
    pixel origin (u, v) = (0, 0) lies at (-cx, -cy) from the principal point,
        so image coordinates relative to the principal point are u - cx, v - cy
    detected pixel u = 795 px, v = 467 px
    Euclidean distance camera origin -> object d = 2.7 m
Camera frame (figure 616_2, pinhole model): z_c along the viewing direction,
x_c along u (right in the image), y_c along v (down in the image).
Assumption: R is the camera pose, i.e. it maps camera coordinates into the
vehicle frame: p_vehicle = t + R p_camera (standard pose convention).
Asked: x, y, z of the object in the vehicle frame in m, three decimals.
"""
import math
from decimal import Decimal, ROUND_HALF_UP

MM_TO_M = 1e-3

camera_position = [500 * MM_TO_M, 160 * MM_TO_M, 1140 * MM_TO_M]  # m
roll = math.radians(100.0)
pitch = math.radians(0.0)
yaw = math.radians(90.0)

principal_u, principal_v = 636.0, 548.0  # px
focal_u, focal_v = 241.0, 238.0          # px
pixel_u, pixel_v = 795.0, 467.0          # px
distance = 2.7                           # m, Euclidean, camera origin to object


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def rot_x(angle):
    c, s = math.cos(angle), math.sin(angle)
    return [[1, 0, 0], [0, c, -s], [0, s, c]]


def rot_y(angle):
    c, s = math.cos(angle), math.sin(angle)
    return [[c, 0, s], [0, 1, 0], [-s, 0, c]]


def rot_z(angle):
    c, s = math.cos(angle), math.sin(angle)
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]


# Intrinsic Z, then Y', then X'' composes left to right.
rotation = matmul(matmul(rot_z(yaw), rot_y(pitch)), rot_x(roll))
for name, col in zip("xyz", range(3)):
    axis = [rotation[row][col] for row in range(3)]
    print(f"camera {name}-axis in vehicle frame: ({axis[0]:+.4f}, {axis[1]:+.4f}, {axis[2]:+.4f})")

# Back-project the pixel to a viewing ray on the normalised image plane z_c = 1.
ray = [(pixel_u - principal_u) / focal_u, (pixel_v - principal_v) / focal_v, 1.0]
# The sensor gives the Euclidean distance (along the ray), not the depth z_c,
# so scale the unit ray, not the z = 1 ray.
ray_length = math.sqrt(sum(component**2 for component in ray))
point_camera = [distance * component / ray_length for component in ray]
print("object in camera frame [m]:", [f"{c:.6f}" for c in point_camera])

point_vehicle = [
    camera_position[row] + sum(rotation[row][k] * point_camera[k] for k in range(3))
    for row in range(3)
]
print("object in vehicle frame [m]:", [f"{c:.6f}" for c in point_vehicle])

rounded = [
    str(Decimal(repr(c)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP))
    for c in point_vehicle
]
print(", ".join(rounded))
