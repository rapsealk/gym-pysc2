#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gym
from pysc2.env import sc2_env
from pysc2.lib import features


class PySC2Env(gym.Env):

    def __init__(self, map_name, screen_size=84, minimap_size=64,
                 apm=300, steps_per_episode=0,
                 visualize=True, realtime=True):
        players = [sc2_env.Agent(sc2_env.Race.terran),
                   sc2_env.Bot(sc2_env.Race.zerg, sc2_env.Difficulty.very_easy)]
        interface = features.AgentInterfaceFormat(
            feature_dimensions=features.Dimensions(
                screen=screen_size, minimap=minimap_size),
            use_feature_units=True)

        apm = int(apm / 18.5)

        self._env = sc2_env.SC2Env(map_name=map_name,
                                   players=players,
                                   agent_interface_format=interface,
                                   step_mul=apm,
                                   game_steps_per_episode=steps_per_episode,
                                   visualize=visualize,
                                   realtime=realtime)


    def step(self, action):
        return self._env.step(action)

    def reset(self):
        return self._env.reset()

    def render(self):
        pass

    def close(self):
        pass

    def observation_spec(self):
        return self._env.observation_spec()

    def action_spec(self):
        return self._env.action_spec()

    @property
    def env(self):
        return self._env


if __name__ == "__main__":
    pass
