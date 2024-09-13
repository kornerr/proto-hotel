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

# Load sounds
#
# Conditions:
# 1. Sound config tree has just become available
def desktop_loadConfigSounds(p):
    if (
        p.c.recentField != "soundCfgTrees"
    ):
        return

    for key in p.c.soundCfgTrees:
        snd = desktop_aux_loadSound(p.c.cfgDir, p.c.soundCfgTrees[key]["init"])
        p.audios[key] = snd

    # Report finish.
    p.ctrl.set("didLoadConfigSounds", True)

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
# 1. Player position changed
def desktop_movePlayerInstantly(p):
    if (
        p.c.recentField == "playerPosition"
    ):
        p.player.left = p.c.playerPosition[0]
        p.player.top = p.c.playerPosition[1]

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

# Reset scene
#
# Conditions:
# 1. Scene has been scheduled for goto
def desktop_resetSceneAfterDelay(p):
    if (
        p.c.recentField == "delayScene" and
        p.c.selectedGoto is not None
    ):
        goto = p.c.goto[p.c.selectedGoto]
        delay = float(goto[0])
        p.timer.schedule("scene", p.c.delayScene, delay)

# Create item sprites for activated scene and remove old ones
#
# Conditions:
# 1. Config textures have been loaded or scenes were specified or scene was activated
def desktop_resetSceneItemSprites(p):
    if (
        (
            p.c.recentField == "didLoadConfigTextures" or
            p.c.recentField == "scene" or
            p.c.recentField == "sceneCfgTrees" or
            p.c.recentField == "scenes" 
        ) and
        p.c.scene is not None and
        cld_len(p.c.sceneCfgTrees) > 0 and
        cld_len(p.c.scenes) > 0 and
        p.c.didLoadConfigTextures == True
    ):
        pass
    else:
        return

    #  Remove previous static sprites.
    p.items.clear()
    p.itemSprites.clear()

    # Create new ones.
    tree = p.c.sceneCfgTrees[p.c.scene]
    for key in tree:
        if (
            cld_startswith(key, "item ")
        ):
            name = cfg_aux_subsectionName(key)
            sprite = desktop_aux_createItemSprite(p, name, tree[key])
            p.items[name] = sprite
            p.itemSprites.append(sprite)

    # Report finish.
    p.ctrl.set("didResetSceneItemSprites", True)

# Create player sprites for activated scene and remove old ones
#
# Conditions:
# 1. Config textures have been loaded or scenes were specified or scene was activated
def desktop_resetScenePlayerSprites(p):
    if (
        (
            p.c.recentField == "didLoadConfigTextures" or
            p.c.recentField == "scene" or
            p.c.recentField == "sceneCfgTrees" or
            p.c.recentField == "scenes" 
        ) and
        p.c.scene is not None and
        cld_len(p.c.sceneCfgTrees) > 0 and
        cld_len(p.c.scenes) > 0 and
        p.c.didLoadConfigTextures == True
    ):
        pass
    else:
        return

    #  Remove previous static sprites.
    p.player = None
    p.playerSprites.clear()

    # Create new ones.
    tree = p.c.sceneCfgTrees[p.c.scene]
    for key in tree:
        if (
            key == "player"
        ):
            name = cfg_aux_subsectionName(key)
            sprite = desktop_aux_createPlayerSprite(p, name, tree[key])
            p.player = sprite
            p.playerSprites.append(sprite)

    # Report finish.
    p.ctrl.set("didResetScenePlayerSprites", True)

# Create static sprites for activated scene and remove old ones
#
# Conditions:
# 1. Config textures have been loaded or scenes were specified or scene was activated
def desktop_resetSceneStaticSprites(p):
    if (
        (
            p.c.recentField == "didLoadConfigTextures" or
            p.c.recentField == "scene" or
            p.c.recentField == "sceneCfgTrees" or
            p.c.recentField == "scenes" 
        ) and
        p.c.scene is not None and
        cld_len(p.c.sceneCfgTrees) > 0 and
        cld_len(p.c.scenes) > 0 and
        p.c.didLoadConfigTextures == True
    ):
        pass
    else:
        return

    #  Remove previous static sprites.
    p.statics.clear()
    p.staticSprites.clear()

    # Create new ones.
    tree = p.c.sceneCfgTrees[p.c.scene]
    for key in tree:
        if (
            cld_startswith(key, "static ")
        ):
            name = cfg_aux_subsectionName(key)
            sprite = desktop_aux_createStaticSprite(p, name, tree[key])
            p.statics[name] = sprite
            p.staticSprites.append(sprite)

    # Report finish.
    p.ctrl.set("didResetSceneStaticSprites", True)

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




import arcade


def desktop_checkAudioPlay(p):
    if (
        p.c.recentField != "didClickMouse"
    ):
        return
    arcade.play_sound(p.checkAudio, pan = -1)

# See if GIFs work
def desktop_checkGIF(p):
    if (
        p.c.recentField != "didClickMouse"
    ):
        return
    path = p.c.cfgDir + "/img/123.gif"
    sprite = arcade.load_animated_gif(path)
    sprite.left = 200
    sprite.top = 200
    sprite.visible = True
    p.itemSprites.append(sprite)
