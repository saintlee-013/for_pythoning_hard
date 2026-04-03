#JibTie and Lami's
import math
w=[]
wg = []
j=[]
jg=[]
jt=[]
t=[]
tg=[]
th=[]
ths =[]
al=[]
als=[]
l1=5
l2=3
g = 9.806
def getvalues():
    if(val == "w"):
        for i in range(l2):
         i = float(input(f"enter weight {i+1} of {l2}\t"))
         w.append(i)
    elif(val == "jib"):
        for i in range(l2):
         i = float(input(f"enter jib force {i+1} of {l2}\t"))
         j.append(i)
    elif(val == "tie"):
        for i in range(l2):
         i = float(input(f"enter tie force {i+1} of {l2}\t"))
         t.append(i)
    elif(val =="theta"):
     for i in range(l2):
       i = int(input(f"enter the theta {i+1} of {l2} \t"))
       th.append(i)
    elif(val == "alpha"):
     for i in range(l2):
       i = int(input(f"enter the alpha {i+1} of {l2} \t"))
       al.append(i)
def multiplybyg():
    if(val == "w"):
        for force in w:
         mult = force*g
         wg.append(round(mult,4))
        print(wg)
    elif(val == "jib"):
        for f in j:
            f = (f*0.2) + f
            jt.append(f)
        for force in jt:
         mult = force*g
         jg.append(round(mult,4))
        print(jg)
    elif(val == "tie"):
        for force in t:
         mult = force*g
         tg.append(round(mult,4))
        print(tg)
    elif(val=="theta"):
        for angle in th:
            sin = math.sin(math.radians(angle))
            ths.append(round(sin,4))
        print(ths)
    elif(val=="alpha"):
        for angle in al:
            sin = math.sin(math.radians(angle))
            als.append(round(sin,4))
        print(als)
for z in range(l1):
 val=input("enter w or jib or tie or theta or alpha\t")
 getvalues()
 multiplybyg()

sum_list=[]
sin_list=[]
for b in range(l2):
    sum_of_angles = th[b] + al[b]
    sum_list.append(sum_of_angles)
    sin_of_angles = math.sin(math.radians(sum_of_angles))
    sin_list.append(round(sin_of_angles,4))
print(f"the sin of theta + alpha is {sin_list}")

ta =[]
fa=[]
for c in range(l2):
    t = (wg[c]*ths[c])/sin_list[c]
    ta.append(round(t,4))
    f = (wg[c]*als[c])/sin_list[c]
    fa.append(round(f,4))
print(f"the analytically calculated value of Tension is: \t{ta}")
print(f"the analytically calculated value of F is: \t{fa}")

sub1 =[]
sub2=[]
for d in range(l2):
    subtracted_values1 = ((math.fabs(ta[d]-tg[d]))/ta[d])*100
    sub1.append(round(subtracted_values1,4))
    subtracted_values2= ((math.fabs(fa[d]-jg[d]))/fa[d])*100
    sub2.append(round(subtracted_values2,4))
print(f"the percentage error in the analyitcal and experimental values of the tension are:\t {sub1}")   
print(f"the percentage error in the analyitcal and experimental values of the f are:\t {sub2}")   

    

