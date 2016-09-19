__author__ = 'Adam'
import numpy as np

def parameter_learning_train_1(parent,child):
    parent_uniq=np.unique(parent)
    child_uniq=np.unique(child)
    parent_size=parent_uniq.size
    child_size=child_uniq.size

    # buat cpd polos / make plain cpd table 
    cpd=np.zeros((parent_size*child_size,3))
    tmp=0
    for p in parent_uniq:
        for c in child_uniq:
            cpd[tmp][0]=p
            cpd[tmp][1]=c
            tmp+=1

    # isi cpd / fill the cpd table 
    print("isi cpd")
    for c in cpd:
        temp2=0
        temp=list(((parent[:]==c[0]) & (child[:]==c[1])))
        temp2=temp.count(True)+1
        c[2]=temp2

    # copy matrix
    cpd_mdl=cpd
    tmp_zeros=np.zeros((cpd.shape[0],1))
    cpd_mdl=np.concatenate((cpd_mdl, tmp_zeros), axis=1)

    # isi probability / fill the probability to cpd 
    temp=len(child_uniq)
    temp2=max(child)
    for c in range(len(cpd_mdl)):
        jum=0
        if(cpd_mdl[c,1]==temp2):
            jum=sum(cpd_mdl[c-(temp-1):c+1,2])
            cpd_mdl[c-(temp-1):c+1,3]=jum


    cpd[:,2]=cpd[:,2]/cpd_mdl[:,3]

    return cpd,cpd_mdl
	
# example code with ess =1 	, data with csv document
data=np.loadtxt('data.csv',int,delimiter=',');
parent=data[:,-1]
child=data[:,0]	
h_v,m_h_v=parameter_learning_train_1(parent,child)
print("h_v")
print(h_v) # probability h given by v 

print("m_h_v")
print(m_h_v) # probability h given by v for mdl(scoring funtion purpose)
