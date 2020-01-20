# Starmap

Starmap is a program for viewing the positions of the stars in the sky at the desired date and location. The format of the star maps included in the program is "[XEphem database file](https://www.mmto.org/obscats/edb.html)" and the file extension is ".edb". The program currently uses the following two catalog files.
* [Yale Bright Star Catalog](http://tdc-www.harvard.edu/catalogs/bsc5.html) (1991)
* Messier Catalog (2005)

It uses the [star-charts](https://github.com/codebox/star-charts) library to draw the position of the stars in the sky and display it in SVG format.

## Query Strings

The parameters you can use while calling the program are given below.

| Parameter | Description |
| ------ | ------ |
| date | Date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. If not, it takes the current date. Ex.: 2017-07-07T12:00:00Z|
| lat | Latitude information. Default value is Istanbul: 41.015137 |
| lon | Longitude information. Default value is Istanbul: 28.979530 |
| elevation | Elevation information. Default: 0 |
| mag_min | The lowest star brightness that will be included in the drawing. The value increases as the brightness decreases. Default: 4 |
| mag_max | The highest star brightness that will be included in the drawing. It can take negative values. Default: 0 |

### About

The positions of the stars are calculated with the help of EDB databases and pyephem library according to the date and location of the request. After the positions of the stars are calculated, these positions are converted to the format requested by the star-charts library with edb_converter. After converting to the desired format, SVG file is created and displayed with the help of star-charts library.
