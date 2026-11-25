import math

# Helper functions

def calc_distance(p_1, p_2):
    """
    Calculates distance between two points.

    ARGUMENTS
        p1      Point 1 coordinates; tuple
        p2      Point 2 coordinates; tuple

    OUTPUT
        Straight-line distance from p1->p2; scalar
    """
    return math.sqrt((p_2[0]-p_1[0])**2 + (p_2[1]-p_1[1])**2)

def point_to_line(p_1, p_2, p_3):
    """
    Defines a line passing through two points. Determines whether the tangent to
    the line passing through a third point intersects between the first two. Formula is
    defined at http://paulbourke.net/geometry/pointlineplane/

    ARGUMENTS
        p_1     Point 1 coordinates; tuple
        p_2     Point 2 coordinates; tuple
        p_3     Point 3 coordinates; tuple

    OUTPUT
        r_u         p_1 -> p_2 distance intersection ratio; scalar
        tan_len     Distance from p_1 -> p_2 line to p_3; scalar
    """
    # distance from P1 -> P2
    dist = math.sqrt((p_2[0] - p_1[0])**2 + (p_2[1] - p_1[1])**2)

    # determine intersection ratio u
    # for three points A, B with a line between them and a third point C, the tangent to the line AB
    # passing through C intersects the line AB a distance along its length equal to u*|AB|
    r_u = ((p_3[0] - p_1[0])*(p_2[0] - p_1[0]) + (p_3[1] - p_1[1])*(p_2[1] - p_1[1]))/(dist**2)

    # intersection point
    p_i = (p_1[0] + r_u*(p_2[0] - p_1[0]), p_1[1] + r_u*(p_2[1] - p_1[1]))

    # distance from P3 to intersection point
    tan_len = calc_distance(p_i, p_3)

    return r_u, tan_len
