import arcade

class desktop_Platform:
  def __init__(self):
    self.c = None
    self.ctrl = None
    self.items = {}
    self.player = None
    self.statics = {}
    self.itemSprites = arcade.SpriteList()
    self.playerSprites = arcade.SpriteList()
    self.staticSprites = arcade.SpriteList()
    self.textures = {}
