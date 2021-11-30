me = {'name': 'sagar', 'age':36}

import pickle

F = open('pickle.pickle', 'wb')
pickle.dump(me, F)

F = open('pickle.pickle', 'rb')
E = pickle.load(F)

print(E['age'])