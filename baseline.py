#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# E. Culurciello
# August 2017
# Ethan was here hehe

from __future__ import division
from __future__ import print_function
from vizdoom import *
import itertools as it
from random import sample, randint, random
from time import time, sleep
import numpy as np
import numpy as np
import skimage.color, skimage.transform
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import os.path
from torchvision import datasets, transforms
from torch.autograd import Variable
from tqdm import trange
import argparse
from load_in_data import default_data

default = default_data()
# Q-learning settings
learning_rate = default.learning_rate
discount_factor = default.discount_factor
epochs = default.epochs
learning_steps_per_epoch = default.learning_steps_per_epoch
replay_memory_size = default.replay_memory_size

# NN learning settings
batch_size = default.batch_size

# Training regime
test_episodes_per_epoch = default.test_episodes_per_epoch

# Other parameters
frame_repeat = default.frame_repeat
resolution = default.resolution
episodes_to_watch = default.episodes_to_watch

model_savefile = default.model_savefile
save_model = default.save_model
load_model = default.load_model
skip_learning = default.skip_learning
skip_evaluation = default.skip_evaluation

folder = False
model_folder = ("model_"+default.scenario+"_epochs_"+str(epochs)+"_index_")
model_savefile = ("model_"+default.scenario+"_epoch_")

rewards_per_episode = []
avg_reward_per_episode = [] #TODO store the average score per episode

# Configuration file path
# config_file_path = "scenarios/nolan_made.cfg"
config_file_path = default.config_file_path
# config_file_path = "../../scenarios/rocket_basic.cfg"

# Converts and down-samples the input image
def preprocess(img):
    img = skimage.transform.resize(img, resolution)
    img = img.astype(np.float32)
    return img


class ReplayMemory:
    def __init__(self, capacity):
        channels = 1
        state_shape = (capacity, channels, resolution[0], resolution[1])
        self.s1 = np.zeros(state_shape, dtype=np.float32)
        self.s2 = np.zeros(state_shape, dtype=np.float32)
        self.a = np.zeros(capacity, dtype=np.int32)
        self.r = np.zeros(capacity, dtype=np.float32)
        self.isterminal = np.zeros(capacity, dtype=np.float32)

        self.capacity = capacity
        self.size = 0
        self.pos = 0

    def add_transition(self, s1, action, s2, isterminal, reward):
        self.s1[self.pos, 0, :, :] = s1
        self.a[self.pos] = action
        if not isterminal:
            self.s2[self.pos, 0, :, :] = s2
        self.isterminal[self.pos] = isterminal
        self.r[self.pos] = reward

        self.pos = (self.pos + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)

    def get_sample(self, sample_size):
        i = sample(range(0, self.size), sample_size)
        return self.s1[i], self.a[i], self.s2[i], self.isterminal[i], self.r[i]


class Net(nn.Module):
    def __init__(self, available_actions_count):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 8, kernel_size=6, stride=3)
        self.conv2 = nn.Conv2d(8, 8, kernel_size=3, stride=2)
        self.fc1 = nn.Linear(192, 128)
        self.fc2 = nn.Linear(128, available_actions_count)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.view(-1, 192)
        x = F.relu(self.fc1(x))
        return self.fc2(x)

criterion = nn.MSELoss()

def createPTH(epoch):
    directory = "models/"+model_folder
    name = model_savefile+str(epoch)+".pth"
    print("Saving Model: "+name)
    os.chdir(directory)
    torch.save(model, name)
    os.chdir("..")
    os.chdir("..")
    print("Directory: "+os.getcwd())

def writeToFile(rewards):
    path = "results/"
    name = "results"
    suf = ".txt"
    files = os.listdir(path)
    count = len(files) -1
    f = open(path + name + str(count)+ '_'+ default.scenario +"_"+ str(epochs) + "Epochs" + suf, "w+")
    print("created new file in results: " + name + str(count) + suf)
    for x in range (0,len(rewards)):
        f.write(str(x) + "," + str(rewards[x])+"\n")
    f.close()
    print("done writing to file")

def learn(s1, target_q):
    s1 = torch.from_numpy(s1)
    target_q = torch.from_numpy(target_q)
    s1, target_q = Variable(s1), Variable(target_q)
    output = model(s1)
    loss = criterion(output, target_q)
    # compute gradient and do SGD step
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    return loss

def get_q_values(state):
    state = torch.from_numpy(state)
    state = Variable(state)
    return model(state)

def get_best_action(state):
    q = get_q_values(state)
    m, index = torch.max(q, 1)
    #index = index.cuda()
    action = index.data.numpy()[0]
    return action


def learn_from_memory():
    """ Learns from a single transition (making use of replay memory).
    s2 is ignored if s2_isterminal """

    # Get a random minibatch from the replay memory and learns from it.
    if memory.size > batch_size:
        s1, a, s2, isterminal, r = memory.get_sample(batch_size)

        q = get_q_values(s2).data.numpy()
        q2 = np.max(q, axis=1)
        target_q = get_q_values(s1).data.numpy()
        # target differs from q only for the selected action. The following means:
        # target_Q(s,a) = r + gamma * max Q(s2,_) if isterminal else r
        target_q[np.arange(target_q.shape[0]), a] = r + discount_factor * (1 - isterminal) * q2
        learn(s1, target_q)


