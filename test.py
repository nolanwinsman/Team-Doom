#!/usr/bin/env python
#https://github.com/mwydmuch/ViZDoom/blob/master/doc/DoomGame.md (Lots of great information)
from vizdoom import *
import random
import time
import itertools as it

game = DoomGame()
#game.load_config("/vizdoom/scenarios/test.cfg")
game.load_config("scenarios/deadly_corridor.cfg")
game.init()

actions_num = game.get_available_buttons_size()
actions = []
# Action = which buttons are pressed
print('Availible Buttons: ',game.get_available_buttons())
print('Availible Actions: ',actions_num)
for perm in it.product([False, True], repeat=actions_num):
	actions.append(list(perm))

episodes = 10
for i in range(episodes):
    game.new_episode()
    while not game.is_episode_finished():
        state = game.get_state()
        img = state.screen_buffer
        misc = state.game_variables
        reward = game.make_action(random.choice(actions))
        print("\treward:", reward)
        time.sleep(0.02)
    print("Result:", game.get_total_reward())
    time.sleep(2)