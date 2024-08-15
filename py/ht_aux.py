from cld import *

# Find scene associated with the item and assign it to the first parameter
def ht_aux_gotoSceneAssign(
    scene: str,
    goto: dict[str, tuple[str, str]],
    item: str
) -> bool:
    for name in goto:
        d = goto[name]
        if (
            item == d[0] 
        ):
            scene = d[1]
            return True
    return False

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
