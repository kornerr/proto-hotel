from cfg_aux import *
from cld import *
from desktop_aux import *
from desktop_Platform import *

# Pass config init key-value pairs to context controller
#
# Conditions:
# 1. Config tree has just been parsed
def desktop_applyConfigInit(p):
    if (
        p.c.recentField != "cfgTree"
    ):
        return

    for key in p.c.cfgTree["init"]:
        val = p.c.cfgTree["init"][key]
        value = desktop_aux_convertValue(val)
        p.ctrl.set(key, value)

# Create item sprites
#
# Conditions:
# 1. Config textures has just been loaded
def desktop_createConfigItemSprites(p):
    if (
        p.c.recentField != "didLoadConfigTextures"
    ):
        return

    for key in p.c.cfgTree:
        if (
            cld_startswith(key, "item ")
        ):
            name = cfg_aux_subsectionName(key)
            sprite = desktop_aux_createItemSprite(p, name, p.c.cfgTree[key])
            p.items[name] = sprite
            p.itemSprites.append(sprite)
    # Report finish.
    p.ctrl.set("didCreateConfigItemSprites", True)

# Create player sprites
#
# Conditions:
# 1. Config textures has just been loaded
def desktop_createConfigPlayerSprites(p):
    if (
        p.c.recentField != "didLoadConfigTextures"
    ):
        return

    for key in p.c.cfgTree:
        if (
            key == "player"
        ):
            sprite = desktop_aux_createPlayerSprite(p, key, p.c.cfgTree[key])
            p.player = sprite
            p.playerSprites.append(sprite)
    # Report finish.
    p.ctrl.set("didCreateConfigPlayerSprites", True)

# Create static sprites
#
# Conditions:
# 1. Config textures has just been loaded
def desktop_createConfigStaticSprites(p):
    if (
        p.c.recentField != "didLoadConfigTextures"
    ):
        return

    for key in p.c.cfgTree:
        if (
            cld_startswith(key, "static ")
        ):
            name = cfg_aux_subsectionName(key)
            sprite = desktop_aux_createStaticSprite(p, name, p.c.cfgTree[key])
            p.statics[name] = sprite
            p.staticSprites.append(sprite)
    # Report finish.
    p.ctrl.set("didCreateConfigStaticSprites", True)

# Load textures
#
# Conditions:
# 1. Config tree has just been parsed
def desktop_loadConfigTextures(p):
    if (
        p.c.recentField != "cfgTree"
    ):
        return

    for key in p.c.cfgTree:
        if (
            cld_startswith(key, "texture ")
        ):
            name = cfg_aux_subsectionName(key)
            tex = desktop_aux_loadTexture(p.c.cfgDir, p.c.cfgTree[key])
            p.textures[name] = tex
    # Report finish.
    p.ctrl.set("didLoadConfigTextures", True)

# Move player instantly along X axis
#
# Conditions:
# 1. Mouse has just been clicked
def desktop_movePlayerInstantly(p):
    if (
        p.c.recentField != "didClickMouse"
    ):
        return

    p.player.left = p.c.didClickMouse[0]

# Print selected item id/name
#
# Conditions:
# 1. Item has just been selected
def desktop_printSelectedItem(p):
    if (
        p.c.recentField != "selectedItem"
    ):
        return
    print(f"ИГР desktop_printSI: '{p.c.selectedItem}'")

# Reset comment visibility
#
# Conditions:
# 1. Item has just been selected
# 2. Time to hide the comment
def desktop_resetCommentVisibility(p):
    if (
        p.c.recentField == "selectedComment" and
        p.c.selectedComment != None
    ):
        comm = p.c.comments[p.c.selectedComment]
        delay = comm[0]
        name = comm[2]
        p.statics[name].visible = True
        p.timer.schedule("hideStaticComment", name, delay)

    if (
        p.c.recentField == "hideStaticComment"
    ):
        name = p.c.hideStaticComment
        p.statics[name].visible = False

# Select visible item on mouse click
#
# Conditions:
# 1. Mouse has just been clicked
def desktop_selectItem(p):
    if (
        p.c.recentField != "didClickMouse"
    ):
        return
    item = desktop_aux_firstVisibleItemAt(p, p.c.didClickMouse)
    p.ctrl.set("selectedItem", item)
