import os
import sys


if len(sys.argv) < 2:
    print("Usage: python3 /path/to/main.py /path/to/ht.config")
    sys.exit(1)

CFG = os.path.realpath(sys.argv[1])
SCRIPT_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

sys.path.append(f"{SCRIPT_DIR}/../cross-language-dialect/ctx")
sys.path.append(f"{SCRIPT_DIR}/../cross-language-dialect/lib")
sys.path.append(f"{SCRIPT_DIR}/py")

import arcade
from cfg import *
from cld import *
from ctx import *
from fs import *
from desktop import *
from desktop_Platform import *
from desktop_Window import *
from ht import *
from ht_Context import *

ctrl = ctx_Controller(ht_createContext())
ctrl.registerFunctions([
    cfg_parseComments,
    cfg_parseConfigTree,
    cfg_parseScenes,
    fs_locateConfigDir,
    fs_readConfig,
    fs_readSceneConfigs,
    ht_selectComment,
])

def printDbg(c):
  print(f"Dbg key/value: '{c.recentField}'/'{c.field(c.recentField)}'")
ctrl.registerCallback(printDbg)

p = desktop_Platform()
p.ctrl = ctrl
p.timer = desktop_Timer()
p.timer.callback = lambda key, value: ctrl.set(key, value)

# Bind platform to context changes.
def process(c):
  # Copy context to platform.
  p.c = c
  # Perform context dependent calls of desktop functions.
  # Similar to context functions, but no platform is returned.
  desktop_applyConfigInit(p)
  #desktop_createConfigItemSprites(p)
  #desktop_createConfigPlayerSprites(p)
  #desktop_createConfigStaticSprites(p)
  desktop_loadConfigTextures(p)
  desktop_movePlayerInstantly(p)
  desktop_printSelectedItem(p)
  desktop_resetCommentVisibility(p)
  desktop_resetSceneStaticSprites(p)
  desktop_selectItem(p)
ctrl.registerCallback(process)

ctrl.set("cfgPath", CFG)
ctrl.set("scriptDir", SCRIPT_DIR)

wnd = desktop_Window(p)
ctrl.set("didLaunch", True)
arcade.run()
