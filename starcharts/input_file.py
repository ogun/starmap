import codecs
from star_data import StarData, StarDataList


class InputFile:
    def __init__(self, new_catalog):
        self.new_catalog = new_catalog

    def get_stars(self, sky_area):
        """
        Expected line format:
            <RA>,<DEC>,<MAG>

        RA:    0 ->  24
        DEC: +90 -> -90
        MAG: any floating-point value
        """
        matches = []
        idx = 0
        for line in self.new_catalog.splitlines():
            parts = line.split(",")
            ra, dec, mag = map(float, parts[:3])
            label = "" if len(parts) < 4 else parts[3]
            idx += 1

            # because smaller mag values mean brighter stars
            if mag > sky_area.mag_min:
                continue
            if sky_area.mag_max > mag:
                continue
            if not (sky_area.ra_min <= ra <= sky_area.ra_max):
                continue
            if not (sky_area.dec_min <= dec <= sky_area.dec_max):
                continue

            matches.append(StarData(ra, dec, mag, label))

        return StarDataList(matches)
