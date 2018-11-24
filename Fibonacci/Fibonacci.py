import sys
#top-bottom approach
def fib_tb(n, memo):
	if memo[n] is not None:
		return memo[n]
	if n == 1 or n == 2:
		result = 1
	else:
		result = fib_tb(n-1, memo) + fib_tb(n-2, memo)
	memo[n] = result
	return result

#bottom-up approach
def fib_bu(n):
	if n == 1 or n == 2:
		result = 1
	fib_bu = [None]*(n+1)
	fib_bu[1] = 1
	fib_bu[2] = 1
	for x in range(3,n+1):
		fib_bu[x] = fib_bu[x-1] + fib_bu[x-2]
	return fib_bu[n]

if __name__ == '__main__':
	n = int(sys.argv[1])
	memo = [None]*(n+1)
	res_tb = fib_tb(n, memo)
	res_bu = fib_bu(n)
	print "The top-bottom approach produces:", res_tb, "and the bottom-up approach produces:", res_bu
