def desc_aux_isVisible(
    desc: dict[str, str]
) -> bool:
    if (
        "visible" in desc and
        desc["visible"] == "true"
    ):
        return True
    return False
