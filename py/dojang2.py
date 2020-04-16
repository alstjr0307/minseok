import pickle

a= ['1', '2']
b= ('a', 'bd')
c= {1,2,3}
with open('test.p', 'wb') as file:
    pickle.dump(a,file)
    pickle.dump(b,file)
    pickle.dump(c, file)
