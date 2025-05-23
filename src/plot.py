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

def plot():
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

    # Plot simplified geometry
    alphas_simple = np.array([case[0] for case in SIMPLE_TEST_CASES])
    r_expected_simple = np.array([case[1] for case in SIMPLE_TEST_CASES])

    # Calculate r values for a continuous range of alpha values
    alpha_range_simple = np.linspace(min(alphas_simple), max(alphas_simple), 100)
    r_calculated_simple = np.array([
        calculate_length_r(alpha, n_simple, g_simple, i_simple, j_simple, k_simple, s_simple)
        for alpha in alpha_range_simple
    ])

    ax1.plot(alpha_range_simple, r_calculated_simple, 'b-', label='Calculated r')
    ax1.scatter(alphas_simple, r_expected_simple, color='red', label='Test cases')
    ax1.set_title('Simplified Geometry')
    ax1.set_xlabel('Alpha (degrees)')
    ax1.set_ylabel('Length r')
    ax1.grid(True)
    ax1.legend()

    # Plot real-world geometry
    alphas_real = np.array([case[0] for case in REAL_TEST_CASES])
    r_expected_real = np.array([case[1] for case in REAL_TEST_CASES])

    # Calculate r values for a continuous range of alpha values
    alpha_range_real = np.linspace(min(alphas_real), max(alphas_real), 100)
    r_calculated_real = np.array([
        calculate_length_r(alpha, n_real, g_real, i_real, j_real, k_real, s_real)
        for alpha in alpha_range_real
    ])

    ax2.plot(alpha_range_real, r_calculated_real, 'b-', label='Calculated r')
    ax2.scatter(alphas_real, r_expected_real, color='red', label='Test cases')
    ax2.set_title('Real-world Geometry')
    ax2.set_xlabel('Alpha (degrees)')
    ax2.set_ylabel('Length r')
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()

    # Ensure tmp directory exists
    os.makedirs('artifacts', exist_ok=True)
    plt.savefig('artifacts/plot.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    plot()
