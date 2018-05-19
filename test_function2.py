import function
import pytest

@pytest.mark.parametrize("number_input, expected_prime",
									[(11,True),
									(10,False),
									(101,True),
									(100, False),
									(10177, True),
									(27277, True),
									(27278, False),
									(10399, True),
									(-10, False)])

def test_is_prime(number_input, expected_prime):
	result = function.is_prime(number_input)
	assert result == expected_prime 
