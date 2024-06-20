import pickle
fp = open("picklefile.txt",wb)
cn=["doni","virat","dhavan"]
pickle.dump(cn,fp)
fp.close()


