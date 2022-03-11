# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def odsetki(windxxx,lombard,należne):
    import json
    from datetime import datetime, date
    s=[]
    karne_odsetki=0
    with open(windxxx+'.json') as p:
         d= json.load(p)
         u=[]
         with open(lombard+'.txt') as r:
             for line in r:
                 z=[]
                 a=line.strip().split('\t')
                 z.append(datetime.strptime(a[0],'%Y-%m-%d'))
                 z.append(float(a[1][:-1])/100)
                 u.append(z)
    s=[]
    for i in d:
        (numer_sprawy, nazwa, termin, kwota, tel)=i
        b=(numer_sprawy, nazwa, termin, kwota)
        if any(b) == False:
                 continue
        else:
            termin=datetime.strptime(termin,'%Y-%m-%d')
            p=termin
            i=0
            days=0
            for a in u:
                   if termin<a[0]:
                            
                            if i==0: 
                                te = a
                                st=te[1]
                                dkwo=(st/365)*kwota
                                b=te[0]
                                dni=abs((b.date()-date.today()).days)
                                days+=dni
                                ods=dkwo*dni
                                karne_odsetki=karne_odsetki+ods
                                i+=1
                                h=te[0]
                            else:
                                
                                te = a
                                st=te[1]
                                dkwo=(st/365)*kwota
                                b=te[0]
                                dni=abs((b.date()-h.date()).days)
                                days+=dni
                                ods=dkwo*dni
                                karne_odsetki=karne_odsetki+ods
                                h=te[0]
            li=u
            for elem in li:
                if termin>elem[0]:
                    te = elem
                    preelem = li[li.index(elem)-1]
                    b=preelem[0]
                    st=te[1]
                    dkwo=(st/365)*kwota
                    dni=abs((b.date()-p.date()).days)
                    ods=dkwo*dni
                    karne_odsetki=karne_odsetki+ods
                    karne_odsetki=round(karne_odsetki,2)
                    s.append([numer_sprawy, nazwa, termin.strftime('%Y-%m-%d'), kwota,karne_odsetki])
                    karne_odsetki=0
                    break
    for a in s:
        for v in s:
            if v[0]==a[0]:
                if datetime.strptime(v[2],'%Y-%m-%d')>datetime.strptime(a[2],'%Y-%m-%d'):
                    del a
                
    with open('należne.json','w') as g:
        json.dump(s,g)

a=odsetki('wind111', 'lombard', 'należne')
    

 # for i in s_json:
   #   for a in s_json:
        #  if i[0]==a[0]:
          #    if datetime.strptime(i[2],'%Y-%m-%d')>datetime.strptime(a[2],'%Y-%m-%d'):
            #      q.append(a)