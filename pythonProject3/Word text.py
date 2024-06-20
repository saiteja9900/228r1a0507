'''
fp = open (" word.txt","w")
if fp:
    print("sucessfully opened")
    fp.write("i")
    fp.write("a")
    fp.write("")
    fp.close()
'''



n = int(input("Enter no of values"))
  dic = { }
  for i in range(n):
      key = input("Enter key")
      value = input("Enter value")
      dic [key] = value
print(dic)
  print("after invertion")
  print(invert_content(dic))



def invert_convert(dic):
    invert_dic = { }

    invert_dic = { k:v in for v,k dic.line}

    return invertdic

