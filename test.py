import textarena as ta 

agents = {
    0: ta.agents.HumanAgent(),
    1: ta.agents.OpenRouterAgent(model_name="gpt-4o")
}

# initialize the environment
env = ta.make(env_id="ConnectFour-v0")

env = ta.wrappers.LLMObservationWrapper(env=env)

# reset it
env.reset(num_players=len(agents))


# main game loop
done = False 
while not done:
  player_id, observation = env.get_observation()
  action = agents[player_id](observation)
  done, info = env.step(action=action)
rewards = env.close()
print(rewards)