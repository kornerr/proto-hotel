import arcade

class desktop_Window(arcade.Window):
    def __init__(self, p):
        super().__init__(
            p.c.windowWidth,
            p.c.windowHeight,
            p.c.windowTitle,
        )
        self.antialiasing = p.c.windowAntialiasing
        self.background_color = arcade.color_from_hex_string(p.c.windowBackgroundColor)
        self.p = p

    def on_draw(self):
        arcade.start_render()
        self.p.staticSprites.draw()
        self.p.playerSprites.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        self.p.ctrl.set("didClickMouse", [x, y])

    def on_update(self, delta):
        self.p.playerSprites.update_animation()
