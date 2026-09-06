import numpy as np

def Vector2D_rotation(v,theta):
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])

    return np.dot(rotation_matrix,v)


print("Algorithm to find final location of end-effector from a two joints robotic arm.")

# For any length of the two links, use this line
#v = np.asarray(input("Enter the lengths of the two links (Ex: 2,3):").split(','),dtype=float)
l = np.asarray([20, 15],dtype=float)

theta = np.asarray(input("Enter the angles of the two joints in degrees (Ex: 30,45):").split(','),dtype=float)
theta = np.radians(theta)

#First link rotation
v1 = np.asarray([l[0],0])
v1_final = Vector2D_rotation(v1,theta[0])

#Second link rotation
v2 = np.asarray([l[1],0])
v2_rotation = Vector2D_rotation(v2,theta[0]+theta[1])

#End-effector final location
v = v1_final + v2_rotation

print(f"Final location of end-effector: ({v[0]:.1f}, {v[1]:.1f})")
