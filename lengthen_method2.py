def lengthen(stri, x):
	if len(stri) > len(x):
		longer = stri
		shorter = x
	else:
		longer = x
		shorter = stri

	return shorter * (len(longer)//len(shorter)) + shorter[0:len(longer)%len(shorter)]


print lengthen("ingenius", "forest")
print lengthen("clap", "skipping")
print lengthen("abcdefg", "ab")