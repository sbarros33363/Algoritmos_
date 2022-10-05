dias=int(input())
años=int()
meses=int()

años=dias//365
meses=(dias%365)//30
dias=(dias%365)%30


print(int(años),"ano(s)")
print(int(meses),"mes(es)")
print(dias,"dia(s)")
