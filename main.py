import json,os,sys
from urllib.request import*
sys.setrecursionlimit(9000)
EU=os.environ["MAKEFUN_ENV_URL"]
def po(p,d):return json.load(urlopen(Request(EU+p,json.dumps(d).encode(),{"content-type":"application/json"})))
PC=" PNBRQKpnbrqk"
SQ=[s for s in range(21,99)if 0<s%10<9]
KN=(-21,-19,-12,-8,8,12,19,21)
BD=(-11,-9,9,11)
RD=(-10,-1,1,10)
DI=(0,0,KN,BD,RD,BD+RD,BD+RD)
V=(0,100,320,330,500,900,0)
PW=(0,0,1,1,2,4,0)
CR={95:12,25:3,98:14,91:13,28:11,21:7}
PA=(0,0,4,8,14,24,40,0)
PF=(0,0,0,10,15,10,5,0)
KH=(20,25,10,0,0,10,25,20)
MG=[[0]*120 for _ in range(13)]
EG=[[0]*120 for _ in range(13)]
for s in SQ:
 q,f=divmod(s-21,10)
 for u in(0,6):
  r=7-q if u<1 else q
  c=min(f,7-f)+min(r,7-r)
  for t in range(1,7):
   g=e=(0,6*c-20,4*c-8,(15 if r==6 else 0)+(5 if r<1 and 2<f<5 else 0),2*c-6,0)[t-1]
   if t==1:g=PA[r]+(PF[r]if 2<f<5 else 0);e=g+9*r
   if t==6:g=KH[f]if r<1 else max(-50,-15*r);e=8*c-24
   w=1 if u<1 else-1
   MG[t+u][s]=w*(V[t]+g);EG[t+u][s]=w*(V[t]+e)
def n2(a):return(56-ord(a[1]))*10+ord(a[0])-76
def pm(a):return(n2(a[:2]),n2(a[2:4]),"nbrq".index(a[4])+2 if len(a)>4 else 0)
def se(fen):
 p=fen.split();b=bytearray(b'\r'*125);i=0
 for s in SQ:b[s]=0
 for c in p[0]:
  if c=='/':continue
  if c<'9':i+=int(c)
  else:b[SQ[i]]=PC.index(c);i+=1
 b[-5]=0 if p[1]=='w'else 6
 b[-4]=sum((k in p[2])<<j for j,k in enumerate("KQkq"))
 b[-3]=0 if p[3]=='-'else n2(p[3])
 b[-2]=b.index(6,21);b[-1]=b.index(12,21)
 return b
def at(b,s,y):
 for d in KN:
  if b[s+d]==y+2:return 1
 p=9 if y<1 else-11
 if b[s+p]==y+1 or b[s+p+2]==y+1:return 1
 for d in BD:
  t=s+d;q=b[t]
  if q==y+6:return 1
  while not q:t+=d;q=b[t]
  if q==y+3 or q==y+5:return 1
 for d in RD:
  t=s+d;q=b[t]
  if q==y+6:return 1
  while not q:t+=d;q=b[t]
  if q==y+4 or q==y+5:return 1
 return 0
def mk(b,f,t,r,g,e,h):
 n=b[:];u=b[-5];p=n[f];q=n[t]
 n[f]=0;n[-5]=6-u;n[-3]=0;n[-4]=b[-4]&CR.get(f,15)&CR.get(t,15)
 if q:g-=MG[q][t];e-=EG[q][t];h-=PW[(q-1)%6+1]
 if p==u+1:
  if t==b[-3]:
   z=t+10 if u<1 else t-10;y=n[z];g-=MG[y][z];e-=EG[y][z];n[z]=0
  elif abs(t-f)==20:n[-3]=(f+t)//2
  if r:p=u+r;h+=PW[r]
 elif p==u+6:
  n[-2 if u<1 else-1]=t
  if abs(t-f)==2:
   a,c=(f+3,f+1)if t>f else(f-4,f-1)
   y=n[a];n[a]=0;n[c]=y;g+=MG[y][c]-MG[y][a];e+=EG[y][c]-EG[y][a]
 n[t]=p;o=b[f]
 return n,g+MG[p][t]-MG[o][f],e+EG[p][t]-EG[o][f],h
H={}
def gn(b,o=0):
 u=b[-5];y=6-u;x=b[-3];m=[];A=m.append;G=H.get;w=-10 if u<1 else 10;z=2 if u<1 else 9
 for f in SQ:
  p=b[f]
  if not u<p<=u+6:continue
  k=p-u
  if k==1:
   for c in(w-1,w+1):
    t=f+c;q=b[t]
    if y<q<=y+6 or x and t==x:
     s=5999+V[(q-1)%6+1 if q else 1]
     if t//10==z:A((s+3000,f,t,5))
     else:A((s,f,t,0))
   t=f+w
   if not b[t]:
    if t//10==z:A((9000,f,t,5))
    elif not o:
     A((G(p*120+t,0),f,t,0));v=t+w
     if f//10==(8 if u<1 else 3)and not b[v]:A((G(p*120+v,0),f,v,0))
  else:
   for d in DI[k]:
    t=f+d
    while 1:
     q=b[t]
     if q==13 or u<q<=u+6:break
     if q:A((6000+V[(q-1)%6+1]-k,f,t,0));break
     if not o:A((G(p*120+t,0),f,t,0))
     if k<3 or k>5:break
     t+=d
 if not o and b[-4]:
  i=b[-2 if u<1 else-1];C=b[-4]>>(0 if u<1 else 2)
  if C&1 and not(b[i+1]or b[i+2]or at(b,i,y)or at(b,i+1,y)):A((200,i,i+2,0))
  if C&2 and not(b[i-1]or b[i-2]or b[i-3]or at(b,i,y)or at(b,i-1,y)):A((200,i,i-2,0))
 m.sort(reverse=True)
 return m