def perform_learning_step(epoch):
    """ Makes an action according to eps-greedy policy, observes the result
    (next state, reward) and learns from the transition"""

    def exploration_rate(epoch):
        """# Define exploration rate change over time"""
        start_eps = 1.0
        end_eps = 0.1
        const_eps_epochs = 0.1 * epochs  # 10% of learning time
        eps_decay_epochs = 0.6 * epochs  # 60% of learning time

        if epoch < const_eps_epochs:
            return start_eps
        elif epoch < eps_decay_epochs:
            # Linear decay
            return start_eps - (epoch - const_eps_epochs) / \
                               (eps_decay_epochs - const_eps_epochs) * (start_eps - end_eps)
        else:
            return end_eps

    s1 = preprocess(game.get_state().screen_buffer)

    # With probability eps make a random action.
    eps = exploration_rate(epoch)
    if random() <= eps:
        a = randint(0, len(actions) - 1)
    else:
        # Choose the best action according to the network.
        s1 = s1.reshape([1, 1, resolution[0], resolution[1]])
        a = get_best_action(s1)
    reward = game.make_action(actions[a], frame_repeat)
    #print(reward)

    isterminal = game.is_episode_finished()
    s2 = preprocess(game.get_state().screen_buffer) if not isterminal else None

    # Remember the transition that was just experienced.
    memory.add_transition(s1, a, s2, isterminal, reward)

    learn_from_memory()


# Creates and initializes ViZDoom environment.
def initialize_vizdoom(config_file_path):
    print("Initializing doom...")
    game = DoomGame()
    game.load_config(config_file_path)
    game.set_window_visible(False)
    game.set_mode(Mode.PLAYER)
    game.set_screen_format(ScreenFormat.GRAY8)
    game.set_screen_resolution(ScreenResolution.RES_640X480)
    game.init()
    print("Doom initialized.")
    return game


if __name__ == '__main__':
    # Create Doom instance
    game = initialize_vizdoom(config_file_path)
    actions_num = game.get_available_buttons_size()
    actions = []
    # Action = which buttons are pressed
    print('Availible Buttons: ',game.get_available_buttons())
    print('Availible Actions: ',actions_num)
  
    for perm in it.product([False, True], repeat=actions_num):
        actions.append(list(perm))

    # Create replay memory which will store the transitions
    memory = ReplayMemory(capacity=replay_memory_size)

    if load_model:
        print("Loading model from: ", model_savefile)
        model = torch.load(model_savefile)
    else:
	    print("Model not loaded")
	    model = Net(len(actions))
    #model = model.to('cuda')
	
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    device = "cpu" #remove line to force GPU
    model = model.to(device)
	
    optimizer = torch.optim.SGD(model.parameters(), learning_rate)

    print("Starting the training!")
    time_start = time()
    if not skip_learning:
        iteration = epochs/4
        files = os.listdir("models/")
        model_folder = model_folder+str(len(files))
        os.mkdir("models/"+model_folder)
        for epoch in range(1, epochs+1):
            print("\nEpoch %d\n-------" % (epoch))
            train_episodes_finished = 0
            train_scores = []

            print("Training...")
            game.new_episode()
            for learning_step in trange(learning_steps_per_epoch, leave=False):
                perform_learning_step(epoch)
                if game.is_episode_finished():
                    score = game.get_total_reward()
                    train_scores.append(score)
                    game.new_episode()
                    train_episodes_finished += 1
            
            print("%d training episodes played." % train_episodes_finished)

            train_scores = np.array(train_scores)

            print("Results: mean: %.1f +/- %.1f," % (train_scores.mean(), train_scores.std()), \
                  "min: %.1f," % train_scores.min(), "max: %.1f," % train_scores.max())
            avg_reward_per_episode.append(train_scores.mean())
            #adds the data from train_scores into global list
            for s in train_scores:
                rewards_per_episode.append(s)

            print("\nTesting...")
            test_episode = []
            test_scores = []
            for test_episode in trange(test_episodes_per_epoch, leave=False):
                game.new_episode()
                while not game.is_episode_finished():
                    state = preprocess(game.get_state().screen_buffer)
                    state = state.reshape([1, 1, resolution[0], resolution[1]])
                    best_action_index = get_best_action(state)

                    game.make_action(actions[best_action_index], frame_repeat)
                r = game.get_total_reward()
                test_scores.append(r)

            test_scores = np.array(test_scores)
            print("Results: mean: %.1f +/- %.1f," % (
                test_scores.mean(), test_scores.std()), "min: %.1f" % test_scores.min(),
                  "max: %.1f" % test_scores.max())

            if epoch % iteration == 0:
                createPTH(epoch)

            print("Saving the network weigths to:", model_savefile)
            #torch.save(model, model_savefile)

            print("Total elapsed time: %.2f minutes" % ((time() - time_start) / 60.0))
    game.close()
    writeToFile(rewards_per_episode)
    print("======================================")
    print("Training finished. It's time to watch!")

    if not skip_evaluation:
        # Reinitialize the game with window visible
        game.set_window_visible(default.game_window_visible)
        game.set_mode(Mode.ASYNC_PLAYER)
        game.init()

        for _ in range(episodes_to_watch):
            game.new_episode()
            while not game.is_episode_finished():
                state = preprocess(game.get_state().screen_buffer)
                state = state.reshape([1, 1, resolution[0], resolution[1]])
                best_action_index = get_best_action(state)

                # Instead of make_action(a, frame_repeat) in order to make the animation smooth
                game.set_action(actions[best_action_index])
                for _ in range(frame_repeat):
                    game.advance_action()

            # Sleep between episodes
            sleep(1.0)
            score = game.get_total_reward()
            print("Total score: ", score)
