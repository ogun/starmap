from .svg import Svg

MARGIN_X = 50
MARGIN_Y = 50
MAGNIFICATION = 500

MIN_D = 1
MAX_D = 4

DIMMEST_MAG = 6
BRIGHTEST_MAG = -1.5

CONS = [
    ("4301", "4295"),
    ("4295", "4554"),
    ("4554", "4660"),
    ("4660", "4905"),
    ("4905", "5054"),
    ("5054", "5191"),
    ("4853", "4656"),
    ("4730", "4763"),
    ("5984", "5953"),
    ("5953", "5944"),
    ("5953", "6084"),
    ("6084", "6134"),
    ("6134", "6165"),
    ("6165", "6241"),
    ("6241", "6247"),
    ("6247", "6247"),
    ("6247", "6271"),
    ("6271", "6553"),
    ("6553", "6527"),
    ("6527", "6508"),
    ("15", "337"),
    ("337", "603"),
    ("15", "39"),
    ("39", "8781"),
    ("8781", "8775"),
    ("8775", "15"),
    ("8781", "8308"),
    ("21", "168"),
    ("168", "264"),
    ("264", "403"),
    ("403", "542"),
    ("7924", "7796"),
    ("7796", "7615"),
    ("7615", "7417"),
    ("7796", "7949"),
    ("7796", "7528"),
    ("2061", "1879"),
    ("1879", "1790"),
    ("1790", "1852"),
    ("1852", "1713"),
    ("1852", "1903"),
    ("1903", "1948"),
    ("1948", "2061"),
    ("1948", "2004"),
    ("2004", "1713"),
    ("3982", "3975"),
    ("3975", "4057"),
    ("4057", "4031"),
    ("4031", "3905"),
    ("3905", "3873"),
    ("3982", "4359"),
    ("4359", "4534"),
    ("4534", "4357"),
    ("4357", "4359"),
    ("4357", "4057"),
    ("2491", "2294"),
    ("2491", "2693"),
    ("2693", "2827"),
    ("2693", "2618"),
    ("6879", "6746"),
    ("6746", "6859"),
    ("6859", "6913"),
    ("6913", "7039"),
    ("7039", "7121"),
    ("7121", "7234"),
    ("7234", "7194"),
    ("7194", "6879"),
    ("1708", "2088"),
    ("2088", "2095"),
    ("2095", "1791"),
    ("1791", "1577"),
    ("1577", "1641"),
    ("1641", "1708"),
    ("1791", "1409"),
    ("1409", "1346"),
    ("1910", "1457"),
    ("1457", "1346"),
    ("2421", "2650"),
    ("2650", "2777"),
    ("2777", "2905"),
    ("2905", "2990"),
    ("2990", "2891"),
    ("2891", "2697"),
    ("2697", "2473"),
    ("2473", "2286"),
    ("1220", "1122"),
    ("1122", "1017"),
    ("1017", "915"),
    ("915", "834"),
    ("1017", "936"),
    ("5340", "5478"),
    ("5340", "5235"),
    ("5340", "5429"),
    ("5340", "5506"),
    ("5506", "5681"),
    ("5681", "5602"),
    ("5602", "5435"),
    ("5435", "5429"),
    ("7557", "7602"),
    ("7602", "7710"),
    ("7710", "7377"),
    ("7377", "7235"),
    ("7235", "7525"),
    ("7525", "7557"),
    ("7377", "7236"),
    ("7001", "7056"),
    ("7056", "7106"),
    ("7106", "7178"),
    ("7178", "7139"),
    ("7139", "7056"),
]


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

        # add lines
        for con in CONS:
            left = con[0]
            right = con[1]

            left_star = next(
                (star for star in self.star_data_list.data if star.label == left), None
            )
            if not left_star:
                continue

            right_star = next(
                (star for star in self.star_data_list.data if star.label == right), None
            )
            if not right_star:
                continue

            x1, y1 = self._invert_and_offset(left_star.x, left_star.y)
            x2, y2 = self._invert_and_offset(right_star.x, right_star.y)
            svg.line(x1, y1, x2, y2, 1, self.star_color)

        # next add labels
        for star_data in self.star_data_list.data:
            if star_data.label:
                x, y = self._invert_and_offset(star_data.x, star_data.y)
                self._mag_to_d(star_data.mag)

        return svg.to_list()
