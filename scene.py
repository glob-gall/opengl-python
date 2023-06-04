from model import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # n, s = 30, 3
        # for x in range(-n, n, s):
        #     for z in range(-n, n, s):
        #         add(Cube(app, pos=(x, -s, z)))

        add(Cat(app, pos=(0, -5, -60)))
        
        add(Road(app, pos=(0,-6,-10)))
        add(Road(app, pos=(0,-6,-41)))
        add(House(app, pos=(0,0,0)))

    def render(self):
        for obj in self.objects:
            obj.render()