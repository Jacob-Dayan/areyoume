# Areyoume

uhhh🥲

#### BORRING stuff start here, **RUN**!
Areyoume is a high-performance voxel-based "Only Up" style parkour game built in Python with the Ursina engine. Started as an old side project from my early days of game development, it has grown into a playable sandbox with custom world-building tools and specialized mesh optimization.

Now, it's a playable old, side project where I browse young me's code  and enjoying the geniuenly funny comments I left there.

---

## Features

- **Only Up Gameplay**: Jump, climb, sprint, and manage stamina while navigating vertical voxel terrain without falling back to square one.
- **Dynamic Camera**: Seamlessly switch from First-Person view to a dynamic Third-Person camera simply by scrolling your mouse wheel.
- **Stamina & Sprint System**: Burst sprint with `Left Shift` and keep track of stamina cooldowns with on-screen HUD alerts.
- **Checkpoint System**: Hit checkpoints on your climb so mistakes don't wipe all your progress (`R` to quickly respawn at the last saved point).
- **Built-in World Editor**: An in-engine voxel builder to create, edit, and export custom levels as clean JSON maps under `worldobjects/`.
- **Level & Mesh Optimizer**:
  - **BQ (Better Quality)**: Combines block entities into a unified level mesh with automatic collision mapping.
  - **PMODE (Performance Mode)**: Custom face-culling engine that strips hidden internal voxel faces before generating the level geometry, maximizing frame rates on huge maps.

---

## Controls

### In-Game
| Key / Input | Action |
| :--- | :--- |
| **W, A, S, D** | Move |
| **Space** | Jump / Fly |
| **Left Shift** | Sprint (consumes stamina) |
| **Mouse Scroll Up / Down** | Adjust camera distance (First-Person to Third-Person) |
| **R** | Respawn at last checkpoint |
| **Esc** | Quit game |

### World Editor
| Key / Input | Action |
| :--- | :--- |
| **Left Click** | Place a block on target face |
| **C + Left Click** | Turn targeted block into a Checkpoint (green block) |
| **Right Click** | Delete targeted block |
| **S** | Save world to `worldobjects/level_map.json` (auto-creates backups) |
| **L** | Reload world from disk |
| **Right Click + Drag / WASD** | Fly around with editor camera |
| **Esc** | Exit editor |

---

## Quick Start

### 1. Requirements & Dependencies
Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

To set up the environment and install all locked dependencies:

```bash
uv sync
```

> **Note**: `uv` uses [`pyproject.toml`](./pyproject.toml) to specify project dependencies and automatically creates/maintains the cross-platform lockfile [`uv.lock`](./uv.lock). Running `uv sync` ensures your `.venv` perfectly matches the locked dependencies.

### 2. Launch the Game
```bash
uv run python src/main.py
```
When prompted in the terminal:
- Enter `BQ` (Better Quality) for combined-mesh rendering.
- Enter `PMODE` (Performance Mode) for culled-face optimized rendering.

### 3. Open the World Editor
```bash
uv run python src/world_editor.py
```

---

## Tech Stack

- **Core Language**: Python 3
- **Game Engine**: [Ursina Engine](https://www.ursinaengine.org/)
- **Shading & PBR**: [simplepbr](https://github.com/Moguri/panda3d-simplepbr)

Oh, and  you can fly. You defenetly don't need it, but when you won't be able to beat the game and you decide: __"Yeah, I'll just code it so I fly if I hold space"__, yeah I saved you that part 😉.
