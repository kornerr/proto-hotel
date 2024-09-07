from ht import *
from ht_Context import *

def test_ht_delayScene(
) -> str:
    c = ht_createContext()
    c.goto = {
        "goto1": [700, "some", None, None, "yo"]
    }
    c.selectedGoto = "goto1"
    c.recentField = "selectedGoto"
    c = ht_delayScene(c)
    if (
        c.delayScene == "yo"
    ):
        return "OK: ht_delayScene"
    return "ERR: ht_delayScene"

def test_ht_resetPlayerAvailability(
) -> str:
    c = ht_createContext()
    c.scene = "scn1"
    c.sceneCfgTrees = {
        "scn1": {
        }
    }
    c.recentField = "didResetScenePlayerSprites"
    c = ht_resetPlayerAvailability(c)
    if (
        c.hasPlayer == False
    ):
        return "OK: ht_resetPlayerAvailability"
    return "ERR: ht_resetPlayerAvailability"

def test_ht_resetPlayerPosition_click(
) -> str:
    c = ht_createContext()
    c.hasPlayer = True
    c.didClickMouse = [100, 150]
    c.playerPosition = [20, 30]
    c.recentField = "didClickMouse"
    c = ht_resetPlayerPosition(c)
    if (
        c.playerPosition[0] == 100 and
        c.playerPosition[1] == 30
    ):
        return "OK: ht_resetPlayerPosition_click"
    return "ERR: ht_resetPlayerPosition_click"

def test_ht_resetPlayerPosition_initial(
) -> str:
    c = ht_createContext()

    c.hasPlayer = True
    c.scene = "scn1"
    c.sceneCfgTrees = {
        "scn1": {
            "player": {
                "base": 50,
                "left": 100
            }
        }
    }
    c.recentField = "hasPlayer"

    c = ht_resetPlayerPosition(c)
    
    if (
        c.playerPosition[0] == 100 and
        c.playerPosition[1] == 50
    ):
        return "OK: ht_resetPlayerPosition_initial"
    return "ERR: ht_resetPlayerPosition_initial"

def test_ht_resetPlayerPosition_scene(
) -> str:
    c = ht_createContext()
    c.goto = {
        "goto1": [700, "some", 30, 40, "yo"]
    }
    c.hasPlayer = True
    c.selectedGoto = "goto1"
    c.recentField = "scene"
    c = ht_resetPlayerPosition(c)
    if (
        c.playerPosition[0] == 40 and
        c.playerPosition[1] == 30
    ):
        return "OK: ht_resetPlayerPosition_scene"
    return "ERR: ht_resetPlayerPosition_scene"

def test_ht_resetSelectedGoto(
) -> str:
    c = ht_createContext()
    c.goto = {
        "goto1": [700, "some", None, None, "yo"]
    }
    c.selectedItem = "some"
    c.recentField = "selectedItem"
    c = ht_resetSelectedGoto(c)
    if (
        c.selectedGoto == "goto1"
    ):
        return "OK: ht_resetSelectedGoto"
    return "ERR: ht_resetSelectedGoto"

def test_ht_selectComment(
) -> str:
    c = ht_createContext()
    c.comments = {
        "comm1": [700, "some", "yo"],
        "comm2": [700, "another", "wo"],
    }
    c.selectedItem = "some"
    c.recentField = "selectedItem"
    c = ht_selectComment(c)
    if (
        c.selectedComment == "comm1"
    ):
        return "OK: ht_selectComment"
    return "ERR: ht_selectComment"
