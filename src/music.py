from ursina import Audio

class Music:
    def loop(self, path):
        Audio(path, loop=True)
