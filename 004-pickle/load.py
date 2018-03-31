import pickle


with open('./tmp.tmp', 'r') as f:
    b = pickle.load(f)
    print b

