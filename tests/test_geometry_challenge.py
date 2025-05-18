import pytest
from src.geometry_challenge import calculate_length_r, calculate_alpha_degrees

# Constants from the geometry construction https://www.geogebra.org/classic/nhmywvj7
n = 1.0
g = 8.0
i = 2.0
j = 4.0
k = 1.0
s = 4.0

# Test cases as (alpha_degrees, expected_r) pairs
TEST_CASES = [
    (90.00, 0.00),
    (100.00, 0.29),
    (110.00, 0.80),
    (120.00, 1.50),
    (130.00, 2.33),
    (140.00, 3.25),
    (150.00, 4.19),
    (160.00, 5.05),
    (170.00, 5.78),
    (180.00, 6.35),
]

@pytest.mark.parametrize("alpha_degrees,expected_r", TEST_CASES)
def test_calculate_length_r(alpha_degrees, expected_r):
    calculated_r = calculate_length_r(alpha_degrees, n, g, i, j, k, s)
    assert round(calculated_r, 2) == expected_r, \
        f"Failed for alpha={alpha_degrees}°: expected r={expected_r}, got {round(calculated_r, 2)}"

@pytest.mark.parametrize("expected_alpha,r", TEST_CASES)
def test_calculate_alpha_degrees(expected_alpha, r):
    calculated_alpha = calculate_alpha_degrees(r, n, g, i, j, k, s)
    assert round(calculated_alpha, 2) == expected_alpha, \
        f"Failed for r={r}: expected alpha={expected_alpha}°, got {round(calculated_alpha, 2)}"
