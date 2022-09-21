#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import gym
# instantiate env. () <- select simulator you wanna exec
# env will be a object which has Pendulum-v0 info
env = gym.make("Pendulum-v1")
# initialize the instantiation
env.reset()
for i in range (3):
    # give appropriate sample-action(selected by agent)
    action = env.action_space.sample()
    # against any action, env.step() give a reward/state(next)/done(whether certain conditions are met)
    state, reward, done, info = env.step(action)
    print("action:{}, state:{}, reward:{}".format(action, state, reward))

