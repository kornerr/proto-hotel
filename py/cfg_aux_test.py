from cfg_aux import *

def test_cfg_aux_staticSpriteName(
) -> str:
    section = f"static \"s-floor1\""
    name = cfg_aux_staticSpriteName(section)
    if (
        name == "s-floor1"
    ):
        return "OK: cfg_aux_staticSpriteName"
    return "ERR: cfg_aux_staticSpriteName"

def test_cfg_aux_textureName(
) -> str:
    section = f"texture \"t-floor1\""
    tex = cfg_aux_textureName(section)
    if (
        tex == "t-floor1"
    ):
        return "OK: cfg_aux_textureName"
    return "ERR: cfg_aux_textureName"

def test_cfg_aux_tree(
) -> str:
    lines = [
        "[abc]",
        "width = 100",
        "wrongSep=another",
        "[def]",
        "anotherWrongSep -> whatever",
        "title = yo",
        "subtitle = whoa",
    ]
    tree = cfg_aux_tree(lines)
    if (
        cld_len(tree) == 2 and
        cld_len(tree["abc"]) == 1 and
        cld_len(tree["def"]) == 2
    ):
        return "OK: cfg_aux_tree"
    return "ERR: cfg_aux_tree"

def test_cfg_aux_treeCreateSection(
) -> str:
    tree: dict[str, dict[str, str]] = {}
    line = "[abc]"
    sectionName = cfg_aux_treeCreateSection(tree, line)
    if (
        sectionName == "abc" and
        cld_len(tree) == 1
    ):
        return "OK: cfg_aux_treeCreateSection"
    return "ERR: cfg_aux_treeCreateSection"

def test_cfg_aux_treeSetKeyValue(
) -> str:
    tree: dict[str, dict[str, str]] = {}
    line = "[abc]"
    sectionName = cfg_aux_treeCreateSection(tree, line)
    line = "title = wazup"
    cfg_aux_treeSetKeyValue(tree, sectionName, line)
    if (
        cld_len(tree[sectionName]) == 1 and
        tree[sectionName]["title"] == "wazup"
    ):
        return "OK: cfg_aux_treeSetKeyValue"
    return "ERR: cfg_aux_treeSetKeyValue"
