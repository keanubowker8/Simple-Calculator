from calculator import add, multiply

def test_add():
	'''test to make sure function can add 2 numbers'''
	assert add(0,0) == 0
	assert add(4,5) == 9
	'''test to make sure function can add negative numbers'''
	assert add(-1,-1) == -2	
	'''test to make sure function can add many numbers'''
	assert add(2,3,3)== 8
	
def test_multiply():
	'''test to make sure function can multiply 2 numbers'''
	assert multiply(1,2) == 2
	'''test to make sure function can multiply many numbers'''
	assert multiply(1,2,3,4) == 24	