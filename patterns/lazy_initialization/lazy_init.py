import time
from datetime import datetime


class Satellite:

    def __init__(self):
        time.sleep(10)

    def get_coord(self):
        return 0, 0


class SatelliteProxy:

    def __init__(self):
        self.satellite = None

    def get_coord(self):
        if self.satellite is None:
            self.satellite = Satellite()
        return self.satellite.get_coord()


class MoonPhotos:

    def __init__(self, satellite):
        self.satellite = satellite

    def take_pic(self):
        if int(time.mktime(datetime.now().timetuple()))%2 == 0:
            self.satellite.get_coord()
        else:
            print('It is not time to take picture')

if __name__ == '__main__':
    moon_photos = MoonPhotos(SatelliteProxy())
    moon_photos.take_pic()