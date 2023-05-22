import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.npc_pain_soldier = pg.mixer.Sound(self.path + 'npc_pain_soldier.wav')
        self.npc_pain_caco_demon = pg.mixer.Sound(self.path + 'npc_pain_caco_demon.mp3')
        self.npc_pain_cyber_demon = pg.mixer.Sound(self.path + 'npc_pain_cyber_demon.mp3')
        self.npc_death_soldier = pg.mixer.Sound(self.path + 'npc_death_soldier.mp3')
        self.npc_death_caco_demon = pg.mixer.Sound(self.path + 'npc_death_caco_demon.mp3')
        self.npc_death_cyber_demon = pg.mixer.Sound(self.path + 'npc_death_cyber_demon.mp3')
        self.npc_shot_soldier = pg.mixer.Sound(self.path + 'npc_attack_soldier.wav')
        self.npc_shot_caco_demon = pg.mixer.Sound(self.path + 'npc_attack_caco_demon.wav')
        self.npc_shot_cyber_demon = pg.mixer.Sound(self.path + 'npc_attack_cyber_demon.wav')
        self.laugh = pg.mixer.Sound(self.path + 'laugh.mp3')
        self.npc_shot_soldier.set_volume(0.4)
        self.npc_shot_caco_demon.set_volume(0.8)
        self.npc_shot_cyber_demon.set_volume(0.4)
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
        pg.mixer.music.set_volume(0.2)