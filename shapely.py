from shapely.geometry import Point
from shapely.geometry import Polygon
import imp

# Create Point objects
p1 = Point(24.82, 60.24)
p2 = Point(24.895, 60.05)

# Create a square
coords = [(24.89, 60.06), (24.75, 60.06), (24.75, 60.30), (24.89, 60.30)]
poly = Polygon(coords)

# PIP test with 'within'
p1.within(poly)     # True
p2.within(poly)     # False

# PIP test with 'contains'
poly.contains(p1)   # True
poly.contains(p2)   # False
