from cld import *
from ht_aux import *
from ht_Context import *

# Go to scene with a delay
#
# Conditions:
# 1. Goto has been selected
@cld_by_value
def ht_delayScene(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "selectedGoto" and
        c.selectedGoto is not None and
        cld_len(c.goto) > 0
    ):
        c.delayScene = c.goto[c.selectedGoto][4]
        c.recentField = "delayScene"
        return c

    c.recentField = "none"
    return c

# Reset player position
#
# Conditions:
# 1. Player sprites have been reset due to scene loading for the first time
# 2. Player sprites have been reset due to scene loading for the second time and on
# 3. Mouse has been clicked
# 4. Goto has been selected
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
        c.recentField == "didResetScenePlayerSprites" and
        cld_len(c.playerPosition) == 2
    ):
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

    if (
        c.recentField == "scene" and
        c.selectedGoto is not None and
        c.goto[c.selectedGoto][2] is not None and
        c.goto[c.selectedGoto][3] is not None
    ):
        gt = c.goto[c.selectedGoto]
        top = float(gt[2])
        left = float(gt[3])
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

# Select comment (i.e., make it visible)
#
# Conditions:
# 1. Item with an associated comment has just been selected
@cld_by_value
def ht_selectComment(
    c: ht_Context
) -> ht_Context:
    if (
        c.recentField == "selectedItem" and
        c.selectedItem is not None
    ):
        c.selectedComment = ht_aux_itemComment(c.comments, c.selectedItem)
        c.recentField = "selectedComment"
        return c

    c.recentField = "none"
    return c
