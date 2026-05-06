def mode(numbers):
	count = {}
	curr_mode = None
	curr_freq = None

	for i in numbers:
		if i not in count:
			count[i] = 1
		else:
			count[i] += 1

	for key, val in count.items():
		curr_freq = val
		curr_mode = key
		if val > curr_freq:
			curr_freq = val
			curr_mode = key
	return curr_mode



