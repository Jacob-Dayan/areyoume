from ursina import Audio

class Music:
    def loop(self, path):
        Audio(path, loop=True)
    def play(self, path):
        Audio(path)
    def stop(self, path):
        Audio.stop(path)
