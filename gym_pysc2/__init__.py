from gym.envs.registration import register


register(
    id='FindAndDefeatZerglings-v0',
    entry_point='gym_pysc2.envs:PySC2Env',
    kwargs={
        'map_name': 'FindAndDefeatZerglings',
        'screen_size': 84,
        'minimap_size': 64,
        'apm': 300,
        'steps_per_episode': 0,
        'visualize': True,
        'realtime': True
    }
)
