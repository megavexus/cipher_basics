import math

alfa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(alfa)):
    for j in range(len(alfa[i::]+alfa[i::])):
        print alfa[j]
        
    print '\n'