import arcade

class desktop_Platform:
  def __init__(self):
    self.c = None
    self.ctrl = None
    self.comments = {}
    self.items = {}
    self.player = None
    self.statics = {}
    self.commentSprites = arcade.SpriteList()
    self.itemSprites = arcade.SpriteList()
    self.playerSprites = arcade.SpriteList()
    self.staticSprites = arcade.SpriteList()
    self.textures = {}
