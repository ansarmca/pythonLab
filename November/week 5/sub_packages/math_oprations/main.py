from basic_operations import arithmetic
from geomatric_operations import area

print("Arithmetic Operations")
print("5 + 3 =",arithmetic.add(5,3))
print("5 - 3 =",arithmetic.subtract(5,3))
print("5 * 3 =",arithmetic.multiply(5,3))
print("5 / 3 =",arithmetic.divide(5,3))
print("5 / 0 =",arithmetic.divide(5,0))


print("Area operations")
print("rectangle area: ",area.rect_area(5,3))
print("circle area: ",area.circle_area(7))
print("traiangle area: ",area.triangle_area(4,5))
