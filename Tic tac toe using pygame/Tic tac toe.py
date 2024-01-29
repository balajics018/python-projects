import pygame as pg 
import sys
from random import randint

win_size=600
cell_size=win_size //3
INF=float('inf')
vec2=pg.math.Vector2
CELL_CENTER=vec2(cell_size / 2)

class TicTacToe:
    def __init__(self,game):
        self.game=game
        self.fieldimage = self.get_scaled_image(path='field.png',res=[win_size]*2)
        self.O_image = self.get_scaled_image(path='o.png',res=[cell_size]*2)
        self.X_image = self.get_scaled_image(path='x.png',res=[cell_size]*2)
        
        self.gamearray=[[INF,INF,INF],
                        [INF,INF,INF],
                        [INF,INF,INF]]
        self.player=randint(0,1)
        self.line_indices_array= [ [(0, 0), (0, 1), (0, 2)],
                                   [(1, 0), (1, 1), (1, 2)],
                                   [(2, 0), (2, 1), (2, 2)],
                                   [(0, 0), (1, 0), (2, 0)],
                                   [(0, 1), (1, 1), (2, 1)],
                                   [(0, 2), (1, 2), (2, 2)],
                                   [(0, 0), (1, 1), (2, 2)],
                                   [(0, 2), (1, 1), (2, 0)]]
        self.winner = None
        self.game_steps=0
        self.font=pg.font.SysFont('Courier',cell_size//4,True)
        
    def checkwinner(self):
        for line_indices in self.line_indices_array:
            sum_line=sum([self.gamearray[i][j] for i, j in line_indices])
            if sum_line in {0,3}:
                self.winner='XO'[sum_line==0]
                self.winner_line=[vec2(line_indices[0][::-1])*cell_size+CELL_CENTER,
                                  vec2(line_indices[2][::-1])*cell_size+CELL_CENTER]
    
    def rungameprocess(self):
        current_cell=vec2(pg.mouse.get_pos())//cell_size
        col,row=map(int,current_cell)
        left_click=pg.mouse.get_pressed()[0]
        
        if left_click and self.gamearray[row][col]==INF and not self.winner:
            self.gamearray[row][col]=self.player
            self.player=not self.player
            self.game_steps+=1
            self.checkwinner()
            
    def draw_objects(self):
        for y,row in enumerate(self.gamearray):
            for x,obj in enumerate(row):
                if obj !=INF:
                    self.game.screen.blit(self.X_image if obj else self.O_image,vec2(x,y)*cell_size)
    
    def draw_winner(self):
        if self.winner:
            pg.draw.line(self.game.screen,'red',*self.winner_line,cell_size//8)
            label=self.font.render(f'player"{self.winner}" wins!',True,'white','black')
            self.game.screen.blit(label,(win_size//2-label.get_width()//2,win_size//4))
    
    def draw(self):
        self.game.screen.blit(self.fieldimage,(0,0))
        self.draw_objects()
        self.draw_winner()
        
    @staticmethod
    def get_scaled_image(path,res):
        img=pg.image.load(path)
        return pg.transform.smoothscale(img,res)
    
    def print_caption(self):
        pg.display.set_caption(f'Player"{"OX"[self.player]}"turn!')
        if self.winner:
            pg.display.set_caption(f'player"{self.winner}"Wins! Press Space to Restart')
        elif self.game_steps==9:
            pg.display.set_caption(f'Game Over! Press space to Restart')
            
    def run(self):
        self.print_caption()
        self.draw()
        self.rungameprocess()
        
class Game:
    def __init__(self):
         pg.init()
         self.screen=pg.display.set_mode([win_size]*2)
         self.clock=pg.time.Clock()
         self.tic_tac_toe=TicTacToe(self)
            
    def new_game(self):
        self.tic_tac_toe=TicTacToe(self)
            
    def check_events(self):
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_SPACE:
                    self.new_game()
                        
    def run(self):
        while True:
            self.tic_tac_toe.run()
            self.check_events()
            pg.display.update()
            self.clock.tick(60)
                
if __name__ == '__main__':
    game = Game()
    game.run()
    
       
            
            
            
        
                         
        