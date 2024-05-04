#Problem 5
#Min positive number that is evenly divisible by all of the numbers from 1-20

def minPos(n):
    st = n
    while True:
        divisible = True
        for i in range(1,21):
            if n % i != 0:
                divisible = False
                break
        if divisible:
            return n
        n+=1

print(minPos(2))

    #if st <= 7:
        #st += 1
        #minPos(st)
    #else:
        #return st

           
        
    #if n < 2550 and not ok:
        #minPos(st + 1)
    #elif n > 2550 and not ok:
        #return "awww shucks"
    #else:
        #return st



