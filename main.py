#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime

import gym
import gym_pysc2
from absl import app, flags
from pysc2.agents import base_agent
from pysc2.lib import actions

flags.DEFINE_boolean('realtime', default=True,
                     help='')

FLAGS = flags.FLAGS


class Agent(base_agent.BaseAgent):
    def step(self, obs):
        super(Agent, self).step(obs)
        return actions.FUNCTIONS.no_op()


def main(_):
    agent = Agent()
    env = gym.make('FindAndDefeatZerglings-v0', realtime=FLAGS.realtime)

    agent.setup(env.observation_spec(), env.action_spec())

    for _ in range(3):
        timestep = env.reset()
        agent.reset()

        try:
            while True:
                step_actions = [agent.step(timestep[0])]
                if timestep[0].last():
                    break

                print(f'[{datetime.now().isoformat()}] timestep: {type(timestep[0])}')
                timestep = env.step(step_actions)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    app.run(main)
