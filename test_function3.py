import function
import pytest

@pytest.mark.parametrize("number_input, expected_prime",
									[(59,61),
									(3253,3257),
									(2207,2213),
									(1009,1013),
									(104723,104729 ),
									(86843,86851),
									(57791,57793),
									(29537,29567),
									(0,2),				
									(-10,2)])

def test_print_next_prime(number_input,expected_prime):
	result = function.print_next_prime(number_input)
	assert result == expected_prime 
