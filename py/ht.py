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
