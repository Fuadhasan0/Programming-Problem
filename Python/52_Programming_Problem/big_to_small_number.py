"""
Problem is~
    
    Firstly, input who much number run this code. And then print number 1000 to 1 and 5 number in 1 line with single tap gap between two number
"""

for i in range(1000, 0, -1):
    if i % 5 == 0:
        print()
    print(i, end="\t")
