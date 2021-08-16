import unittest
from  search.calculate_distance import haversine


# Rublevo-Uspenskoye shosse  30 km 
# 37.1412157 55.6909315
# Ryazansky prospekt, Lermontovsky prospekt — Lyubertsy 46 km
# 37.8332525 55.6909315
class TestDistance(unittest.TestCase):
    def test_distance(self):
        # testing distances between Moscow Ring Road and specified place
        self.assertAlmostEqual(haversine(37.4130217, 55.6909315, 37.1412157, 55.6909315), 30.231987268879518)
        self.assertAlmostEqual(haversine(37.4130217, 55.6909315, 37.8332525, 55.6909315), 46.74073491972502)