TT={};RP=set();KL=[0]*72;ND=[0];CAP=[0]
def qs(b,al,be,g,e,h,y):
 ND[0]+=1
 if ND[0]>CAP[0]:raise ArithmeticError
 v=(g*h+e*(24-h))//24;u=b[-5]
 if u:v=-v
 if y>58:return v
 t=6-u;j=-2 if u<1 else-1;ic=at(b,b[j],t);bs=-99999
 if not ic:
  if v>=be:return v
  if v>al:al=v
  bs=v
 for s,f,d,r in gn(b,not ic):
  nb,ng,ne,nh=mk(b,f,d,r,g,e,h)
  if at(nb,nb[j],t):continue
  sc=-qs(nb,-be,-al,ng,ne,nh,y+1)
  if sc>bs:bs=sc
  if sc>=be:return sc
  if sc>al:al=sc
 if ic and bs<-90000:return y-30000
 return bs
def sr(b,d,al,be,g,e,h,y):
 if d<1 or y>58:return qs(b,al,be,g,e,h,y)
 ND[0]+=1
 if ND[0]>CAP[0]:raise ArithmeticError
 kk=bytes(b)
 if y and kk in RP:return 0
 u=b[-5];t=6-u;j=-2 if u<1 else-1;ic=at(b,b[j],t);tm=0;en=TT.get(kk)
 if en:
  ed,es,ef,tm=en
  if ed>=d and abs(es)<9000 and(not ef or ef<0 and es<=al or ef>0 and es>=be):return es
 if d>2 and h>3 and not ic and be<9000:
  nb=b[:];nb[-5]=t;nb[-3]=0
  if-sr(nb,d-3,-be,1-be,g,e,h,y+1)>=be:return be
 if y:RP.add(kk)
 m=gn(b)
 for q in(KL[y],tm):
  if q:
   for i,x in enumerate(m):
    if x[1:]==q:m.insert(0,m.pop(i));break
 bs=-99999;bm=0;a0=al;n=0;nd=d-1+ic
 for s,f,dd,r in m:
  nb,ng,ne,nh=mk(b,f,dd,r,g,e,h)
  if at(nb,nb[j],t):continue
  n+=1
  if n>3 and nd>1 and s<1600 and not ic:
   sc=-sr(nb,nd-1,-al-1,-al,ng,ne,nh,y+1)
   if sc>al:sc=-sr(nb,nd,-be,-al,ng,ne,nh,y+1)
  else:sc=-sr(nb,nd,-be,-al,ng,ne,nh,y+1)
  if sc>bs:bs=sc;bm=(f,dd,r)
  if sc>al:al=sc
  if al>=be:
   if s<1600:KL[y]=(f,dd,r);i=b[f]*120+dd;H[i]=H.get(i,0)+d*d
   break
 if y:RP.discard(kk)
 if not n:return y-30000 if ic else 0
 TT[kk]=(d,bs,0 if a0<bs<be else-1 if bs<=a0 else 1,bm)
 return bs
def best(G):
 b=se(G["fen"]);g=e=h=0
 for s in SQ:
  p=b[s]
  if p:g+=MG[p][s];e+=EG[p][s];h+=PW[(p-1)%6+1]
 TT.clear();RP.clear();KL[:]=[0]*72;ND[0]=0;CAP[0]=18000
 c=se(G["start_fen"])
 for a in G["moves"]:RP.add(bytes(c));c=mk(c,*pm(a),0,0,0)[0]
 RP.add(bytes(c))
 rm=[pm(a)+(a,)for a in sorted(G["legal_moves"])]
 bu=rm[0][3]
 for d in range(1,40):
  try:
   al=-99999;sc=[]
   for f,t,r,a in rm:
    nb,ng,ne,nh=mk(b,f,t,r,g,e,h)
    v=-sr(nb,d-1,-99999,-al,ng,ne,nh,1)
    sc.append((v,a,f,t,r))
    if v>al:al=v
   sc.sort(reverse=True);bu=sc[0][1];rm=[(x[2],x[3],x[4],x[1])for x in sc]
  except ArithmeticError:break
  if ND[0]*3>CAP[0] or abs(sc[0][0])>29000:break
 return bu
while 1:
 G=po("/game",{})
 if G["status"]=="done":break
 while G["status"]=="your_move":G=po("/move",{"game":G["game"],"move":best(G)})
 print(G["game"],G.get("outcome"),G.get("reason"),file=sys.stderr)
