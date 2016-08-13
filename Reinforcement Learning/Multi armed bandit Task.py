'''
10 armed bandit testbed:

A single bandit consists of an arm that needs to be picked in order to gain a
certain reward and in turn a certain true value. The idea is to maximize the
final true value for that bandit.

Over 1000 tries:
1. Initialize each q value to normal distributed random value using np.random.normal
2. select the best bandit to check value
3. if value is less than epsilon, explore to select another random bandit, else
   select best bandit
4. update q value using faster method, as seen in update function
5. accumulate reward

'''
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import math

class EpsilonGreedy:

    def __init__(self, epsilon, rewards):
        self.epsilon = epsilon
        self.rewards = rewards# reward  behind each door
        self.counts = np.zeros(len(rewards))  # count of arm picked up during sampling
        self.q_values = np.zeros(len(rewards)) # action value assigned to each arm
        

    def action_taken_greedy(self,reward_current):
        '''
        This function returns the best bandit action taken by gaussian normal probability (i.e. selecting the
        highest rewarding bandit) and the reward for that bandit
        '''
        if reward_current>(1-self.epsilon):
            return random.randint(len(self.q_values))
        else:
            return np.argmax(self.q_values)
        

    def action_taken_softmax(self):
        '''
        This function returns the best bandit action taken by softmax probability distribution(i.e. selecting the
        highest rewarding bandit) and the reward for that bandit

        to be improved.

        Prevents denominator overflow by logarithmic method
        '''
        tau=0.00001
        values=self.q_values.tolist()
        m=max(self.q_values/tau)
        den_exponential_values=np.exp((self.q_values/tau)-m)
        denominator=m+math.log1p(sum(den_exponential_values))
        prob = [((i/tau)-denominator) for i  in values]
        prob=np.exp(prob)
        if sum(prob)<=0.5:
            prob=[i*2 for i in prob]
        temp=random.uniform(0,1)
        cumulative=0.0
        for item,item_probability in zip(self.q_values,prob):
            cumulative += item_probability
            if temp < cumulative: break
        return values.index(item)
        
    def update(self,action,current_reward):
        '''
            updation function, self.q_values converges over trials to reward
            value
        '''
        self.q_values[action]=self.q_values[action]+(current_reward-self.q_values[action])/(1+self.counts[action])
        self.counts[action]+=1
        return(self.q_values)

    def perform_trial(self,runs):
        final_reward_accumulation=np.zeros(runs)
        for i in range(0,runs):
            bandit_no=self.action_taken_greedy(random.rand())
            reward_current_here=self.rewards[bandit_no]+random.normal(0,1,1)
            final_q=self.update(bandit_no,reward_current_here)
            final_reward_accumulation[i]=reward_current_here
        return(final_reward_accumulation)    

    def perform_trial_softmax(self,runs):
        final_reward_accumulation=np.zeros(runs)
        for i in range(0,runs):
            bandit_no=self.action_taken_softmax()
            reward_current_here=self.rewards[bandit_no]+random.normal(0,1,1)
            final_q=self.update(bandit_no,reward_current_here)
            final_reward_accumulation[i]=reward_current_here
        return(final_reward_accumulation)

            

final_reward_values_ep1=np.zeros(1000)
final_reward_values_ep2=np.zeros(1000)
final_reward_values_ep3=np.zeros(1000)
final_reward_values_ep4=np.zeros(1000)
print ('averaging over 2000 plays of 10 bandits, each play has 1000 trials')
for i in range(1,2000):
    q_starx=random.normal(0,1,1)
    q=random.normal(q_starx,1,10)
    q=np.squeeze(q)
    
    ep1=EpsilonGreedy(0, q)
    final_reward_values_ep1+=ep1.perform_trial(1000)

    
    ep2=EpsilonGreedy(0.01, q)
    final_reward_values_ep2+=ep2.perform_trial(1000)
    
    ep3=EpsilonGreedy(0.1, q)
    final_reward_values_ep3+=ep3.perform_trial(1000)

    ep4=EpsilonGreedy(0,q)
    final_reward_values_ep4+=ep4.perform_trial_softmax(1000)

    print('iteration: %d')%i
    
plt.plot(final_reward_values_ep1/2000, c='r', label='epsilon=0')
plt.plot(final_reward_values_ep2/2000, c='b', label='epsilon=0.01')
plt.plot(final_reward_values_ep3/2000, c='g', label='epsilon=0.1')
plt.plot(final_reward_values_ep4/2000, c='y', label='Softmax tau=0.00001')
plt.xlabel('Plays')
plt.ylabel('Average Reward')
plt.legend(loc=4)
plt.xlim(-25, 1000)

plt.show()

        
        
        
        
        
        
        
