def get_ordered(points):
    points.sort(key=lambda p: (p[0] - 0.0) ** 2 + (p[1] - 0.0)**2)
    return points
