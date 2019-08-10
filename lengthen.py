def lengthen(stri, x):
x = "stockjobbingsis"

str = "forest"

if len(str) < len(x):
	u = len(x)/len(str)
	e = str*u

	print e + str[0:len(x)-len(e)]
if len(str) > len(x):
	u =  len(str)/len(x)
	e = x * u
	print e + x[0:len(str)-len(e)]

print lengthen("ingenius", "forest")
print lengthen("clap", "skipping")
print lengthen("abcdefg", "ab")
