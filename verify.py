import sys
L=open(sys.argv[1]).read().split("\n"); n,m,K=map(int,L[0].split()); a=open(sys.argv[2]).read().strip()
if len(a)!=n or not set(a)<=set("01"): sys.exit(1)
for l in L[1:m+1]:
    if not any((int(x)>0)==(a[abs(int(x))-1]=="1") for x in l.split()): sys.exit(1)
print("VERIFIED")
