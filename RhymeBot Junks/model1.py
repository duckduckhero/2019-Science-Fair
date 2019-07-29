import g2p

vowels = ['ii','ee','qq','aa','xx','vv','uu','oo','ye','yq','ya','yv','yu','yo','wi','wo','wq','we','wa','wv','xi']
consonants = ['p0','ph','pp','t0','th','tt','k0','kh','kk','s0,','ss','h0','c0','mm','nn','rr','pf','ph','tf','th','kf','kh','s0','ss','h0','c0','mf','nf','ng','ll','ks','nc','nh','lk','lm','lt','lp','lh','ps']

group1 = ['ee','qq', 'ye', 'yq', 'wq','wo', 'we', 'xi'] #ㅔ 계열 모음
group2 = ['ii','wi'] #ㅣ 계열 모음
group3 = ['aa', 'ya', 'wa'] # ㅏ 계열 모음
group4 = ['uu', 'yu'] # ㅜ 계열 모음
group5 = ['vv', 'oo', 'yv', 'wv'] #ㅓ계열 모음

def vowel(word1): #단어 음절에서 모음만 빼서 모으는 함수
    word1 = word1.split()
    length = len(word1)
    w1v = []
    for i in range(length):
        if vowels.count(word1[i])!=0:
            w1v.append(word1[i])
        else :
            w1v.append(' ')
    return w1v

def consonant(word1): #단어 음절에서 자음만 빼서 모으는 함수
    word1 = word1.split()
    length = len(word1)
    w1c = []
    for i in range(length):
        if consonants.count(word1[i])!=0:
            w1c.append(word1[i])
        else :
            w1c.append(' ')
    return w1c

def vowelconvt(vow1): #모음을 해당 그룹의 대표 모음으로 치환하는 함수
    length = len(vow1)
    for i in range(length):
        if group1.count(vow1[i])==1: vow1[i]='ee'
        if group2.count(vow1[i])==1: vow1[i]='ii'
        if group3.count(vow1[i])==1: vow1[i]='aa'
        if group4.count(vow1[i])==1: vow1[i]='uu'
        if group5.count(vow1[i])==1: vow1[i]='vv'
    return vow1

def slice(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    if len1>=len2:
        word1 = word1[(len1-len2):]
    else :
        word2 = word2[(len2-len1):]
    return word1, word2

'''
def isRhyme(word1, word2):
    length = len(word1)
    result = []
    cnt=0
    for i in range(length-1):
        if word1[i]==word2[i]:
            if word1[i+1]==word2[i+1]:
                cnt=cnt+1
    if cnt+1>0:
        return True, cnt+1
    elif cnt==0:
        return False,0
'''

w1 = input()
w2 = input()
w1 = g2p.runKoG2P(w1, 'rulebook.txt')
w2 = g2p.runKoG2P(w2, 'rulebook.txt')
print('단어 자모 분리 결과')
print(w1)
print(w2)
w1v = vowel(w1)
w1c = consonant(w1)
w2v = vowel(w2)
w2c = consonant(w2)
print("변환하기 전의 모음")
print(w1v)
print(w2v)
w2v = vowelconvt(w2v)
w1v = vowelconvt(w1v)
print("변환하고 난 다음의 모음")
print(w1v)
print(w2v)
w1v, w2v = slice(w1v, w2v)
print("슬라이스 한 다음의 모음")
print(w1v)
print(w2v)
print("연속되는 모음의 개수")
'''
res, num = isRhyme(w1v, w2v)
print(str(num)+"개")
print(res)
'''
