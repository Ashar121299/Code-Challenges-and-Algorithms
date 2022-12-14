# Write here the code challenge solution
from collections import defaultdict
def findRepeatedword(s):
	
	word_count = defaultdict(lambda: 0)

	
	for i in s.split():
		word_count[i] += 1
		if word_count[i] > 1:
			return i
	return 'No Repetition'



if __name__ == "__main__":
    str="I am learning programming at ASAC."
    print(findRepeatedword(str))