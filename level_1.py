def solution(s):
    # Your code here
    text = s
	result = "" 
	asciicodes = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    braillecodes = ['000000', '100000', '110000', '100100', '100110', '100010', '110100', '110110', '110010', '010100', '010110', '101000', '111000', '101100', '101110', '101010', '111100', '111110', '111010', '011100', '011110', '101001', '111001', '010111', '101101', '101111', '101011']
	for i in range(0, len(text)):
		if text[i].isupper():
			result = result + '000001'
		result = result + braillecodes[asciicodes.index(text[i].lower())]
	print(result)
	return result
