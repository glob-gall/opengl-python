
from orientado.Tree import Tree
from orientado.Cat import Cat
from orientado.Road import Road
from orientado.Grass import Grass
from orientado.House import House,House2

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

        add(Cat(app, pos=(-0.5, -5, -60)))
        
        add(Road(app, pos=(0,-6,-10)))
        add(Road(app, pos=(0,-6,-41)))
        add(House(app, pos=(6,-5,-48)))
        add(House(app, pos=(6,-5,-40)))
        add(House(app, pos=(6,-5,-32)))
        add(House(app, pos=(6,-5,-26)))
        add(House(app, pos=(6,-5,-18)))
        
        add(House2(app, pos=(-7,-5,-48)))
        add(House2(app, pos=(-7,-5,-40)))
        add(House2(app, pos=(-7,-5,-32)))
        add(House2(app, pos=(-7,-5,-26)))
        add(House2(app, pos=(-7,-5,-18)))
        
        add(Grass(app, pos=(-10,-5.5,-3)))
        add(Grass(app, pos=(-10,-5.5,-17)))
        add(Grass(app, pos=(-10,-5.5,-32)))
        add(Grass(app, pos=(-10,-5.5,-47)))
        add(Grass(app, pos=(-10,-5.5,-62)))
        add(Grass(app, pos=(-10,-5.5,-77)))
        
        add(Grass(app, pos=(9,-5.5,-3)))
        add(Grass(app, pos=(9,-5.5,-17)))
        add(Grass(app, pos=(9,-5.5,-32)))
        add(Grass(app, pos=(9,-5.5,-47)))
        add(Grass(app, pos=(9,-5.5,-62)))
        add(Grass(app, pos=(9,-5.5,-77)))
        
        add(Tree(app, pos=(-6,-5.2,-9)))
        add(Tree(app, pos=(10,-5.2,-1)))
        add(Tree(app, pos=(-4,-5.2,-4)))
        add(Tree(app, pos=(-2,-5.2,-1)))
        add(Tree(app, pos=(-13,-5.2,-8)))
        add(Tree(app, pos=(-10,-5.2,-2)))
        

    def render(self):
        for obj in self.objects:
            obj.render()