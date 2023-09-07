sud = open('./sudoku.csv', 'r')
qlist, alist = [], [] #qlist: 스도쿠 문제 리스트, alist: 스도쿠 답 리스트
#qlist 및 alist 성분 형태: ex) ['1', '2', '0', ... , '2'] (이때 0은 공백을 의미함) <- 총 81개의 성분

idx = 0
for line in sud:
    idx += 1
    if idx <= 2: continue #앞의 2개는 문제와 정답이 없음
    
    #qnum: 스도쿠 문제(숫자 81개가 왼쪽에서 오른쪽으로, 위에서 아래로 붙어있으며 type은 str)
    qnum = line.strip('\n').split(',')[0]
    qlist.append(list(qnum))
    
    #anum: 스도쿠 정답(숫자 81개가 왼쪽에서 오른쪽으로, 위에서 아래로 붙어있으며 type은 str)
    anum = line.strip('\n').split(',')[1]
    alist.append(list(anum))
    
    # if idx <= 5: #앞에거 몇개만 시각화해서 나타냄(있으나 없으나 의미 없음)
    #     for i in range(9):
    #         print(' '.join(qnum[i*9 : (i+1)*9]), '  ', ' '.join(anum[i*9 : (i+1)*9]))
    #     print('\n')

# print(qlist[:2])
# print(alist[:2])
sud.close()

