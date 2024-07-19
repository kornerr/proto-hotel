import arcade
from cld import *
from desktop_Platform import *

# Convert String config value to Bool or Float if possible
def desktop_aux_convertValue(
    value: str
) -> any:
    # Bool.
    if (
        value == "false"
    ):
        return False
    elif (
        value == "true"
    ):
        return True
    # Float.
    elif (
        cld_isdigit(value)
    ):
        return float(value)
    # String.
    return value

def desktop_aux_createPlayerSprite(
    p: desktop_Platform,
    name: str,
    desc: dict[str, str]
):
    sp = arcade.Sprite()
    sp.guid = name
    texName = desc["texture"]
    sp.texture = p.textures[texName]
    # Position.
    sp.left = float(desc["left"])
    sp.top = float(desc["base"])
    # Visibility.
    sp.visible = True if desc["visible"] == "true" else False

    return sp

def desktop_aux_createStaticSprite(
    p: desktop_Platform,
    name: str,
    desc: dict[str, str]
):
    sp = arcade.Sprite()
    sp.guid = name
    texName = desc["texture"]
    sp.texture = p.textures[texName]
    # Position.
    sp.left = float(desc["left"])
    sp.top = float(desc["top"])
    # Visibility.
    sp.visible = True if desc["visible"] == "true" else False

    return sp

def desktop_aux_loadTexture(
    resDir: str,
    desc: dict[str, str]
):
    path = resDir + "/" + desc["file"]
    return arcade.load_texture(
        path,
        x = float(desc["x"]),
        y = float(desc["y"]),
        width = float(desc["width"]),
        height = float(desc["height"])
    )
