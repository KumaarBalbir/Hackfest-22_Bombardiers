
# for infinitely length of horizontal line from point p, we take maximum value as INT_MAX=10000
INT_MAX = 10000

# onSegment() function:
# Given three collinear points p, q, r,
# the function checks if point q lies
# on line segment 'pr'
# x and y projection of pq and qr intersect then q lies on line segment pr
# otherwise not


def onSegment(p: tuple, q: tuple, r: tuple) -> bool:

    if ((q[0] <= max(p[0], r[0])) &
            (q[0] >= min(p[0], r[0])) &
            (q[1] <= max(p[1], r[1])) &
            (q[1] >= min(p[1], r[1]))):
        return True

    return False

# orientation() function
# To find orientation of ordered triplet (p, q, r).
# The function returns following values if p,q,r are:
# 0 --> collinear
# 1 --> Clockwise
# 2 --> Counterclockwise


def orientation(p: tuple, q: tuple, r: tuple) -> int:

    val = (((q[1] - p[1]) *
            (r[0] - q[0])) -
           ((q[0] - p[0]) *
            (r[1] - q[1])))

    if val == 0:
        return 0
    if val > 0:
        return 1
    else:
        return 2


# doIntersect() function to check if line segments (p1,q1) and
# line (p2,q2) intersect or not.

def doIntersect(p1, q1, p2, q2):

    # Finding the four orientations needed for
    # general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if (o1 != o2) and (o3 != o4):
        return True

    # Special Cases
    # p1, q1 and p2 are collinear and
    # p2 lies on segment p1q1
    if (o1 == 0) and (onSegment(p1, p2, q1)):
        return True

    # p1, q1 and p2 are collinear and
    # q2 lies on segment p1q1
    if (o2 == 0) and (onSegment(p1, q2, q1)):
        return True

    # p2, q2 and p1 are collinear and
    # p1 lies on segment p2q2
    if (o3 == 0) and (onSegment(p2, p1, q2)):
        return True

    # p2, q2 and q1 are collinear and
    # q1 lies on segment p2q2
    if (o4 == 0) and (onSegment(p2, q1, q2)):
        return True

    # if all condition above fails then , line segment don't intersect
    return False


# the very first function, is_point_inside_polygon()
# Returns true if the point p lies
# inside the polygon[] with n vertices


def is_point_inside_polygon(points: list, p: tuple) -> bool:

    n = len(points)

    # There must be at least 3 vertices
    # in polygon
    if n < 3:
        return False

    # Creating a point for line segment
    # from p to infinite
    extreme = (INT_MAX, p[1])
    count = i = 0

    while True:
        next = (i + 1) % n

        # Check if the line segment from 'p' to
        # 'extreme' intersects with the line
        # segment from 'polygon[i]' to 'polygon[next]'
        if (doIntersect(points[i],
                        points[next],
                        p, extreme)):

            # If the point 'p' is collinear with line
            # segment 'i-next', then check if it lies
            # on segment. If it lies, return true, otherwise false
            if orientation(points[i], p,
                           points[next]) == 0:
                return onSegment(points[i], p,
                                 points[next])

            count += 1

        i = next
        # next =i=0 means we came to again same starting vertex
        if (i == 0):
            break

    # Return true if count is odd, false otherwise
    return (count % 2 == 1)


# control of code execution starts here
if __name__ == '__main__':
    # taking  vertices of polygon in clockwise fashion

    # list of tuples
    polygon = [(0, 0), (10, 0), (10, 10), (0, 10)]

    # check if point p(20,20) is inside polygon or not
    p = (10, 0)
    if (is_point_inside_polygon(points=polygon, p=p)):
        print('Yes')
    else:
        print('No')
