from cld import *

# Find scene associated with the item
def ht_aux_gotoScene(
    goto: dict[str, tuple[str, str]],
    item: str
) -> str:
    print(f"ИГР ht_aux_gotoS goto: '{goto}'")
    for name in goto:
        d = goto[name]
        if (
            item == d[0] 
        ):
            return d[2]
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
    goto: dict[str, tuple[str, float, str]],
    item: str
) -> str:
    for name in goto:
        d = goto[name]
        if (
            item == d[1] 
        ):
            return name
    return None
