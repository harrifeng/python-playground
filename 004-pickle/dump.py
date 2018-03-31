import pickle

a = dict(a=1, b=2,c=3)

with open('./tmp.tmp', 'w') as f:
    pickle.dump(a, f, 0)

print(a)
