#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime

import gym
import gym_pysc2
from absl import app, flags
from pysc2.agents import base_agent
from pysc2.lib import actions, units

flags.DEFINE_boolean('realtime', default=True,
                     help='')

FLAGS = flags.FLAGS


class Agent(base_agent.BaseAgent):
    def step(self, obs):
        super(Agent, self).step(obs)
        return actions.FUNCTIONS.no_op()


class MarineGroupAgent(base_agent.BaseAgent):
    def step(self, observation):
        super(MarineGroupAgent, self).step(observation)
        marines = [unit for unit in observation.observation.feature_units \
                   if unit.unit_type == units.Terran.Marine]
        # print('Marines:', marines, end=' ')
        if not marines:
            return actions.FUNCTIONS.no_op()
        marine = marines[0]
        print('marine:', marine.unit_type, marine.health, (marine.x, marine.y))
        # if self._unit_type_is_selected(observation, units.Terran.Marine):
        #     print('selected: True')
        #     return actions.FUNCTIONS.no_op()
        # else:
        #     print('selected: False')
        return actions.FUNCTIONS.select_point('select', (marine.x, marine.y))

    def _unit_type_is_selected(self, observation, unit_type):
        if len(observation.observation.single_select) > 0 \
           and observation.observation.single_select[0].unit_type == unit_type:
            return True
        elif len(observation.observation.multi_select) > 0 \
             and observation.observation.multi_select[0].unit_type == unit_type:
            return True
        return False


def main(_):
    agent = MarineGroupAgent()  # Agent()
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

                timestep_ = timestep[0]

                print(f'[{datetime.now().isoformat()}] r: {timestep_.reward}, discount: {timestep_.discount}')
                # print(f'[{datetime.now().isoformat()}] obs: {timestep_.observation}')
                timestep = env.step(step_actions)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    app.run(main)
