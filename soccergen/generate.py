import gfootball.env as football_env


def gen_data():
    env = football_env.create_environment(
        env_name="11_vs_11_stochastic",
        stacked=False,
        logdir="/tmp/football",
        write_goal_dumps=False,
        write_full_episode_dumps=False,
        render=False,
    )
    env.reset()
    steps = 0
    states = []
    while True:
        obs, rew, done, info = env.step(env.action_space.sample())
        states.append(env.unwrapped._env.observation())
        steps += 1
        if done:
            break
    return states
