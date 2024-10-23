area_of_square = lambda side: side * side

area_of_rectangle = lambda length, breadth: length * breadth

area_of_triangle = lambda base, height: 0.5 * base * height

side_of_square = float(input("Enter the side of the square: "))

length_of_rectangle = float(input("Enter the length of the rectangle: "))
breadth_of_rectangle = float(input("Enter the breadth of the rectangle: "))

base_of_triangle = float(input("Enter the base of the triangle: "))
height_of_triangle = float(input("Enter the height of the triangle: "))

square_area = area_of_square(side_of_square)
rectangle_area = area_of_rectangle(length_of_rectangle, breadth_of_rectangle)
triangle_area = area_of_triangle(base_of_triangle, height_of_triangle)

print("Area of square:", square_area)
print("Area of rectangle:", rectangle_area)
print("Area of triangle:", triangle_area)
