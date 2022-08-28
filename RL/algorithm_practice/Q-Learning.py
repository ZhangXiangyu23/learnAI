import time
import random

# 环境类
class Env():
    def __init__(self, length, height):
        # define the height and length of the map
        self.length = length # 12
        self.height = height # 4
        # define the agent's start position
        self.x = 0
        self.y = 0

    def render(self, frames=50):
        for i in range(self.height):
            if i == 0: # cliff is in the line 0
                # 第0行[S, x, x, x, x, x, x, x, x, x, x, T]
                line = ['S'] + ['x']*(self.length - 2) + ['T'] # 'S':start, 'T':terminal, 'x':the cliff
            else:
                line = ['.'] * self.length
            if self.x == i:
                line[self.y] = 'o' # mark the agent's position as 'o'
            print(''.join(line))
        print('\033['+str(self.height+1)+'A')  # printer go back to top-left
        time.sleep(1.0 / frames)

    def step(self, action):
        # 0:向右    1:向左      2:向上        3:向下
        change = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        # 计算agent移动之后的位置
        self.x = min(self.height - 1, max(0, self.x + change[action][0]))
        self.y = min(self.length - 1, max(0, self.y + change[action][1]))

        # 其实状态就是agent在地图中的位置
        states = [self.x, self.y]
        reward = -1
        terminal = False
        if self.x == 0:  # if agent is on the cliff line "SxxxxxT"
            # 在第0行，而不在起始位置
            if self.y > 0:  # if agent is not on the start position
                # 无论是达到终点，还是摔落悬崖，游戏都终止了！！！
                terminal = True
                # 摔落悬崖了！！
                if self.y != self.length - 1: # if agent falls
                    reward = -100
        return reward, states, terminal
    # 重开游戏，让agent回到起点
    def reset(self):
        self.x = 0
        self.y = 0


class Q_table():
    def __init__(self, length, height, actions=4, alpha=0.1, gamma=0.9):
        # Q表是一维列表
        self.table = [0] * actions * length * height # initialize all Q(s,a) to zero
        self.actions = actions
        self.length = length
        self.height = height
        self.alpha = alpha
        self.gamma = gamma # 折扣因子

    # 在一维Q表中寻找，对应状态下采取特定action的索引
    def _index(self, a, x, y):
        """Return the index of Q([x,y], a) in Q_table."""
        return a * self.height * self.length + x * self.length + y

    def _epsilon(self):
        return 0.1
        # version for better convergence:
        # """At the beginning epsilon is 0.2, after 300 episodes decades to 0.05, and eventually go to 0."""
        # return 20. / (num_episode + 100)

    def take_action(self, x, y, num_episode):
        """epsilon-greedy action selection"""
        # episode的概率进行随机选取动作
        if random.random() < self._epsilon():
            return int(random.random() * 4)
        else:
            actions_value = [self.table[self._index(a, x, y)] for a in range(self.actions)]
            return actions_value.index(max(actions_value))

    def max_q(self, x, y):
        actions_value = [self.table[self._index(a, x, y)] for a in range(self.actions)]
        print(len(self.table))
        print(actions_value)
        print("-" * 50)
        return max(actions_value)

    # 更新Q表
    def update(self, a, s0, s1, r, is_terminated):
        # both s0, s1 have the form [x,y]
        q_predict = self.table[self._index(a, s0[0], s0[1])]
        if not is_terminated:
            q_target = r + self.gamma * self.max_q(s1[0], s1[1])
        else:
            q_target = r
        self.table[self._index(a, s0[0], s0[1])] += self.alpha * (q_target - q_predict)


def cliff_walk():
    # 初始化环境
    env = Env(length=12, height=4)
    # 构造Q表，Q表是一个48 x 4列的矩阵
    table = Q_table(length=12, height=4)
    # 训练3000个episode
    for num_episode in range(3000):
        # within the whole learning process
        episodic_reward = 0
        is_terminated = False
        s0 = [0, 0]
        while not is_terminated:
            # within one episode
            action = table.take_action(s0[0], s0[1], num_episode)
            # 选择了action之后的奖励、状态和是否结束游戏
            r, s1, is_terminated = env.step(action)
            table.update(action, s0, s1, r, is_terminated)
            episodic_reward += r
            # env.render(frames=1)
            s0 = s1
        if num_episode % 20 == 0:
            print("Episode: {}, Score: {}".format(num_episode, episodic_reward))
        env.reset()

if __name__ == "__main__":
    cliff_walk()