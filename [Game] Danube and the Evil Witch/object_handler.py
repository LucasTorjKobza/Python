from sprite_object import *
from npc import *
from random import choices, randrange
import time

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

      # spawn npc
        self.enemies = 20  # npc count
        self.npc_types = [SoldierNPC, CacoDemonNPC, CyberDemonNPC]
        self.weights = [70, 20, 10]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        #self.spawn_npc()

        #Sprite map
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'statue.png', pos=(8.5, 13.5), scale=1.5, shift=-0.1))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'statue.png', pos=(11.5, 13.5), scale=1.5, shift=-0.1))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'Knight.png', pos=(12.5, 15.5), scale=1, shift=0.100))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'Knight.png', pos=(6.5, 21.5), scale=1, shift=0.100))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'Knight.png', pos=(12.5, 21.5), scale=1, shift=0.100))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'Knight.png', pos=(18.5, 14.5), scale=1, shift=0.100))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'dracula.png', pos=(6.5, 95.5), scale=1, shift=0.150))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'dracula.png', pos=(18.5, 95.5), scale=0.8, shift=0.150))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'dracula.png', pos=(6.5, 86.5), scale=0.8, shift=0.150))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'dracula.png', pos=(18.5, 86.5), scale=0.8, shift=0.150))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'statue_2.png', pos=(9.5, 32.5), scale=0.6, shift=0.300))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'statue_2.png', pos=(14.5, 32.5), scale=0.6, shift=0.300))
        #add_sprite(SpriteObject(game))
        #add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(11.5, 75.5)))
        add_sprite(AnimatedSprite(game, pos=(11.5, 76.5)))
        add_sprite(AnimatedSprite(game, pos=(11.5, 77.5)))
        add_sprite(AnimatedSprite(game, pos=(11.5, 78.75)))
        add_sprite(AnimatedSprite(game, pos=(13.5, 75.75)))
        add_sprite(AnimatedSprite(game, pos=(13.5, 76.75)))
        add_sprite(AnimatedSprite(game, pos=(13.5, 77.75)))
        add_sprite(AnimatedSprite(game, pos=(13.5, 78.75)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(11.5, 79.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(11.5, 80.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(11.5, 81.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(11.5, 82.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(13.5, 79.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(13.5, 80.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(13.5, 81.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(13.5, 82.5)))

        #NPC map
        add_npc(SoldierNPC(game, pos=(17.5, 17.5)))
        add_npc(SoldierNPC(game, pos=(17.5, 16.5)))
        add_npc(SoldierNPC(game, pos=(7.5, 23.5)))
        add_npc(SoldierNPC(game, pos=(7.5, 22.5)))
        add_npc(SoldierNPC(game, pos=(17.5, 32.5)))
        add_npc(SoldierNPC(game, pos=(10.5, 32.5)))
        add_npc(SoldierNPC(game, pos=(11.5, 32.5)))
        add_npc(SoldierNPC(game, pos=(12.5, 32.5)))
        add_npc(SoldierNPC(game, pos=(13.5, 32.5)))
        add_npc(SoldierNPC(game, pos=(10.5, 39.5)))
        add_npc(SoldierNPC(game, pos=(10.5, 40.5)))
        add_npc(SoldierNPC(game, pos=(6.5, 48.5)))
        add_npc(SoldierNPC(game, pos=(9.5, 48.5)))
        add_npc(SoldierNPC(game, pos=(7.5, 60.5)))
        add_npc(SoldierNPC(game, pos=(8.5, 57.5)))
        add_npc(SoldierNPC(game, pos=(11.5, 62.5)))
        add_npc(SoldierNPC(game, pos=(17.5, 57.5)))
        add_npc(SoldierNPC(game, pos=(2.5, 70.5)))
        add_npc(SoldierNPC(game, pos=(3.5, 70.5)))
        add_npc(SoldierNPC(game, pos=(11.5, 70.5)))
        add_npc(SoldierNPC(game, pos=(12.5, 70.5)))
        add_npc(SoldierNPC(game, pos=(11.5, 69.5)))
        add_npc(SoldierNPC(game, pos=(12.5, 69.5)))
        add_npc(CacoDemonNPC(game, pos=(13.5, 41.5)))
        add_npc(CacoDemonNPC(game, pos=(13.5, 41.5)))
        add_npc(CacoDemonNPC(game, pos=(14.5, 44.5)))
        add_npc(CacoDemonNPC(game, pos=(13.5, 44.5)))
        add_npc(CacoDemonNPC(game, pos=(15.5, 41.5)))
        add_npc(CacoDemonNPC(game, pos=(18.5, 23.5)))
        add_npc(CacoDemonNPC(game, pos=(12.5, 29.5)))
        add_npc(CacoDemonNPC(game, pos=(11.5, 29.5)))
        add_npc(CacoDemonNPC(game, pos=(15.5, 50.5)))
        add_npc(CacoDemonNPC(game, pos=(12.5, 59.5)))
        add_npc(CacoDemonNPC(game, pos=(13.5, 59.5)))
        add_npc(CacoDemonNPC(game, pos=(9.5, 65.5)))
        add_npc(CacoDemonNPC(game, pos=(1.5, 73.5)))
        add_npc(CacoDemonNPC(game, pos=(4.5, 73.5)))
        add_npc(CyberDemonNPC(game, pos=(12.5, 93.5)))

    #def spawn_npc(self):
    #    for i in range(self.enemies):
    #            npc = choices(self.npc_types, self.weights)[0]
    #            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
    #            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
    #                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
    #            self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))
       
    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
         
    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(4000)
            self.game.new_game()