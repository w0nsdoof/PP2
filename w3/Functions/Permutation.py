
def next_permutation(s:str):
	if len(s) == 0:
		return []

	elif len(s) == 1:
		return [s]

	result = []

	for i in range(len(s)):
		m = s[i]
		res = s[:i] + s[i+1:]

		for p in next_permutation(res):
			result.append(m + p)

	return result

user_input = input()
for p in next_permutation(user_input):
	print(p)


