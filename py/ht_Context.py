class ht_Context:
    def __init__(self):
        self.cfgContents = []
        self.cfgDir = None
        self.cfgPath = None
        self.cfgTree = {}
        self.comments = {}
        self.delayScene = None
        self.didClickMouse = []
        self.didCreateConfigPlayerSprites = False
        self.didResetSceneItemSprites = False
        self.didResetSceneStaticSprites = False
        self.didLaunch = False
        self.didLoadConfigSounds = False
        self.didLoadConfigTextures = False
        self.goto = {}
        self.hasPlayer = False
        self.hideStaticComment = None
        self.playerPosition = []
        self.recentField = "none"
        self.scene = None
        self.sceneCfgContents = {}
        self.sceneCfgTrees = {}
        self.scenes = {}
        self.selectedComment = None
        self.selectedGoto = None
        self.selectedItem = None
        self.selectedSound = None
        self.soundCfgContents = {}
        self.soundCfgTrees = {}
        self.sounds = {}
        self.windowAntialiasing = False
        self.windowBackgroundColor = "#000000"
        self.windowHeight: float  = 0
        self.windowTitle = ""
        self.windowWidth: float = 0

    def field(self, fieldName):
        return getattr(self, fieldName)

    def setField(self, fieldName, value):
        setattr(self, fieldName, value)

def ht_createContext():
    return ht_Context()
