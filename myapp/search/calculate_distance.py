from math import radians, cos, sin, asin, sqrt

# using Haversine formula
def haversine(lat1, lon1, lat2, lon2):
      try:
            if (lat1, lon1, lat2, lon2):
                  R = 6372.8 # this is in km.

                  dLat = radians(lat2 - lat1)
                  dLon = radians(lon2 - lon1)
                  lat1 = radians(lat1)
                  lat2 = radians(lat2)

                  a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
                  c = 2*asin(sqrt(a))

                  return R * c
            else:
                  raise TypeError('(lat1, lon1, lat2, lon2) one of it is missing')
      except ValueError:
            raise 'data should be number'