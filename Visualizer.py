import matplotlib.pyplot as plt
import numpy as np


def show_radar_graph(feature_list: dict):

    categories = feature_list.keys()
    values = list(feature_list.values())
    N = len(categories)

    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([20,40,60,80,100], ["20", "40", "60", "80", "100"], color="grey", size=7)
    plt.ylim(0, 100)

    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)
    plt.show()
