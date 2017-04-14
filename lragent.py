import time
import numpy as np
import sys
import csv
import pygame
from ple.games.flappybird import FlappyBird
from ple import PLE

#Does it make a difference to change the number of action?
#need to do:output data as it goes, go back and update previous predicted rewards,run till plenty is collected, retrain, repeat

game = FlappyBird()
nb_frames = 15000
data=np.genfromtxt('weights2v.csv',delimiter=',',dtype=float)
weights=np.matrix(data[0:6])
bias=data[6]
p = PLE(game, fps=30, display_screen=True)
p.init()
result=0
explore=0.2
alpha=0.6
rfile= open('recordvs45.csv','w') 
writer=csv.writer(rfile,dialect='excel')
reader=csv.reader(rfile,delimiter=',')
print weights
class lrAgent():
    """
           lr picks based on the weights
    """
    def __init__(self, actions):
        self.actions = actions

    def pickAction(self, reward, obs):
        global result, alpha
        if np.random.rand(1)<explore:
            print 'random'
            return self.actions[np.random.randint(0,len(self.actions))]
        else:
 
            state=game.getGameState()
            playerY=state["player_y"]
            #nextTopY=state["next_pipe_top_y"]
            nextBottomY=state["next_pipe_bottom_y"]
            #nextDistance=state["next_pipe_dist_to_player"]
            #nnextTopY=state["next_next_pipe_top_y"]
            nnextBottomY=state["next_next_pipe_bottom_y"]
            #nnextDistance=state["next_next_pipe_dist_to_player"]
            score=state["score"]
       
            flap_state=np.matrix([1,0,result,playerY,nextBottomY,nnextBottomY])
            nflap_state=np.matrix([0,1,result,playerY,nextBottomY,nnextBottomY])
            fu_flap_state=np.matrix([1,0,result+10*np.random.rand(1),playerY-3,nextBottomY,nnextBottomY])
            fu_nflap_state=np.matrix([0,1,result+10*np.random.rand(1),playerY-3,nextBottomY,nnextBottomY])
            fr= np.dot(weights,flap_state.transpose())
            ffr=alpha*((np.dot(weights,fu_flap_state.transpose()))-fr)+fr
            nfr=np.dot(weights,nflap_state.transpose())
            nffr=alpha*((np.dot(weights,fu_nflap_state.transpose()))-nfr)+nfr
            print fr
            #print ffr-nffr
            result+=10
            f_reward=fr+score*1000
            nf_reward=nfr+score*1000
            if fr>=nfr:
                writer.writerow([1,0,f_reward,playerY,nextBottomY,nnextBottomY])
                return 119
            else:
                writer.writerow([0,1,nf_reward,playerY,nextBottomY,nnextBottomY])
                return None
        



agent = lrAgent(p.getActionSet())
reward = 0.0
for i in range(nb_frames):
      
   if p.game_over():
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
