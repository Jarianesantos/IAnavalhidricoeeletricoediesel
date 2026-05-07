import gymnasium as gym
import numpy as np

from stable_baselines3 import PPO

# ============================
# Ambiente Naval
# ============================
class NavalEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.action_space = gym.spaces.Box(
            low=0,
            high=1,
            shape=(1,)
        )

        self.observation_space = gym.spaces.Box(
            low=0,
            high=500,
            shape=(2,)
        )

    def reset(self, seed=None, options=None):
        self.soc = 60
        self.demanda = 250

        return np.array([self.soc, self.demanda]), {}

    def step(self, action):

        uso_bateria = action[0]

        diesel = self.demanda * (1 - uso_bateria)
        bateria = self.demanda * uso_bateria

        # função custo
        custo = diesel + 0.2 * bateria**2

        recompensa = -custo

        # atualização simples
        self.soc -= uso_bateria * 5

        done = self.soc <= 10

        obs = np.array([self.soc, self.demanda])

        return obs, recompensa, done, False, {}

# ============================
# Treinamento PPO
# ============================
env = NavalEnv()

model = PPO(
    "MlpPolicy",
    env,
    verbose=1
)

model.learn(total_timesteps=10000)

model.save("models/ppo_naval")