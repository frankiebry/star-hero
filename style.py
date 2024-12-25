import pygame
from settings import *

class Style():
    """Class for displaying text"""
    def __init__(self,screen,audio):
        super().__init__() # why is this necessary?
        self.screen = screen
        self.small_font = pygame.font.Font('font/Pixeled.ttf',10)
        self.medium_font = pygame.font.Font('font/Pixeled.ttf',20)
        self.large_font = pygame.font.Font('font/Pixeled.ttf',30)
        self.font_color = 'white'

        # Needed to display the volume
        self.audio = audio

        # Volume Bar
        self.volume_bar = pygame.Surface((40,40))
        self.volume_bar.fill((240,240,240))
        self.volume_bar_rect = self.volume_bar.get_rect(center = (400,400))
        self.maximum_volume = 1000
        self.volume_bar_length = 150
        self.volume_bar_ratio = self.maximum_volume / self.volume_bar_length

        # Load image of ship for intro and game over screens
        self.player_ship = pygame.image.load('graphics/player_ship.png').convert_alpha()
        self.player_ship = pygame.transform.rotozoom(self.player_ship,0,0.2)
        self.player_ship_rect = self.player_ship.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

    def display_title(self):
        """# Displays the title on the intro and game over screens"""
        title = self.large_font.render('STAR HERO',False,(self.font_color))
        title_rect = title.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 100))
        self.screen.blit(title,title_rect)

    def display_game_over(self):
        """Displays Game Over message"""
        game_over_message = self.large_font.render('GAME OVER',False,(self.font_color))
        game_over_message_rect = game_over_message.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 100))
        self.screen.blit(game_over_message,game_over_message_rect)

    def display_player_ship(self):
        """Displays the player ship on intro and game over screens"""
        self.screen.blit(self.player_ship,self.player_ship_rect)

    def display_intro_message(self):
        """Displays instructions on how to begin on the intro screen (show controls in this method?)"""
        intro_message = self.medium_font.render('PRESS ENTER TO BEGIN',False,(self.font_color))
        intro_message_rect = intro_message.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 130))
        self.screen.blit(intro_message,intro_message_rect)

    def display_high_score(self,save_data):
        """Displays the high score on the intro and game over screens"""
        self.save_data = save_data

        high_score_message = self.medium_font.render(f'HIGH SCORE: {self.save_data["high_score"]}',False,(self.font_color))
        high_score_message_rect = high_score_message.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 100))
        self.screen.blit(high_score_message,high_score_message_rect)

    def display_in_game_score(self,save_data,score):
        """Displays the high score and current score on the top left during gameplay"""
        self.save_data = save_data
        self.score = score

        high_score_surf = self.small_font.render(f'HIGH SCORE: {self.save_data["high_score"]}',False,self.font_color)
        high_score_rect = high_score_surf.get_rect(topleft = (10,5))
        self.screen.blit(high_score_surf,high_score_rect)

        score_surf = self.medium_font.render(f'SCORE: {self.score}',False,self.font_color)
        score_rect = score_surf.get_rect(topleft = (10,20))
        self.screen.blit(score_surf,score_rect)

    def display_game_over_score(self,score):
        """Displays the player score on the game over screen"""
        self.score = score

        score_message = self.medium_font.render(f'YOUR SCORE: {self.score}',False,(self.font_color))
        score_message_rect = score_message.get_rect(center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 130))
        self.screen.blit(score_message,score_message_rect)

    def display_pause_text(self):
        """Displays the Pause message on pause"""
        pause_text = self.medium_font.render('PAUSED', False, (self.font_color))
        pause_text_rect = pause_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.screen.blit(pause_text,pause_text_rect)

    def display_volume(self):
        """Displays the volume, called when + and - keys are pressed"""

        # Volume Number
        volume_message = self.small_font.render(f'VOLUME: {round(self.audio.master_volume * 10)}',False,(self.font_color))
        volume_message_rect = volume_message.get_rect(bottomleft = (10,SCREEN_HEIGHT - 20))
        self.screen.blit(volume_message,volume_message_rect)
        
        # Volume Bar
        pygame.draw.rect(self.screen,'green',(10,SCREEN_HEIGHT - 20,(self.audio.master_volume*1000)/self.volume_bar_ratio,10))

    def update(self,game_state,save_data,score):
        self.game_state = game_state
        self.save_data = save_data
        self.score = score

        if game_state == 'intro':
            self.display_title()
            self.display_high_score(self.save_data)
            self.display_intro_message()
            self.display_player_ship()
        elif game_state == 'game_active':
            self.display_in_game_score(self.save_data,self.score)
        elif game_state == 'game_over':
            self.display_game_over()
            self.display_high_score(self.save_data)
            self.display_game_over_score(self.score)
            self.display_player_ship()
        elif game_state == 'pause':
            self.display_pause_text()