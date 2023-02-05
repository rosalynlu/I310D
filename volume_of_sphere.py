def calculate_volume_of_sphere(radius):
	pi = 3.14
	area = (4.0 / 3.0) * pi * pow(radius, 3)
	return area

radius1 = 30
vol1 = calculate_volume_of_sphere(radius1)
print(f"The volume of sphere with radius {radius1} is: {vol1}")

radius2 = 40
vol2 = calculate_volume_of_sphere(radius2)
print(f"The volume of sphere with radius {radius2} is: {vol2}")
