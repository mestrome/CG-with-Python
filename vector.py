import math

class Vector3d:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def sum(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def rotate(self, angle):
        if abs(angle.x) > 0:
            self.y = (self.y * math.cos((angle.x/180)*math.pi)) - (self.z * math.sin((angle.x/180)*math.pi))
            self.z = (self.y * math.sin((angle.x/180)*math.pi)) + (self.z * math.cos((angle.x/180)*math.pi))
        if abs(angle.y) > 0:
            self.x = (self.x * math.cos((angle.y/180)*math.pi)) - (self.z * math.sin((angle.y/180)*math.pi))
            self.z = (self.z * math.sin((angle.y/180)*math.pi)) + (self.z * math.cos((angle.y/180)*math.pi))
        if abs(angle.z) > 0:
            self.x = (self.x * math.cos((angle.z/180)*math.pi)) - (self.y * math.sin((angle.z/180)*math.pi))
            self.y = (self.x * math.sin((angle.z/180)*math.pi)) + (self.y * math.cos((angle.z/180)*math.pi))

    def get(self):
        return (self.x, self.y, self.z)
