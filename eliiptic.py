import matplotlib.pyplot as plt
import random
import numpy
import numbers
import os
import math
def Float2(d):
    ds = str(d);
    d = float(str(ds.replace("]","").replace("[","").replace("-","")));
    return(d);
def randomPoint(a,b):
    y = random.randint(-100,100)
    roots = numpy.roots([1, 0, a, b - y**2])
    roots = [val.real for val in roots if val.imag == 0]
    x = random.choice(roots)
    return [x];
def trapdoor(a,b):
    cs = str(a);
    c = float(str(cs.replace("]","").replace("[","").replace("-","")));
    ds = str(b);
    d = float(str(ds.replace("]","").replace("[","").replace("-","")));
    return(d ** c);
i = 0;
test = [20,30,40];
ii = 0;
rand1 = random.random();
rand2 = random.random();
x = [randomPoint(rand1,rand2),randomPoint(rand1,rand2),randomPoint(rand1,rand2),randomPoint(rand1,rand2)];
y = [randomPoint(rand1,rand2),randomPoint(rand1,rand2),randomPoint(rand1,rand2),randomPoint(rand1,rand2)];
enc = [""] * 100;
enc2 = [""] * 100;
def traploop(enc,x):
    for i in range(0,2):
        if(i > 1):
            enc[i] = (enc[i - 1] + trapdoor(x[i],x[i+1]));
        else:
            enc[i] = trapdoor(x[i],x[i + 1]);
    return(enc);
#print(trapdoor(y[i],x[i]));
traploop(enc,x);
traploop(enc2,y);
plt.plot(x,y);
plt.show(plt.plot(x,y));
input();
os.system("clear");
print("priavte key ",enc[1]);
print("public key ",enc2[1]);
input();
os.system("clear");
