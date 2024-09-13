from ht_aux import *

def test_ht_aux_itemComment(
) -> str:
    comments = {
        "comm1": [700, "some", "yo"],
        "comm2": [700, "another", "wo"],
    }
    r1 = ht_aux_itemComment(comments, "another")
    r2 = ht_aux_itemComment(comments, "absent")

    if (
        r1 == "comm2" and
        r2 is None
    ):
        return "OK: ht_aux_itemComment"
    return "ERR: ht_aux_itemComment"

def test_ht_aux_itemGoto(
) -> str:
    goto = {
        "goto1": [200, "door1", 50, 100, "yo"],
        "goto2": [None, "door2", None, None, "another"],
    }
    r1 = ht_aux_itemGoto(goto, "door1")
    r2 = ht_aux_itemGoto(goto, "door2")

    if (
        r1 == "goto1" and
        r2 == "goto2"
    ):
        return "OK: ht_aux_itemGoto"
    return "ERR: ht_aux_itemGoto"

def test_ht_aux_findSound(
) -> str:
    soundCfgTrees = {
        "click": {
            "init": {
                "file": "res/sdn/click.wav",
            },
            "play \"when-clicked-start\"": {
                "item": "start",
            }
        }
    }
    snd = ht_aux_findSound(soundCfgTrees, "item", "start")

    if (
        snd == "click"
    ):
        return "OK: ht_aux_itemSound"
    return "ERR: ht_aux_itemSound"
