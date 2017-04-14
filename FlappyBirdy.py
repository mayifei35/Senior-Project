import time
import numpy as np
import sys
import csv
import pygame
from ple.games.flappybird import FlappyBird
from ple import PLE
#from ple.games.flappybird._init_ import self.player.height


game = FlappyBird()
nb_frames = 45000
counter = 0
previousState = None
num = 0
top_y = 0
bottom_y = 0

rfile= open('recordws45.csv','w') 
writer=csv.writer(rfile,dialect='excel')
score=0
death_counter=0

p = PLE(game, fps=30, display_screen=True)
p.init()

class HeuAgent():

    """
           Heuristics
    """
    def __init__(self, actions):
        self.actions = actions

       
    def calculateScore(self):
        global score,death_counter
        if death_counter>0:
            score=0
            death_counter=0
        else:
            score+=10
        return score

    def shouldFlap(self):
	global death_counter,previousState, num,top_y,bottom_y

	state = game.getGameState()
	distance = state["next_pipe_dist_to_player"]
	next_pipe_top_y = state["next_pipe_top_y"]
	player_pos_y = state["player_y"] + 30
	next_pipe_bottom_y = state["next_pipe_bottom_y"]
	player_v = state["player_vel"]
	#nxt_pipe_top_x = previousState["next_pipe]
	pipe_gap = next_pipe_bottom_y - next_pipe_top_y

	if (distance == 3.0) or (distance <= 143.0 and distance >= 127.0):  
	   if distance == 3.0: 
	      top_y = next_pipe_top_y
	      bottom_y = next_pipe_bottom_y 
	      if top_y + 5 < player_pos_y:
	         if bottom_y - 8 < player_pos_y:
		    return True
	      return False  
	   else:
	      if top_y + 5 < player_pos_y:
	         if bottom_y - 8 < player_pos_y:
		    return True
	      return False  
	   #previousState = state
            
	else:	
	  if next_pipe_top_y + 5 < player_pos_y:
 	    if next_pipe_bottom_y - 8 < player_pos_y:
               return True

	  return False

    def pickAction(self,reward,observation):
	time.sleep(.15)	
        state = game.getGameState()
        playerY=state["player_y"]
        #nextTopY=state["next_pipe_top_y"]
        nextBottomY=state["next_pipe_bottom_y"]
        #nextDistance=state["next_pipe_dist_to_player"]
        #nnextTopY=state["next_next_pipe_top_y"]
        nnextBottomY=state["next_next_pipe_bottom_y"]
        #nnextDistance=state["next_next_pipe_dist_to_player"]
        score=state["score"]
	if self.shouldFlap() == True:
            result=self.calculateScore()
            f_reward=result+score*1000
            #print f_reward, result,score
            writer.writerow([1,0, f_reward,playerY,nextBottomY,nnextBottomY])
            return 119
	else:
            # action=0
            result=self.calculateScore()
            f_reward=result+score*1000
            writer.writerow([0,1,f_reward,playerY,nextBottomY,nnextBottomY])
            #print f_reward,result,score
            return None


agent = HeuAgent(p.getActionSet())
reward = 0.0

for i in range(nb_frames):
      
   if p.game_over():
       counter+=1
       score=0	
       p.reset_game()
	 
  
	   

   observation = p.getScreenRGB()
   action = agent.pickAction(reward, observation)
   reward = p.act(action)
   state = game.getGameState()
   player_y = state["player_y"]
   distance = state["next_pipe_dist_to_player"]
   pipe_x = state["next_pipe_x"]



pygame.display.quit()

pygame.quit()
sys.exit()
