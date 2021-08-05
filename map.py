lst=[1,2,3,4,5]
def square(num):
	"return square of a number"
	return num*num

m=map(square,lst)
print(list(m))
