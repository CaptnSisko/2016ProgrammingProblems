[(lambda g:[(lambda a:g.update({a[0]:a[1:]}))(input().split(' '))for k in range(int(i))]and print('T'if (lambda x:x(input(),x))(lambda n,s:n=='T'if n in 'TF'else s(g[n][0],s)^s(g[n][1],s))else 'F'))({})for i in iter(input,'0')]
print((lambda l:'MAX: {}\nMIN: {}'.format(max(l),min(l)))([int(n)for n in iter(input,'-1')]))
[(lambda t,s:(t.update({s:int((t['AB']**2+t['BC']**2)**.5)})if s=='AC'else t.update({s:int((t['AC']**2-t.get('AB',t.get('BC',0))**2)**.5)}))or print('{}: {}, AREA: {}'.format(s,t[s],t['AB']*t['BC']//2)))({l[0]:int(l[1]),l[2]:int(l[3])},({'AB','AC','BC'}-set(l)).pop())for l in iter(lambda:input().split(' '),['-1'])]
[[print(('^'*k).center(n))for k in range(1,n+2,2)]for n in iter(lambda:2*int(input())-1,-3)]
(lambda w:[w.append(w.pop()+abs(2500-int(c))//100*(-1if int(c)<2500else 1))for c in iter(input,'-1')]and print(w[0]))([int(input())])
[b.remove(0)or (lambda s:print('{}REACHABLE {}'.format('UN'if s%2else '',s)))(sum([sum([n<b[i]for n in b[i:]])for i in range(8)]))for b in iter(lambda:[int(n)for n in input().split(' ')],[-1])]
for b in iter(input,'-1'):print(sum([abs(t[0]%3-t[1]%3)+abs(t[0]//3-t[1]//3)if t[1]else 0for t in enumerate([int(n)for n in b.split(' ')])]))
for b in iter(lambda:input().split(' '),['-1']):(lambda z:[0if z-o<0else print(' '.join(['0'if i==z-o else b[z-o]if i==z else b[i]for i in range(9)]))for o in (3,-1,-3,1)]and print('-'))(b.index('0'))
