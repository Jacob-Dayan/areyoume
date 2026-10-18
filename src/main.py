from pathlib import Path

import simplepbr
from panda3d.core import Filename, getModelPath
from ursina import *
from ursina import application, camera, mouse
from ursina.input_handler import held_keys
from ursina.prefabs.first_person_controller import FirstPersonController

import ground
import music
import optimizer
import world
from logic import reset_object, update_camera_view
from sprint import handle_sprint

START_SPEED = 10
FLYING_GRAVITY = -2
START_GRAVITY = 4

cam_dist = 0
# me = sigma
# me.humor.isFunny = False



current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
getModelPath().appendDirectory(Filename.fromOsSpecific(str((parent_dir / "assets" / "textures").resolve())))

app = Ursina(title="AreYouMe", icon="icon.ico")
application.asset_folder = parent_dir
window.fullscreen = True
window.show_ursina_splash = False
pipeline = simplepbr.init()
window.icon = "icon.ico"
window.exit_button.enabled = False
window.cog_button.enabled = False

# optimizer level geometry (requires Ursina app context)
optimizer.load_optimized_level()


# more setups
world.setup_world()
ground.setup_ground()


player = FirstPersonController(position=(0, 2, 0))
player.cursor.visible = False

ALVIN_SCALE = Vec3(1.35, 1.35, 1.35)
player.character = Entity(
    model="alvin.glb", parent=player,
    scale=ALVIN_SCALE,
    y=1,
    color=color.gray,
    name="alvin",
    rotation_y=0,
    enabled=False,
)

camera.parent = player.camera_pivot
camera.position = (0, 0, 0)
camera.rotation_x = 0

mouse.locked = True


def update() -> None:
    global cam_dist

    # if held_keys['up arrow']:
    # player.position += player.forward * START_SPEED * time.dt
    # if held_keys['down arrow']:
    # player.position += player.back * START_SPEED * time.dt
    # if held_keys['left arrow']:
    # player.position += player.left * START_SPEED * time.dt
    # if held_keys['right arrow']:
    # player.position += player.right * START_SPEED * time.dt


    """ ursina.prefabs.first_person_controller.FirstPersonController.position is a Vec3, the y-coordinate is at index 1. """
    if player.position[1] < -30:
        reset_object(player)

    handle_sprint(player, START_SPEED)

    # Update camera based on current cam_dist
    cam_dist = update_camera_view(player, camera, cam_dist)

    if held_keys["space"]:
        player.gravity = FLYING_GRAVITY
    else:
        player.gravity = START_GRAVITY


def input(key) -> None:
    global cam_dist

    match key:
        case "escape":
            application.quit()  # `app.quit()` is an error apparently, `application.quit()` is 'da thing'. who knew?
        case "r":
            reset_object(player)
        # Scroll detection
        case "scroll up":
            cam_dist -= 1
        case "scroll down":
            cam_dist += 1

# You can also load a different music file
# or comment ok out the line above to stop the music
# too lazy to add a visual music button so fuck it you listen to my music
music.Music().loop(parent_dir / "assets" / "sounds" / "music" / "background_music.ogg")


app.run() # type: ignore[attr-defined]
