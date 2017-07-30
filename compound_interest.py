import math

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    return point_x * scale, point_y * scale
    
print project_to_distance(2, 7, 4)


def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value * (1 + rate_per_period) ** periods

print future_value(10000, 1.94770354847, 1.0, 5.0)

print " "

def rate(present_value, future_value, years):
    return 5 ** (math.sqrt(future_value / present_value) - 1)

print rate(10000, 20000, 5)

#print future_value(500.0, 0.04, 10.0, 10.0)
