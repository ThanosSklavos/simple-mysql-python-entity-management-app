import point as p

# create some points
p1 = p.Point(1, 2)
p2 = p.Point(3, 4)
p3 = p.Point(4, 5)

print("p1:", p1)
print("p2:", p2)
print("p3:", p3)

p4 = p.add_points(p1, p3)
print("p4:", p4)

p5 = p1 + p3
print("p5:", p5)