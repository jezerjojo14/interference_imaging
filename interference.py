from matplotlib import pyplot as plt
import numpy as np
import math
D=50
max_k=0
sources=[]

def point_generate(A, k, phi, r0):
    global sources
    global max_k
    if k>max_k:
        max_k=k
    sources+=[lambda r, t: np.multiply(np.divide(A, np.linalg.norm(np.subtract(r, r0))), math.cos(k*(np.linalg.norm(np.subtract(r, r0)) - t + phi)))]



def draw(N, IMG_SIZE=32):

    r=N*0.7/(2*math.pi)
    for i in range(N):
        point_generate([1,0,0], 50, 0, [(IMG_SIZE/2.0)+r*math.cos(i*2*math.pi/N),(IMG_SIZE/2.0)+r*math.sin(i*2*math.pi/N),0])


    image_matrix=[[0 for _ in range(IMG_SIZE)] for _ in range(IMG_SIZE)]

    for x in range(IMG_SIZE):
        for y in range(IMG_SIZE):
            for t in np.arange(0, 6.0/max_k, 0.2/max_k):
                a=0
                for U in sources:
                    a+=U([x,y,D], t)
                if (np.linalg.norm(a)**2)>image_matrix[y][x]:
                    image_matrix[y][x]=np.linalg.norm(a)**2
                # if abs(np.linalg.norm(a))>max_pixel:
                #     max_pixel=abs(np.linalg.norm(a))**2


    plt.imshow(image_matrix, interpolation='nearest')
    plt.show()

N=int(input("Input N: "))
S=int(input("Input screen size (Default - 32): ") or "32")
draw(N, S)
