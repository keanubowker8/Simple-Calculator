from calculator import add, multiply

def test_add():
	assert add(0,0) == 0
	assert add(-1,-1) == -2
	assert add(4,5) == 9	
	assert add(2,3,3)
	
def test_multiply():
    assert multiply(1,2)
    assert multiply(1,2,3,4)	