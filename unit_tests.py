import unittest

from state_server import Coordinates


class UnitTests(unittest.TestCase):

    def test_point_in_polygon(self):
        state_coordinates = [[-77.475793, 39.719623], [-80.524269, 39.721209], [-80.520592, 41.986872], [-74.705273, 41.375059], [-75.142901, 39.881602], [-77.475793, 39.719623]]
        point_in_state = Coordinates.point_inside_polygon(-77.036133, 40.513799, state_coordinates)
        self.assertEquals(point_in_state, True)

    def test_read_json_file_pa(self):
        coordinates = Coordinates(40.513799, -77.036133)
        state = coordinates.parse_states_json_for_match()
        self.assertEqual(state, 'Pennsylvania')

    def test_read_json_file_ok(self):
        coordinates = Coordinates(35.485162, -96.893323)
        state = coordinates.parse_states_json_for_match()
        self.assertEqual(state, 'Oklahoma')

    def test_read_json_file_wv(self):
        coordinates = Coordinates(39.511637, -80.645768)
        state = coordinates.parse_states_json_for_match()
        self.assertEqual(state, 'West Virginia')

    def test_read_json_file_sd(self):
        coordinates = Coordinates(44.414159, -103.514929)
        state = coordinates.parse_states_json_for_match()
        self.assertEqual(state, 'South Dakota')

    def test_read_json_file_nv(self):
        coordinates = Coordinates(35.978121, -114.834509)
        state = coordinates.parse_states_json_for_match()
        self.assertEqual(state, 'Nevada')


if __name__ == '__main__':
    unittest.main()
