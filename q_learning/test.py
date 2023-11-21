import gym
import numpy as np
import matplotlib.pyplot as plt

# Function to visualize the Q-table updates during training
def visualize_q_table(Q, num_episodes):
    for episode in range(1, num_episodes + 1):
        plt.clf()
        plt.imshow(Q, cmap="cool", interpolation="none")
        plt.title(f"Episode: {episode}")
        plt.colorbar()
        plt.pause(0.1)
    plt.show()

# Function to run Q-learning on FrozenLake environment
def q_learning(env, num_episodes=1000, learning_rate=0.1, discount_factor=0.9, exploration_prob=1.0, exploration_decay=0.995):
    # Initialize Q-table with zeros
    Q = np.zeros([env.observation_space.n, env.action_space.n])

    # Lists to store rewards and exploration rates for visualization
    rewards = []
    exploration_rates = []

    for episode in range(num_episodes):
        state = env.reset()
        total_reward = 0

        while True:
            # Exploration-exploitation trade-off
            if np.random.rand() < exploration_prob:
                action = env.action_space.sample()  # Explore
            else:
                action = np.argmax(Q[state, :])  # Exploit

            print("=====")
            # Take the chosen action and observe the next state and reward
            print(env.step(action))
            next_state, reward, done, _ , _ = env.step(action)

            # Update Q-table using the Q-learning formula
            Q[(state, action)] = Q[(state, action)] + learning_rate * (
                    reward + discount_factor * np.max(Q[next_state]) - Q[(state, action)])

            total_reward += reward
            state = next_state

            if done:
                break

        # Decay exploration rate
        exploration_prob = exploration_prob * exploration_decay

        # Store rewards and exploration rates for visualization
        rewards.append(total_reward)
        exploration_rates.append(exploration_prob)

    # Visualize Q-table updates
    visualize_q_table(Q, num_episodes)

    return Q, rewards, exploration_rates

# Create FrozenLake environment
env = gym.make('FrozenLake-v1')

# Run Q-learning
Q, rewards, exploration_rates = q_learning(env, num_episodes=1000)

# Plot rewards and exploration rates
plt.plot(rewards)
plt.title('Rewards over Episodes')
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.show()

plt.plot(exploration_rates)
plt.title('Exploration Rate over Episodes')
plt.xlabel('Episode')
plt.ylabel('Exploration Rate')
plt.show()
