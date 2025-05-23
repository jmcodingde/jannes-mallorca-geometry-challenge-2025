"""
Test data for the real-world geometry construction.
Source: https://www.geogebra.org/classic/mq7vyvab
"""

# Constants from the real-world construction
n = 32
g = 507.7
i = 15
j = 210.23
k = 7.6
s = 308.171

# Test cases as (alpha_degrees, expected_r) pairs
TEST_CASES = [
    (105.15, 0),
    (110.00, 8.08),
    (120.00, 31.59),
    (130.00, 63.09),
    (140.00, 100.64),
    (150.00, 141.92),
    (160.00, 184.47),
    (170.00, 225.73),
    (180.00, 263.69),
]
