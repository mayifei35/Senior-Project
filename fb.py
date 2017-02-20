from ple.games.flappybird import FlappyBird
from ple import PLE
import numpy as np
import time
class NaiveAgent():
    """
            This is our naive agent. It picks actions at random!
    """

    def __init__(self, actions):
        self.actions = actions

    def pickAction(self, reward, obs):
        #return self.actions[np.random.randint(0, len(self.actions))]
        time.sleep(0.2)
	if self.shouldFlap()==True:
		return 119
	else:
		return None
    
    #def reward():
        #considering distance from each pipe???

    def shouldFlap(self):
	state = game.getGameState() 
	next_pipe_top_y = state["next_pipe_top_y"]
	player_pos_y = state["player_y"] + 30 
	next_pipe_bottom_y = state["next_pipe_bottom_y"] 
	player_v = state["player_vel"] 
	#next_pipe_top_x = state["next_pipe] 
	pipe_gap = next_pipe_bottom_y - next_pipe_top_y 
	#distance = state["next_pipe_dist_to_pipe"] 
	#if distance > -5: #if next_pipe_bottom_y > player_pos_y:
 	# if next_pipe_top_y < player_pos_y: 
	#make flap power weaker 
	#take player velocity into account to see if it would hit the pipe 
	if next_pipe_top_y < player_pos_y: 
		if next_pipe_bottom_y < player_pos_y + 5:
	 		return True 
	return False


game = FlappyBird()
p = PLE(game, fps=30, display_screen=True)
agent = NaiveAgent(p.getActionSet())
nb_frames=1500000 

p.init()
reward = 0.0

for i in range(nb_frames):
   if p.game_over():
           p.reset_game()

   observation = p.getScreenRGB()
   #print observation
   action = agent.pickAction(reward, observation)
   reward = p.act(action)
   #print reward


