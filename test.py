#!/usr/bin/env python
#https://github.com/mwydmuch/ViZDoom/blob/master/doc/DoomGame.md (Lots of great information)
from vizdoom import *
import random
import time
import itertools as it
import argparse

#Funtion that returns the proper name of the scenarios in the scenarios directory
#Should probably use cases
def findScenario(s, p):
    ext = '.cfg'
    if (s == 'basic'):
        return p+'basic'+ext
    elif (s == 'cig'): 
        return p+'cig'+ext
    elif (s == 'deadly' or 'deadly_corridor'):
        return p+'deadly_corridor'+ext
    elif (s == 'deathmatch'):
        return p+'deathmatch'+ext
    elif (s == 'defend_center' or s == 'defend_the_center'):
        return p+'defend_the_center'+ext
    elif (s == 'defend_line' or s == 'defend_the_line'):
        return p+'defend_the_line'+ext
    elif (s == 'health_gathering'):
        return p+'health_gathering'+ext
    elif (s == 'health_gathering_supreme'):
        return p+'health_gathering_supreme'+ext
    elif (s == 'learning'):
        return p+'learning'+ext
    elif (s == 'multi'):
        return p+'multi'+ext
    elif (s == 'multi_duel'):
        return p+'multi_duel'+ext
    elif (s == 'my_way_home' or s == 'home'):
        return p+'my_way_home'+ext
    elif (s == 'oblige'):
        return p+'oblige'+ext
    elif (s == 'predict_position'):
        return p+'predict_position'+ext
    elif (s == 'rocket_basic'):
        return p+'rocket_basic'+ext
    elif (s == 'simpler_basic'):
        return p+'simpler_basic'+ext
    elif (s == 'take_cover'):
        return p+'take_cover'+ext
    elif (s == 'test'):
        return p+'test'+ext
    else:
        print('Scenario '+s+' Not Found, Loading basic.cfg')
        return p+'basic'+ext


game = DoomGame()

parser = argparse.ArgumentParser(description = "Something")
parser.add_argument('-scenario','-s', type=str, default = 'basic', help='Doom Scenario')
args = parser.parse_args()
scenario = findScenario(args.scenario, r"scenarios/")

#game.load_config("/vizdoom/scenarios/test.cfg")
game.load_config(scenario)
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