""" edb dosyalarini star-charts'in istedigi formata cevirir """
import logging
import os
import math
import ephem

EXT = ".edb"
PATH = "edb/"


def get_lines(file_path):
    """ dosyadaki tum satirlari doner """
    with open(file_path, "r") as edb_file:
        return edb_file.readlines()


def angle_to_right_ascension(angle):
    """ aciyi star-charts'in istedigi formata cevirir """
    return (1 - angle / (2 * math.pi)) * 24


def convert(date, lat, lon, elevation):
    """ degistirme isini yapar """
    gatech = ephem.Observer()
    gatech.lon = lat
    gatech.lat = lon
    gatech.elevation = elevation
    gatech.date = date

    catalog_stars = []
    for edb_file in os.listdir(PATH):
        if edb_file.endswith(EXT):
            catalog_stars.extend(get_lines(PATH + edb_file))

    new_catalog = ""
    for catalog_star in catalog_stars:
        if catalog_star.startswith("#") or catalog_star.strip() == "":
            continue

        try:
            star = ephem.readdb(catalog_star)
            star.compute(gatech)

            ra = angle_to_right_ascension(star.az)
            dec = math.degrees(star.alt)

            new_catalog += f"{ra},{dec},{star.mag}\n"
        except Exception as ex:
            print(catalog_star)
            logging.exception(ex)

    planets = [
        ephem.Jupiter(),
        ephem.Mars(),
        ephem.Mercury(),
        ephem.Moon(),
        ephem.Neptune(),
        ephem.Pluto(),
        ephem.Saturn(),
        ephem.Sun(),
        ephem.Uranus(),
        ephem.Venus(),
    ]
    for planet in planets:
        planet.compute(gatech)
        ra = angle_to_right_ascension(planet.az)
        dec = math.degrees(planet.alt)
        new_catalog += f"{ra},{dec},{planet.mag},{planet.name}\n"

    return new_catalog
