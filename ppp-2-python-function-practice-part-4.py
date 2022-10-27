#Write a Python function called max_num()to find the maximum of three numbers.
def max_num( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_num( x, max_num( y, z ) )
print(max_of_three(3, 6, -5))

#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(mult_list((8, 2, 3, 4, 7)))

#Write a Python function called rev_string() to reverse a string.
def rev_string(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(rev_string('qazwsxedc'))

#Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(num_within(1000))
print(num_within(900))
print(num_within(800))   
print(num_within(2200))

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal(5) 