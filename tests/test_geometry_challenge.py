import pytest
from src.geometry_challenge import calculate_length_r, calculate_alpha_degrees
from data.simplified_geometry import n as n_simple, g as g_simple, i as i_simple, j as j_simple, k as k_simple, s as s_simple, TEST_CASES as SIMPLE_TEST_CASES
from data.real_world_geometry import n as n_real, g as g_real, i as i_real, j as j_real, k as k_real, s as s_real, TEST_CASES as REAL_TEST_CASES


@pytest.mark.parametrize("alpha_degrees,expected_r", SIMPLE_TEST_CASES)
def test_calculate_length_r_simple(alpha_degrees, expected_r):
    calculated_r = calculate_length_r(alpha_degrees, n_simple, g_simple, i_simple, j_simple, k_simple, s_simple)
    assert round(calculated_r, 2) == expected_r, \
        f"Failed for alpha={alpha_degrees}°: expected r={expected_r}, got {round(calculated_r, 2)}"

@pytest.mark.parametrize("alpha_degrees,expected_r", REAL_TEST_CASES)
def test_calculate_length_r_real(alpha_degrees, expected_r):
    calculated_r = calculate_length_r(alpha_degrees, n_real, g_real, i_real, j_real, k_real, s_real)
    assert round(calculated_r, 2) == expected_r, \
        f"Failed for alpha={alpha_degrees}°: expected r={expected_r}, got {round(calculated_r, 2)}"

@pytest.mark.parametrize("expected_alpha,r", SIMPLE_TEST_CASES)
def test_calculate_alpha_degrees_simple(expected_alpha, r):
   calculated_alpha = calculate_alpha_degrees(r, n_simple, g_simple, i_simple, j_simple, k_simple, s_simple)
   assert round(calculated_alpha, 2) == expected_alpha, \
       f"Failed for r={r}: expected alpha={expected_alpha}°, got {round(calculated_alpha, 2)}"

@pytest.mark.parametrize("expected_alpha,r", REAL_TEST_CASES)
def test_calculate_alpha_degrees_real(expected_alpha, r):
    calculated_alpha = calculate_alpha_degrees(r, n_real, g_real, i_real, j_real, k_real, s_real)
    assert round(calculated_alpha, 2) == expected_alpha, \
        f"Failed for r={r}: expected alpha={expected_alpha}°, got {round(calculated_alpha, 2)}"
