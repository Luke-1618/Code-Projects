import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

rr = np.array([14.1, 17.1, 20.1, 23.1, 26.1]) / 100
ROC = np.array([13.3, 14.3, 15.3, 16.3, 17.3]) / 100
WACC = np.array([5.6, 6.6, 7.6, 8.6, 9.6]) / 100

TerminalCF = 204071
wacc = 9 / 100  # Fixing the WACC value for the plot

basefcff = np.array([177045, 176296, 179109, 175440])

cash = 135876
debt = 278823

# Calculate the terminal value
terminal_value = np.zeros((len(ROC), len(rr)))
for i in range(len(ROC)):
    for j in range(len(rr)):
        result = (TerminalCF * (1 + ROC[i] * rr[j])) / (wacc - ROC[i] * rr[j])
        terminal_value[i, j] = result

E_17 = 1000
shares = 99652711

# Calculate the intrinsic value
intrinsic_value = np.zeros_like(terminal_value)
for i in range(len(ROC)):
    for j in range(len(rr)):
        intrinsic_value[i, j] = ((terminal_value[i, j] + TerminalCF) / (1 + wacc) ** 5 + np.sum(basefcff) + debt + cash) * E_17 / shares

# Create a meshgrid of rr and ROC
RR, ROC = np.meshgrid(rr, ROC)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the wireframe
surf = ax.plot_surface(RR, ROC, intrinsic_value, cmap='viridis', alpha=0.8)

# Set labels and title
ax.set_xlabel('RR', fontsize=12, fontweight='bold', color='black')
ax.set_ylabel('ROC', fontsize=12, fontweight='bold', color='black')
ax.set_zlabel('Intrinsic Value', fontsize=12, fontweight='bold', color='black')
ax.set_title('3D Plot of Intrinsic Value with Terminal WACC 7.62% \n Red<34.62')

# Add labels for intrinsic value with conditional formatting
for i in range(len(ROC)):
    for j in range(len(RR)):
        label_color = 'green' if intrinsic_value[i, j] > 34.62 else 'red'
        ax.text(RR[i, j], ROC[i, j], intrinsic_value[i, j], '{:.2f}'.format(intrinsic_value[i, j]), color=label_color)

plt.show()
