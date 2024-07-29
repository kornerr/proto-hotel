from gm_aux import *

def test_gm_aux_lockedDoorComment(
) -> str:
    comm = gm_aux_lockedDoorComment("door-1")
    if (
        comm == "comment-door-1-locked"
    ):
        return "OK: gm_aux_lockedDoorComment"
    return "ERR: gm_aux_lockedDoorComment"
