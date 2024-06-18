class Camera:
    def __init__(self, id_camera, name_camera, vertical_angle, horizontal_angle, maximum_distance):
        self.id_camera = id_camera
        self.name_camera = name_camera
        self.vertical_angle = vertical_angle
        self.horizontal_angle = horizontal_angle
        self.maximum_distance = maximum_distance

    def __str__(self):
        return f"Camera(ID: {self.id_camera}, Name: {self.name_camera}, Vertical Angle: {self.vertical_angle}, Horizontal Angle: {self.horizontal_angle}, Max Distance: {self.maximum_distance})"
