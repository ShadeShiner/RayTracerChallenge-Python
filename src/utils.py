EPSILON = 0.00001


def equal(a, b):
    return abs(a - b) < EPSILON

def check_axis(origin: int, direction: int):
    # Offset the plane from origin by -1 and +1
    tmin_numerator = (-1 - origin)
    tmax_numerator = (1 - origin)

    if abs(direction) >= EPSILON:
        tmin = tmin_numerator / direction
        tmax = tmax_numerator / direction
    else:
        tmin = tmin_numerator * float("inf")
        tmax = tmax_numerator * float("inf")

    if tmin > tmax:
        tmin, tmax = tmax, tmin

    return tmin, tmax
