# Problem 2
# generate fibonacci sequence up to 4 million, find the sum of the even valued terms
import time 

### ATTEMPT ONE ### Execution time: 0.00012874603271484375 seconds

#st = time.time()
#seq = [] 
#def fib(f1,f2):
#    fn = f1 + f2
#    if (fn < 4000000):
#        seq.append(fn) 
#        fib(f2, fn)
#fib(0,1)

#count = 3
#for x in seq: 
#    print(f"{x} is fibonacci number {count}")
#    count += 1
#et = time.time()
#e_x = et - st
#print(f"Execution time: {e_x} seconds")

### THE REAL ONE ### Execution time: 0.00018262863159179688 seconds
seq = []
def fib(f1,f2):
    fn = f1 + f2
    if (fn < 4000000):
        if (fn % 2 == 0):
            seq.append(fn)
        fib(f2, fn)

fib(0,1)
print(sum(seq))
