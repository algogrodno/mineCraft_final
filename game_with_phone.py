# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

from pandac.PandaModules import Texture, TextureStage, CardMaker


        
class Game(ShowBase):
   def __init__(self):
       ShowBase.__init__(self)
       self.land = Mapmanager()
       #x,y = self.land.loadLand("land3.txt")
       #self.hero = Hero((x//2,y//2,2),self.land)
       self.land.loadMap()
       self.hero = Hero((5,0,1),self.land)
       base.camLens.setFov(90)

   def backgroundImage(self, image):
        bgTexture = loader.loadTexture(image) # Load the background texture
        
        screenStage = TextureStage('screen')
        screenStage.setMode(TextureStage.MDecal)
        
        screenTexture = Texture()
        buffer = base.win.makeTextureBuffer("screen buffer", base.win.getXSize(), base.win.getYSize(), screenTexture, True)
        bufferCam = base.makeCamera(buffer, lens=base.cam.node().getLens())
        
        cm = CardMaker('screencard')
        cm.setFrameFullscreenQuad()
        cm.setHasUvs(True)
        screenCard = render2d.attachNewNode(cm.generate())
        screenCard.setTexture(bgTexture)
        screenCard.setTexture(screenStage, screenTexture)

game = Game()
game.backgroundImage('fon.jpg')
game.run()
