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

# Create comment sprites
#
# Conditions:
# 1. Config textures has just been loaded
def desktop_createConfigCommentSprites(p):
    if (
        p.c.recentField != "didLoadConfigTextures"
    ):
        return

    for key in p.c.cfgTree:
        if (
            cld_startswith(key, "comment ")
        ):
            name = cfg_aux_subsectionName(key)
            sprite = desktop_aux_createCommentSprite(p, name, p.c.cfgTree, key)
            p.comments[name] = sprite
            p.commentSprites.append(sprite)
    # Report finish.
    p.ctrl.set("didCreateConfigCommentSprites", True)

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

# Display comment
#
# Conditions:
# 1. Mouse has just been clicked
def desktop_displayCommentForSelectedItem(p):
    if (
        p.c.recentField != "didClickMouse"
    ):
        return
    print("ИГР desktop_displayCFSI-01")
    itemId = desktop_aux_firstVisibleItemAt(p, p.c.didClickMouse)
    print("ИГР desktop_displayCFSI-02")
    if (itemId is None):
        return
    commId = comment_aux_item(itemId)
    if (commId is None):
        return
    print("ИГР desktop_displayCFSI-03")
    p.comments[commId].visible = True
    print("ИГР desktop_displayCFSI-04")
