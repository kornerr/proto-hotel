from cld import *
from ht_aux import *
from ht_Context import *

# Go to scene
#
# Conditions:
# 1. Item with an associated goto has just been selected
@cld_by_value
def ht_gotoScene(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "selectedItem" and
        c.selectedItem is not None and
        cld_len(c.goto) > 0
    ):
        scene = ht_aux_gotoScene(c.goto, c.selectedItem)
        print(f"ИГР scene-01: '{scene}'")
        if (scene is not None):
            c.scene = scene
            print(f"ИГР scene-02: '{c.scene}'")
            c.recentField = "scene"
            return c

    c.recentField = "none"
    return c

# Reset player position
#
# Conditions:
# 1. Player sprites have been reset due to scene loading for the first time
# 2. Mouse has been clicked
# 3. Goto has been executed
@cld_by_value
def ht_resetPlayerPosition(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "didResetScenePlayerSprites" and
        cld_len(c.playerPosition) == 0
    ):
        tree = c.sceneCfgTrees[c.scene]
        left = float(tree["player"]["left"])
        top = float(tree["player"]["base"])
        c.playerPosition = [left, top]
        c.recentField = "playerPosition"
        return c

    if (
        c.recentField == "didClickMouse"
    ):
        left = c.didClickMouse[0]
        top = c.playerPosition[1]
        c.playerPosition = [left, top]
        c.recentField = "playerPosition"
        return c

    c.recentField = "none"
    return c

# Select goto
#
# Conditions:
# 1. Item with an associated goto has just been selected
@cld_by_value
def ht_resetSelectedGoto(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "selectedItem" and
        c.selectedItem is not None
    ):
        c.selectedGoto = ht_aux_itemGoto(c.goto, c.selectedItem)
        c.recentField = "selectedGoto"
        return c

    c.recentField = "none"
    return c
