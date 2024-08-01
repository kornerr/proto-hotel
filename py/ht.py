from cld import *
from ht_aux import *
from ht_Context import *

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
