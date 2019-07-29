import g2p
#그냥 두 단어의 Subsequence 길이를 구한다

import openpyxl

from openpyxl import Workbook

wb = openpyxl.load_workbook('검증셋.xlsx')
ws = wb.active
#write_wb = Workbook()

#write_ws = write_wb.active

vowels = ['ii','ee','qq','aa','xx','vv','uu','oo','ye','yq','ya','yv','yu','yo','wi','wo','wq','we','wa','wv','xi']
consonants = ['p0','ph','pp','t0','th','tt','k0','kh','kk','s0,','ss','h0','c0','mm','nn','rr','pf','ph','tf','th','kf','kh','s0','ss','h0','c0','mf','nf','ng','ll','ks','nc','nh','lk','lm','lt','lp','lh','ps']

v1 = ['ee','qq', 'ye', 'yq', 'wq','wo', 'we', 'xi'] #ㅔ 계열 모음
v2 = ['ii','wi'] #ㅣ 계열 모음
v3 = ['aa', 'ya', 'wa'] # ㅏ 계열 모음
v4 = ['uu', 'yu'] # ㅜ 계열 모음
v5 = ['vv', 'oo', 'yv', 'wv'] #ㅓ계열 모음

c1 = ['p0', 'ph', 'pp'] # ㅂ 계열 자음
c2 = ['t0', 'th', 'tt'] # ㄷ 계열 자음
c3 = ['k0', 'kh', 'kk'] # ㄱ 계열 자음
c4 = ['s0', 'ss'] # ㅅ 계열 자음
c5 = ['c0', 'ch', 'cc'] # ㅈ 계열 자음

def vowelconvt(vow1): #모음을 해당 그룹의 대표 모음으로 치환하는 함수
    length = len(vow1)
    for i in range(length):
        if v1.count(vow1[i])==1: vow1[i]='ee'
        if v2.count(vow1[i])==1: vow1[i]='ii'
        if v3.count(vow1[i])==1: vow1[i]='aa'
        if v4.count(vow1[i])==1: vow1[i]='uu'
        if v5.count(vow1[i])==1: vow1[i]='vv'
    return vow1

def conconvt(con1):
    length = len(con1)
    for i in range(length):
        if c1.count(con1[i])==1: con1[i]='p0'
        if c2.count(con1[i])==1: con1[i]='t0'
        if c3.count(con1[i])==1: con1[i]='k0'
        if c4.count(con1[i])==1: con1[i]='s0'
        if c5.count(con1[i])==1: con1[i]='c0'
    return con1

def vowel(word1): #단어 음절에서 모음만 빼서 모으는 함
    length = len(word1)
    w1v = []
    for i in range(length):
        if vowels.count(word1[i])!=0:
            w1v.append(word1[i])
    return w1v

def consonant(word1): #단어 음절에서 자음만 빼서 모으는 함수
    length = len(word1)
    w1c = []
    for i in range(length):
        if consonants.count(word1[i])!=0:
            w1c.append(word1[i])
    return w1c

def lcs_length(a, b):
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i, ca in enumerate(a, 1):
        for j, cb in enumerate(b, 1):
            table[i][j] = (
                table[i - 1][j - 1] + 1 if ca == cb else
                max(table[i][j - 1], table[i - 1][j]))
    return table[-1][-1]


'''
cnt=0
flag=0
for r in ws.rows:
    if r[0].value!='단어1':
        w1 = r[0].value
        w2 = r[1].value
        w1 = g2p.runKoG2P(w1, 'rulebook.txt')
        w2 = g2p.runKoG2P(w2, 'rulebook.txt')
        w1 = w1.split()
        w2 = w2.split()
        print('변환하기 전의 음운 구성')
        print(w1)
        print(w2)
        w1 = vowelconvt(w1)
        w2 = vowelconvt(w2)
        w1 = conconvt(w1)
        w2 = conconvt(w2)
        print('변환 후의 음운 구성')
        print(w1)
        print(w2)
        lcs_res = lcs_length(w1, w2)/(max(len(w1), len(w2)))
        print("전체 단어의 최장 겹침 수 : " + str(lcs_res))
        res = lcs_res
        if res>=0.35:
            flag=1
        if flag==r[2].value:
            cnt=cnt+1
        flag=0

print("총 맞힌 횟수 : "+ str(cnt))
print("정확률 : "+ str(cnt/100))
'''



w1 = input()
w2 = input()
w1 = g2p.runKoG2P(w1, 'rulebook.txt')
w2 = g2p.runKoG2P(w2, 'rulebook.txt')
w1 = w1.split()
w2 = w2.split()
print('변환하기 전의 음운 구성')
print(w1)
print(w2)
w1 = vowelconvt(w1)
w2 = vowelconvt(w2)
w1 = conconvt(w1)
w2 = conconvt(w2)
print('변환 후의 음운 구성')
print(w1)
print(w2)
lcs_res = lcs_length(w1, w2)/(max(len(w1), len(w2)))
print("전체 단어의 최장 겹침 수 : " + str(lcs_res))
res = lcs_res
if res>=0.40:
    print("Rhymes")
else : print("Does not Rhymes")


#write_wb.save('lcs3_res.xlsx')
