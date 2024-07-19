import arcade

class desktop_Platform:
  def __init__(self):
    self.c = None
    self.ctrl = None
    self.player = None
    self.statics = {}
    self.playerSprites = arcade.SpriteList()
    self.staticSprites = arcade.SpriteList()
    self.textures = {}
