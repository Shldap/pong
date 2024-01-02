import random

class QLearningAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.q_table = [[0] * action_size for _ in range(state_size)]

    def get_action(self, state, epsilon):
        if random.random() < epsilon:
            # Explore - choose a random action
            action = random.randint(0, self.action_size - 1)
        else:
            # Exploit - choose the best action based on Q-values
            action = max(range(self.action_size), key=lambda x: self.q_table[state][x])
        return action

    def update_q_table(self, state, action, next_state, reward, learning_rate, discount_factor):
        current_q = self.q_table[state][action]
        max_next_q = max(self.q_table[next_state])
        new_q = current_q + learning_rate * (reward + discount_factor * max_next_q - current_q)
        self.q_table[state][action] = new_q
