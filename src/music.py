from ursina import Audio


class Music:
    def loop(self, path) -> None:
        Audio(path, loop=True)
    def play(self, path) -> None:
        Audio(path)
    def stop(self, path) -> None:
        Audio.stop(path)
