from cProfile import label
from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [0, 2, 2, 2, 5, 2, 2, 2, 0]
player2 = [1, 2, 2, 2, 3, 2, 2, 2, 1]
player3 = [1, 2, 2, 2, 3, 2, 2, 2, 1]

labels = ['Player 1', 'Player 2', 'Player 3']
colors = ['#008fd5', '#fc4f30', '#6d904f']

# plt.pie([1,1,1], labels=["Player 1", "Player 2", "Player 3"])
plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)


# plt.legend(loc="upper left")
plt.legend(loc=(0.07, 0.05))

plt.title("My awaesome Stack Plot")
plt.tight_layout()
plt.show()


# Colors
# Blue: #008fd5 
# Red: #fc4f30 
# Yellow: #e5ae37 
# Green: #6d904f 