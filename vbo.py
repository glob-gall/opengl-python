import numpy as np
from base import BaseVBO
import pywavefront
from orientado.Tree import TreeVBO
from orientado.Cat import CatVBO
from orientado.House import HouseVBO,House2VBO
from orientado.Road import RoadVBO
from orientado.Cube import CubeVBO
from orientado.Grass import GrassVBO
#virtual buffer object
class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['cat'] = CatVBO(ctx)
        self.vbos['road'] = RoadVBO(ctx)
        self.vbos['house'] = HouseVBO(ctx)
        self.vbos['house2'] = House2VBO(ctx)
        self.vbos['grass'] = GrassVBO(ctx)
        self.vbos['tree'] = TreeVBO(ctx)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]

















