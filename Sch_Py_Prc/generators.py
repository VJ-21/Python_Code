# Generator=Function that behaves like an iterator(it can be used in a for loop)
        #we can use it to pauses a function,returns a value,then resumes Uses 'yield' instead of 'return'
        # Iterator withoutloading everything into memory (example:reading large file)
        # return:contains all values,yield:returns one by one   

# Iterators=An object that enables a programmer to traverse a container particularly listsff

def sq_num(nums):
    for i in nums:
        yield (i*i)

my_nums=sq_num([1,2,3,4,5])
print(my_nums)
for val in my_nums:
    print(val)