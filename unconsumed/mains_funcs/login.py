# from unconsumed.connecting_funcs import signin
# from unconsumed.DTO import users as user
#
#
# def login(myUser, isSignin):
#     #to serve SQL
#     if isSignin == True:
#         signin.signin(myUser)
#     else:
#         signin.login(myUser)
#
#
# print(23)
# t = login(user.users("Ysrael", "y123"), False)
# t = t + "...."
# print()
# ###לא מציג את המשתמש למרות שהוא קיים במערכת לבדוק את זה!!!
import matplotlib.pyplot as plt

# FOV vertices coordinates
fov_vertices = [
    (2.5477916398634166, 4.300823263832089),
    (2.5477916398634166, -4.300823263832089),
    (19.23234193618235, -11.816414802443791),
    (19.23234193618235, 11.816414802443791)
]

# Close the trapezoid by repeating the first point
vertices = fov_vertices + [fov_vertices[0]]

# Extract x and y coordinates
x_coords = [v[0] for v in vertices]
y_coords = [v[1] for v in vertices]

# Create a plot
plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, 'o-', label='FOV Vertices')
plt.fill(x_coords, y_coords, alpha=0.3, label='FOV Area')

# Annotate vertices
for i, (x, y) in enumerate(fov_vertices):
    plt.text(x, y, f'({x:.2f}, {y:.2f})', fontsize=9, ha='right')

# Display plot
plt.xlabel('X-coordinate (m)')
plt.ylabel('Y-coordinate (m)')
plt.title('Field of View (FOV) Vertices')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
