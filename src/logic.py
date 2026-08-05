from ursina import clamp, Vec3


current_checkpoint = Vec3(0, 2, 0)

def reset_object(player):
    player.position = current_checkpoint
    player.rotation = (0, 0, 0)

def update_camera_view(player, camera, camera_distance):
    dist = clamp(camera_distance, 0, 20)
    if dist <= 0:
        camera.position = (0, 0, 0)
        player.character.enabled = False
    else:
        player.character.enabled = True
        camera.position = (0, (dist / 4) + 1, -dist)
    return dist
