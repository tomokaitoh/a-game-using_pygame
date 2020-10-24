class Settings():
    def __init__(self):
        self.pause = 0.05
        self.screen_width = 500
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.color = [(194, 159, 129), (51, 255, 204)]
        self.character = {
            'size': 20,
            'color': (163, 207, 184),
            'speed': 1,
            'jump_v': 20
        }
        self.gravity = 1.5
