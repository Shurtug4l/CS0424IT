import matplotlib.pyplot as plt

# Redraw the graphs with different colors for execution time and waiting time

# First graph - Monotasking
fig, ax = plt.subplots(figsize=(10,6))
ax.barh('P1', 3, color='green', label='Esecuzione')
ax.barh('P1', 2, left=3, color='red', label='Attesa')
ax.barh('P1', 1, left=5, color='green')
ax.barh('P2', 2, left=6, color='green')
ax.barh('P2', 1, left=8, color='red')
ax.barh('P3', 1, left=9, color='green')
ax.barh('P4', 4, left=10, color='green')
ax.barh('P4', 1, left=14, color='red')

ax.set_xlabel('Tempo [s]')
ax.set_ylabel('Processo')
ax.set_xlim(0, 15)
ax.set_title('Monotasking')
ax.legend()

plt.show()

# Second graph - Multitasking
fig, ax = plt.subplots(figsize=(10,6))
ax.barh('P1', 3, color='green', label='Esecuzione')
ax.barh('P1', 2, left=3, color='red', label='Attesa')
ax.barh('P1', 1, left=5, color='green')
ax.barh('P2', 2, left=3, color='green')
ax.barh('P2', 1, left=5, color='red')
ax.barh('P3', 1, left=6, color='green')
ax.barh('P4', 4, left=7, color='green')
ax.barh('P4', 1, left=11, color='red')

ax.set_xlabel('Tempo [s]')
ax.set_ylabel('Processo')
ax.set_xlim(0, 15)
ax.set_title('Multitasking')
ax.legend()

plt.show()

# Third graph - Time sharing
fig, ax = plt.subplots(figsize=(10,6))
ax.barh('P1', 1, color='green', label='Esecuzione')
ax.barh('P1', 1, left=4, color='green')
ax.barh('P1', 1, left=7, color='green')
ax.barh('P1', 1, left=10, color='green')
ax.barh('P2', 1, left=1, color='green')
ax.barh('P2', 1, left=5, color='green')
ax.barh('P3', 1, left=2, color='green')
ax.barh('P4', 1, left=3, color='green')
ax.barh('P4', 1, left=6, color='green')
ax.barh('P4', 2, left=8, color='green')


ax.set_xlabel('Tempo [s]')
ax.set_ylabel('Processo')
ax.set_xlim(0, 15)
ax.set_title('Time sharing (quantum 1s)')
ax.legend()

plt.show()
