from ursina import *
from ursina import application
from ursina.prefabs.first_person_controller import FirstPersonController
from logic import reset_object, update_camera_view
import os
import simplepbr
import time
import music
import world
import ground
from sprint import handle_sprint
import json
import optimizer

#definitions
startspeed = 10
flying_gravity = -2
startgravity = 4
cam_dist = 0
#me = sigma
#me.humor.isFunny = False

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
SAVE_FILE = os.path.join(parent_dir, 'worldobjects', 'level_map.json')


app = Ursina(title='AreYouMe') #setup game
window.fullscreen = True
window.show_ursina_splash = False
pipeline = simplepbr.init()
window.icon = '../assets/textures/icon.ico'
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
    model='../assets/alvin/alvin.glb',
    parent=player,
    scale=ALVIN_SCALE,
    y=1,
    color=color.gray,
    name='alvin',
    rotation_y=0,
    enabled=False
)

camera.parent = player.camera_pivot
camera.position = (0, 0, 0)
camera.rotation_x = 0

mouse.locked = True

def update():
    global cam_dist

    #if held_keys['up arrow']:
        #player.position += player.forward * startspeed * time.dt
    #if held_keys['down arrow']:
        #player.position += player.back * startspeed * time.dt
    #if held_keys['left arrow']:
        #player.position += player.left * startspeed * time.dt
    #if held_keys['right arrow']:
        #player.position += player.right * startspeed * time.dt


    """ ursina.prefabs.first_person_controller.FirstPersonController.position is a Vec3, the y-coordinate is at index 1. """
    if player.position[1] < -30:
        reset_object(player)

    handle_sprint(player, startspeed)

    # Update camera based on current cam_dist
    cam_dist = update_camera_view(player, camera, cam_dist)

    if held_keys['space']:
        player.gravity = flying_gravity
    else:
        player.gravity = startgravity



def input(key):
    global cam_dist

    match key:
        case 'escape':
            application.quit()  # `app.quit()` is an error apparently, `application.quit()` is 'da thing'. who knew?
        case 'r':
            reset_object(player)
        # Scroll detection
        case 'scroll up':
            cam_dist -= 1
        case 'scroll down':
            cam_dist += 1

# You can also load a different music file
# Or comment out the line above to stop the music
music.Music().loop('../assets/sounds/music/background_music.ogg')

app.run()
