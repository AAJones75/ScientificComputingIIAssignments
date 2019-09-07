from math import asin, cos, radians, sin, sqrt


def haversine(long1, lat1, long2, lat2, r):
    rlong1 = radians(long1)
    rlat1 = radians(lat1)
    rlong2 = radians(long2)
    rlat2 = radians(lat2)

    longdiff = rlong2 - rlong1
    latdiff = rlat2 - rlat1

    return 2 * r * asin(sqrt(pow(sin(latdiff / 2), 2) + cos(rlat1) * cos(rlat2) * pow(sin(longdiff / 2), 2)))


long1 = float(input("Enter longitude 1 "))
lat1 = float(input("Enter latitude 1 "))
long2 = float(input("Enter longitude 2 "))
lat2 = float(input("Enter latitude 2 "))

print("The distance between my home and Dr. Moore is approximately ", haversine(long1, lat1, long2, lat2, 3958.8), " miles")
