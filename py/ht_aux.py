from cld import *

# Find sound associated with an item or a scene
def ht_aux_findSound(
    soundCfgTrees: dict[str, dict[str, str]],
    elementType: str,
    element: str
) -> str:
    for name in soundCfgTrees:
        tree = soundCfgTrees[name]
        for key in tree:
            if (
                cld_startswith(key, "play ") and
                elementType in tree[key] and
                tree[key][elementType] == element
            ):
                return name
    return None

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
    goto: dict[str, tuple[float, str, float, float, str]],
    item: str
) -> str:
    for name in goto:
        d = goto[name]
        if (
            item == d[1] 
        ):
            return name
    return None
