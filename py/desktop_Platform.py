import arcade
from desktop_Timer import *

class desktop_Platform:
    def __init__(self):
        self.c = None
        self.ctrl = None
        self.items = {}
        self.itemSprites = arcade.SpriteList()
        self.player = None
        self.playerSprites = arcade.SpriteList()
        self.statics = {}
        self.staticSprites = arcade.SpriteList()
        self.textures = {}
        self.timer = None
