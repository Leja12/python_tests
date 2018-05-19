import function
import pytest

@pytest.mark.parametrize("abc_input, check_abc",
									[(72,'abc'),
									(0,'abc'),
									(1,'abc'),
									(2,'abc'),
									(10,'abc'),
									(100,'abc')])
									
def test_abc_random_string(abc_input,check_abc):
	abc_result = function.abc_random_string(abc_input)	
	print('print abc_result: ', abc_result)

# checking first 3 letters of new string
	abc_result_2 = abc_result[0:3] #0:3 = abc
	print('print abc_result_2: ', abc_result_2)
	assert abc_result_2 == check_abc

#	checking if new string is longer than abc
	assert len(abc_result) > len(check_abc)




