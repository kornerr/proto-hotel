from cld import *

# Find comment associated with the item
def ht_aux_itemComment(
    comments: dict[str, tuple[float, str, str]],
    item: str
) -> str:
    for name in comments:
        d = comments[name]
        if (
            item == d[1] 
        ):
            return name
    return None

# Find goto associated with the item
def ht_aux_itemGoto(
    goto: dict[str, tuple[str, float, float, str]],
    item: str
) -> str:
    for name in goto:
        d = goto[name]
        if (
            item == d[0] 
        ):
            return name
    return None
