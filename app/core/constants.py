VIRTUAL_DIMENSION = (128, 128)
WINDOW_DIMENSION = (640, 640)
SCALE_FACTOR = 5
TILE_SIZE = 14

BOARD_COLOR = (0, 228, 54)

DATA = {
    "close_button": {
        "frames": [(0,0)],
        "size": (8,8)
    },
    "mouse": {
        "normal": {
            "frames": [(0,8)],
            "size": (8,8)
        },
        "pointer": {
            "frames": [(0,16)],
            "size": (8,8)
        },
        "selected": {
            "frames": [(0,24)],
            "size": (8,8)
        },
        "shovel": {
            "frames": [(0,32)],
            "size": (8,8)
        }
    },
    "store_icons": {
        "peashooter": {
            "frames": [(0,40)],
            "size": (7,7)
        },
        "sunflower": {
            "frames": [(0,47)],
            "size": (7,7)
        },
        "cherry_bomb": {
            "frames": [(0,54)],
            "size": (7,7)
        },
        "wallnut": {
            "frames": [(0,61)],
            "size": (7,7)
        }
    },
    "sun": {
        "frames": [(0,96)],
        "size": (8,8)
    },
    "projectiles": {
        "pea": {
            "damage": 10,
            "frames": [(0,104)],
            "size": (4,4)
        },
        "frozen_pea": {
            "damage": 10,
            "frames": [(4, 104)],
            "size": (4,4)
        }
    },
    "shovel": {
        "frames": [(0,108)],
        "size": (5,12)
    },
    "grass": {
        "variants": [(8,113), (22,113), (36,113), (50,113)],
        "size": (14,14)
    },
    "plants": {
        "peashooter": {
            "type": "offensive",
            "hp": 100,
            "atack_delay": 2,
            "num_atacks": 1,
            "shooting": {
                "frames": [(8,26)],
                "size": (11,13)
            },
            "idle": {
                "frames": [(8,0), (8,13)],
                "size": (11,13)
            },
            "projectile": "pea"
        },
        "sunflower": {
            "type": "sun_producer",
            "hp": 50,
            "produce_delay": 6,
            "sun_value": 20,
            "producing": {
                "frames": [(19,26)],
                "size": (11,13)
            },
            "idle": {
                "frames": [(19,0), (19,13)],
                "size": (11,13)
            }
        },
        "cherry_bomb": {
            "type": "instantaneous",
            "frames": [(30,0), (30,13), (30,26)],
            "size": (11,13),
        },
        "wallnut": {
            "type": "defensive",
            "hp": 500,
            "full": {
                "frames": [(41,0)],
                "size": (11,13)
            },
            "damaged": {
                "frames": [(41,13)],
                "size": (11,13)
            },
            "critical": {
                "frames": [(41,26)],
                "size": (11,13)
            }
        }
    },
    "zombies": {
        "basic": {
            "hp": 40,
            "speed": 4,
            "damage": 20,
            "walking": {
                "frames": [(8, 64), (21, 64), (34, 64)],
                "size": (13,22)
            },
            "eating": {
                "frames": [(47, 64), (60, 64)],
                "size": (13,22)
            },
            "dying": {
                "frames": [(73, 64)],
                "size": (14,20)
            },
            "dead": {
                "frames": [(87, 64)],
                "size": (24,9)
            }
        }
    }
}

LEVELS = {
    "level_1": {
        "store_items": [
            {"type": "peashooter", "price": 50}
        ]
    },
    "level_2": {
        "store_items": [
            {"type": "sunflower", "price": 25},
            {"type": "peashooter", "price": 50}
        ]
    },
    "level_3": {
        "store_items": [
            {"type": "sunflower", "price": 20},
            {"type": "peashooter", "price": 50},
            {"type": "wallnut", "price": 25}
        ]
    },
    "level_4": {
        "store_items": [
            {"type": "sunflower", "price": 20},
            {"type": "peashooter", "price": 50},
            {"type": "wallnut", "price": 25},
            {"type": "cherry_bomb", "price": 90}
        ]
    }
}