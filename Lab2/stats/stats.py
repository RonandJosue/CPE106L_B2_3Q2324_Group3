def median(x):
    
        x.sort()
        n = len(x)
        if n % 2 == 0:
          return (x[n//2-1] + x[n//2]) / 2  # Calculate the median for even number of elements
        else:
            return x[n//2]  
        
def mode(x):
    y = []
    a = [0] * len(x)  
    for i in x:  
            if i not in y:  
                y.append(int(i)) 
    print("output 1: ", y)

    for i in x:  
            for z in y:  
                if i == z:  
                    a[y.index(int(z))] += 1  

    print("output 2: ", a)
    b=max(a)

    return y[a.index(b)]
def mean(x):
     n= len(x)
     total=0
     for i in x:
          total = total + i
     return total/n
