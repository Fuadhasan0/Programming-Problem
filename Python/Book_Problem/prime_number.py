def is_prime(n):
       
       if n < 2:
              return False
       
       number = True
       for x in range(2, n):
              if n % x == 0:
                     print(n,"is divisiable by", x)
                     number = False
       return number              
                     
       


while True:
       input_number = int(input("Enter a number(enter 0 to exit)\n~ "))
       if input_number == 0:
              break
       
       prime = is_prime(input_number)
       
       if prime == True:
              print(input_number," is a prime number")
       else:
              print(input_number,"isn't a prime number.")       
     