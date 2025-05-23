import matplotlib.pyplot as plt
import numpy as np
import os
from src.geometry_challenge import calculate_length_r
from data.simplified_geometry import (
    n as n_simple, g as g_simple, i as i_simple,
    j as j_simple, k as k_simple, s as s_simple,
    TEST_CASES as SIMPLE_TEST_CASES
)
from data.real_world_geometry import (
    n as n_real, g as g_real, i as i_real,
    j as j_real, k as k_real, s as s_real,
    TEST_CASES as REAL_TEST_CASES
)

def plot_geometry(ax, test_cases, n, g, i, j, k, s, title):
    alphas = np.array([case[0] for case in test_cases])
    r_expected = np.array([case[1] for case in test_cases])

    # Calculate r values for a continuous range of alpha values
    alpha_range = np.linspace(min(alphas), max(alphas), 100)
    r_calculated = np.array([
        calculate_length_r(alpha, n, g, i, j, k, s)
        for alpha in alpha_range
    ])

    ax.plot(alpha_range, r_calculated, 'b-', label='Calculated r')
    ax.scatter(alphas, r_expected, color='red', label='Test cases')
    ax.set_title(title)
    ax.set_xlabel('Alpha (degrees)')
    ax.set_ylabel('Length r')
    ax.grid(True)
    ax.legend()

def plot():
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

    # Plot simplified geometry
    plot_geometry(ax1, SIMPLE_TEST_CASES, n_simple, g_simple, i_simple, j_simple, k_simple, s_simple, 'Simplified Geometry')

    # Plot real-world geometry
    plot_geometry(ax2, REAL_TEST_CASES, n_real, g_real, i_real, j_real, k_real, s_real, 'Real-world Geometry')
    plt.tight_layout()

    # Ensure the artifacts directory exists
    os.makedirs('artifacts', exist_ok=True)
    plt.savefig('artifacts/plot.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    plot()
