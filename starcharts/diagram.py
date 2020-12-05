from .svg import Svg

MARGIN_X = 50
MARGIN_Y = 50
MAGNIFICATION = 500

MIN_D = 1
MAX_D = 4

DIMMEST_MAG = 6
BRIGHTEST_MAG = -1.5


class Diagram:
    def __init__(self, area, star_data_list, star_color="white"):
        self.area = area
        self.star_data_list = star_data_list
        self.curves = []
        self.star_color = star_color
        self.border_min_x = (
            self.border_min_y
        ) = self.border_max_x = self.border_max_y = None

    def add_curve(self, curve_points):
        self.curves.append(curve_points)

    def _mag_to_d(self, m):
        mag_range = DIMMEST_MAG - BRIGHTEST_MAG
        m_score = (DIMMEST_MAG - m) / mag_range
        r_range = MAX_D - MIN_D
        return MIN_D + m_score * r_range

    def _invert_and_offset(self, x, y):
        return x + MARGIN_X, (self.star_data_list.max_y - y) + MARGIN_Y

    def get_svg(self):
        svg = Svg()

        # add stars first
        for star_data in self.star_data_list.data:
            x, y = self._invert_and_offset(star_data.x, star_data.y)
            svg.circle(x, y, self._mag_to_d(star_data.mag), self.star_color)

        # next add labels
        for star_data in self.star_data_list.data:
            if star_data.label:
                x, y = self._invert_and_offset(star_data.x, star_data.y)
                self._mag_to_d(star_data.mag)

        return svg.to_list()
