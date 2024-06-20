db = dbm.open(" dbm1.db",'r')
for k,v,in db.item()
  print(k,v)