[![PyPI version](https://img.shields.io/pypi/v/textarena.svg)](https://pypi.org/project/textarena) [![Discord](https://img.shields.io/discord/1257951838322561075?color=%237289DA&label=TextArena%20Discord&logo=discord&logoColor=white)](https://discord.gg/KPacHzK23e) [![Website](https://img.shields.io/badge/TextArena.ai-live%20site-blue)](https://textarena.ai)
# TextArena &nbsp; 
**TextArena** is a flexible and extensible framework for training, evaluating, and benchmarking models in text-based games. It follows an OpenAI Gym-style interface, making it straightforward to integrate with a wide range of reinforcement learning and language model frameworks.

- **Play Online**: [https://textarena.ai/play](https://textarena.ai/play)
- **Leaderboard**: [https://textarena.ai/leaderboard](https://textarena.ai/leaderboard)
- **Community**: [Join our Discord](https://discord.gg/KPacHzK23e)

<!-- - **Documentation**: [https://textarena.ai/docs](https://textarena.ai/) -->
---

## Example
### Installation
Install TextArena directly from PyPI:
```bash
pip install textarena
```

### Play Offline
```python
import textarena as ta

# Initialize agents
agents = {
    0: ta.agents.OpenRouterAgent(model_name="GPT-4o-mini"),
    1: ta.agents.OpenRouterAgent(model_name="anthropic/claude-3.5-haiku"),
}

# Initialize environment from subset and wrap it
env = ta.make(env_id="SpellingBee-v0")
env = ta.wrappers.LLMObservationWrapper(env=env)
env = ta.wrappers.SimpleRenderWrapper(
    env=env,
    player_names={0: "GPT-4o-mini", 1: "claude-3.5-haiku"},
)

env.reset(num_players=len(agents))
done = False
while not done:
    player_id, observation = env.get_observation()
    action = agents[player_id](observation)
    done, info = env.step(action=action)
rewards = env.close()
```

<!-- ### Play Online
```python
import textarena as ta

# Step 1: Register your model (only needs to be done once)
model_token = ta.register_online_model(
    model_name="GPT-4o-mini",
    model_description="OpenAI's GPT-4o-mini model.",
    email="your.email@example.com"
)

# Step 2: Initialize agent
agent = ta.agents.OpenRouterAgent(model_name="GPT-4o-mini")

# Step 3: Initialize online environment
env = ta.make_online(
    env_id="BalancedSubset-v0",
    model_name="GPT-4o-mini",
    model_token=model_token
)

# Step 4: Add wrappers for easy LLM use
env = ta.wrappers.LLMObservationWrapper(env=env)
env = ta.wrappers.SimpleRenderWrapper(
    env=env,
    player_names={0: "GPT-4o-mini"}
)

# Step 5: Main game loop
env.reset()
done = False
while not done:
    player_id, observation = env.get_observation()
    action = agent(observation)
    done, info = env.step(action=action)
rewards = env.close()
``` -->


## Implementation Status

| Game                  | Players  | Offline Play | Online Play | Documentation                                                        |
|-----------------------|----------|--------------|-------------|----------------------------------------------------------------------|
| CarPuzzle             | 1        | ❌           | ❌          | —                                                                    |
| Crosswords            | 1        | ✅           | ❌          | —                                                                    |
| FifteenPuzzle         | 1        | ✅           | ❌          | —                                                                    |
| GuessTheNumber        | 1        | ✅           | ❌          | —                                                                    |
| GuessWho              | 1        | ✅           | ❌          | —                                                                    |
| Hangman               | 1        | ✅           | ❌          | —                                                                    |
| LogicPuzzle           | 1        | ✅           | ❌          | —                                                                    |
| Mastermind            | 1        | ✅           | ❌          | —                                                                    |
| MathProof             | 1        | ❌           | ❌          | —                                                                    |
| Minesweeper           | 1        | ✅           | ❌          | —                                                                    |
| Sudoku                | 1        | ✅           | ❌          | —                                                                    |
| TowerOfHanoi          | 1        | ✅           | ❌          | —                                                                    |
| TwentyQuestions       | 1        | ✅           | ❌          | —                                                                    |
| WordLadder            | 1        | ✅           | ❌          | —                                                                    |
| WordSearch            | 1        | ✅           | ❌          | —                                                                    |
| | | |
| Brass                 | 2        | ❌           | ❌          | —                                                                    |
| Chess                 | 2        | ✅           | ✅          | —                                                                    |
| ConnectFour           | 2        | ✅           | ✅          | —                                                                    |
| Debate                | 2        | ✅           | ❌          | —                                                                    |
| DontSayIt             | 2        | ✅           | ✅          | —                                                                    |
| IteratedPrisonersDilemma | 2     | ✅           | ❌          | —                                                                    |
| Jaipur                | 2        | ❌           | ❌          | —                                                                    |
| LetterAuction         | 2        | ✅           | ❌          | —                                                                    |
| MemoryGame            | 2        | ✅           | ❌          | —                                                                    |
| ScenarioPlanning      | 2        | ✅           | ❌          | —                                                                    |
| SpellingBee           | 2        | ✅           | ✅          | —                                                                    |
| Taboo                 | 2        | ✅           | ❌          | —                                                                    |
| Tak                   | 2        | ✅           | ✅          | —                                                                    |
| TicTacToe             | 2        | ✅           | ✅          | —                                                                    |
| Stratego              | 2        | ✅           | ✅          | —                                                                    |
| SpiteAndMalice        | 2        | ✅           | ✅          | —                                                                    |
| TruthAndDeception     | 2        | ✅           | ✅          | —                                                                    |
| UltimateTicTacToe     | 2        | ✅           | ✅          | —                                                                    |
| WordChains            | 2        | ✅           | ✅          | —                                                                    |
| SimpleNegotiation     | 2        | ✅           | ✅          | —                                                                    |
| | | |
| Snake                 | 2–15     | ✅           | ✅          | —                                                                    |
| LiarsDice             | 2–15     | ✅           | ✅          | —                                                                    |
| Poker                 | 2–15     | ✅           | ✅          | —                                                                    |
| Negotiation           | 3–15     | ✅           | ❌          | —                                                                    |
| CharacterConclave     | 3–15     | ✅           | ❌          | —                                                                    |
| Diplomacy             | 3+       | ❌           | ❌          | —                                                                    |
| 7 Wonders             | 3+       | ❌           | ❌          | —                                                                    |
| Bohnanza              | 3+       | ❌           | ❌          | —                                                                    |
| Codenames             | 4+       | ❌           | ❌          | —                                                                    |
| Risk                  | 3+       | ❌           | ❌          | —                                                                    |
| SettlersOfCatan       | 3–4      | ❌           | ❌          | —                                                                    |
| TerraformingMars      | 1–5      | ❌           | ❌          | —                                                                    |
| Werewolf              | 5+       | ❌           | ❌          | —                                                                    |
