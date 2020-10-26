import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



'''
N = int(input("Enter number of integers: "))


# Build and randomly shuffle list of integers.
A = [x + 1 for x in range(N)]
random.seed(time.time())
random.shuffle(A)
print(A)
'''
def swap(A, i, j):
    """Helper function to swap elements i and j of list A."""

    if i != j:
        A[i], A[j] = A[j], A[i]

def bubblesort(A):
    """In-place bubble sort."""

    if len(A) == 1:
        return

    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A

A = [x + 1 for x in range(100)]
random.seed(time.time())
random.shuffle(A)
    
generator = bubblesort(A)    


print("Generator:",generator)



fig,ax = plt.subplots()
bar_rects = ax.bar(range(len(A)),A)


def vis(A,rects):

    for rect, val in zip(rects, A):
        rect.set_height(val)

   
    

    
    
    #plt.bar(range(len(A)),A,align = 'edge')

    

anim = animation.FuncAnimation(fig,func=vis,frames = generator,fargs =(bar_rects,), interval=1)
plt.show()