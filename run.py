from __future__ import division

from datetime import datetime
import dateutil.parser

import tornado.ioloop
import tornado.web

from edb_converter import converter
from starcharts import sky_area
from starcharts.coord_calc import CoordCalc
from starcharts.diagram import Diagram
from starcharts.input_file import InputFile


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        date, lat, lon, elevation, mag_min, mag_max = self.get_query_strings()
        new_catalog = converter.convert(date, lat, lon, elevation)

        input_file = InputFile(new_catalog)
        area = sky_area.SKY_AREA_CUSTOM
        area.mag_min = mag_min
        area.mag_max = mag_max

        star_data_list = input_file.get_stars(area)

        cc = CoordCalc(star_data_list, area, 500)
        cc.process()

        d = Diagram("My Star Map", area, star_data_list)
        list(map(d.add_curve, cc.calc_curves()))
        svg_file = d.get_svg("")

        self.set_header("Content-Type", "image/svg+xml")
        self.write("".join(svg_file))

    def get_query_strings(self):
        today_utc = datetime.utcnow().isoformat()
        date_argument = str(self.get_argument("date", today_utc, strip=True))
        parsed_date = dateutil.parser.parse(date_argument)
        date = parsed_date.strftime("%Y/%m/%d %H:%M:%S")

        lat = str(self.get_argument("lat", "41.015137", strip=True))
        lon = str(self.get_argument("lon", "28.979530", strip=True))
        elevation = int(self.get_argument("elevation", 0, strip=True))
        mag_min = int(self.get_argument("mag_min", 4, strip=True))
        mag_max = int(self.get_argument("mag_max", 0, strip=True))

        return date, lat, lon, elevation, mag_min, mag_max


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
        ]
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
