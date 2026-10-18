from ursina import Sky

import logger


def setup_world() -> None:
    Sky(texture="../assets/textures/sky.jpg")

    # using `owned logger` cause that's what ruff said
    logger.debug("World Environment Loaded.")
