# NLP course assignment #2
# CKY Parser with parse tree
# Made by Dong hyun kim

# Cocke-Kasami-Younger algorithm based on bottom-up parsing.
# CKY : First grammar must be converted to Chomsky normal form (CNF) in which productions must have either exactly 2 non-terminal symbols

from fileIO import *

if __name__ == '__main__':
    # 문법 불러오기
    myGrammar = Grammar()
    myGrammar.load('data/grammar.txt')

    # 문장 불러오기
    mySentence = Sentence()
    mySentence.load('data/input.txt')

    sentence = mySentence.contents
    grammar = myGrammar.contents

    # 각 문장별로 파싱하기 위해 for문으로 인덱싱한다.
    for sentenceIdx in range(3):
        word = sentence[sentenceIdx].split(' ') # 공백을 기준으로 문장을 어절 단위로 분리한다.
        numOfWord = len(word) # 어절의 개수를 센다.
        print('Parsing 할 문장 : {}'.format(sentence[sentenceIdx]))
        print('문장의 어절은 {}개 입니다.'.format(numOfWord))

        table = [] # 원본 테이블
        result = [] # 결과를 임시 저장할 테이블
        find = [] # 찾을 문법이 들어있는 테이블, 다 찾으면 없애버린다.
        idTable = []

        # 비어있는 2차원의 table을 만든다.
        for i in range (numOfWord) :
            table.append([])
            result.append([])
            find.append([])

            for j in range(numOfWord):
                table[i].append([])
                result[i].append([])
                find[i].append([])

        # 대각선에 먼저 단어를 채우고 시작한다.
        for i in range (numOfWord):
            table[i][i] = word[i]
            result[i][i] = ''
            find[i][i] = word[i]

        ID = 0 # packing 용 정보에 사용할 ID 초기화

        for j in range (numOfWord):
            # 먼저 대각선 방향으로 unary (1:1 매칭인 부분)를 완료한다.
            # 각 셀 별로 grammar가 존재하는지 검색을 한다.
            # 바꿀게 없을 때 까지 계속 해야해
            i = j
            searchKey = find[j][i]
            find[j][i] = ''

            if ' ' in searchKey : # 한 칸에 찾을게 여러개 있으면, TODO 마지막 꺼만 봐도 되지 않을까? -> 두개 추가되면 DONE
                searchKeyS = searchKey.split(' ') # 나눈다.

                for searchIdx in range (len(searchKeyS)): # 현재 찾아야할 개수 만큼 반복한다.
                    searchKey = searchKeyS[searchIdx]
                    for grammarIdx in range(myGrammar.len): # 문법 목록에 있는 개수 만큼 반복한다.
                        searchTarget = grammar[grammarIdx,1] # 문법 목록 오른쪽 포맷에 있는 건지 검색
                        if searchKey == searchTarget :

                            if find[j][i] == '':
                                find[j][i] = str(ID)
                            else :
                                find[j][i] = find[j][i] + ' ' +str(ID)
                            result[j][i] = result[j][i] + ' ' + str(ID)  # TODO 이거 대신에 기록할 방법을 찾아보자
                            idTable.append([grammar[grammarIdx,0], [grammar[grammarIdx, 1]]])
                            ID += 1

            else:  # 하나 있으면
                for grammarIdx in range(myGrammar.len):
                    searchTarget = grammar[grammarIdx,1] # 두번째 열이 바로 바꿀 대상
                    if searchKey == searchTarget : # grammar 가 있으면 결과를 저장하라

                        if find[j][i] == '':
                            find[j][i] = str(ID)
                        else:
                            find[j][i] = find[j][i] + ' ' + str(ID)

                        if result[j][i] == '':
                            result[j][i] = str(ID)
                        else:
                            result[j][i] = result[j][i] + ' ' + str(ID) # TODO 이거 대신에 기록할 방법을 찾아보자
                        idTable.append([grammar[grammarIdx, 0], [grammar[grammarIdx, 1]]])
                        ID += 1

        for j in range(numOfWord):
            for i in range(j, -1, -1):
                # unary 시작
                searchKey = find[j][i]
                find[j][i] = '' # 찾을 query는 현재 테이블에서 제거
                if ' ' in searchKey:  # 한 칸에 찾을게 여러개 있으면
                    searchKeyS = searchKey.split(' ')  # 나눈다.

                    for searchIdx in range(len(searchKeyS)):  # 현재 찾아야할 개수 만큼 반복한다.
                        searchKey = searchKeyS[searchIdx]
                        currentQuery = idTable[int(searchKey)]
                        for grammarIdx in range(myGrammar.len):  # 문법 목록에 있는 개수 만큼 반복한다.
                            searchTarget = grammar[grammarIdx, 1]  # 문법 목록 오른쪽 포맷에 있는 건지 검색
                            if currentQuery[0] == searchTarget:
                                if find[j][i] == '':
                                    find[j][i] = str(ID)
                                else :
                                    find[j][i] = find[j][i] + ' ' +str(ID)
                                result[j][i] = result[j][i] + ' ' + str(ID)  # TODO 이거 대신에 기록할 방법을 찾아보자
                                idTable.append([grammar[grammarIdx, 0], [searchKey]])
                                ID += 1
                elif searchKey == []: # 아무것도 없으면
                    pass

                else:  # 하나 있으면
                    currentQuery = idTable[int(searchKey)]
                    for grammarIdx in range(myGrammar.len):
                        searchTarget = grammar[grammarIdx, 1]  # 두번째 열이 바로 바꿀 대상
                        if currentQuery[0] == searchTarget:  # grammar 가 있으면 결과를 저장하라
                            if find[j][i] == '':
                                find[j][i] = str(ID)
                            else:
                                find[j][i] = find[j][i] + ' ' + str(ID)

                            if result[j][i] == '':
                                result[j][i] = str(ID)
                            else:
                                result[j][i] = result[j][i] + ' ' + str(ID)  # TODO 이거 대신에 기록할 방법을 찾아보자
                            idTable.append([grammar[grammarIdx, 0], [searchKey]])
                            ID += 1

        # 여기 까지 unary 완료 !

        for j in range(1, numOfWord):
            for i in range(j-1, -1, -1):
                for k in range(i,j,1):

                    left = find[i][k]
                    down = find[k+1][j]

                    if left == '' : # 왼쪽에 아무것도 없을 경우 붙일 필요 없으므로 for문 pass
                        continue
                    if down == '' : # 오른쪽에 아무것도 없을 경우 붙일 필요 없으므로 for문 pass
                        continue
                    if left == [] :
                        continue
                    if down == [] :
                        continue

                    if ' ' in left : # 찾을것이 여러개 있으면 나누어서 검색한다.
                        leftS = left.split(' ')
                        if ' ' in down : # left 여러개 & down 여러개
                            downS = down.split(' ')
                            for leftIdx in range(len(leftS)):
                                for downIdx in range(len(downS)):
                                    leftQuery = idTable[int(leftS[leftIdx])]
                                    rightQuery = idTable[int(downS[downIdx])]
                                    searchKey = leftQuery[0] + ' ' + rightQuery[0]

                                    for grammarIdx in range(myGrammar.len):
                                        searchTarget = grammar[grammarIdx, 1] # 이 부분이 있는지 검사하면 된다.

                                        if searchKey == searchTarget:
                                            if find[i][j] == '':
                                                find[i][j] = str(ID)
                                            elif find[i][j] == []:
                                                find[i][j] = str(ID)

                                            idTable.append([grammar[grammarIdx, 0], [int(leftS[leftIdx]),int(downS[downIdx])]])
                                            ID += 1



                                    # TODO  문법 정보 검색하고, 붙일 수 있으면 붙인 다음에 정보 테이블에 저장
                                               
                        else : # left 여러개 & down 한개만
                            for leftIdx in range(len(leftS)):
                                leftQuery = idTable[int(leftS[leftIdx])]
                                rightQuery = idTable[int(down)]
                                searchKey = leftQuery[0] + ' ' + rightQuery[0]

                                for grammarIdx in range(myGrammar.len):
                                    searchTarget = grammar[grammarIdx, 1]  # 이 부분이 있는지 검사하면 된다.

                                    if searchKey == searchTarget:
                                        if find[i][j] == '':
                                            find[i][j] = str(ID)
                                        elif find[i][j] == []:
                                            find[i][j] = str(ID)
                                        idTable.append([grammar[grammarIdx, 0], [int(leftS[leftIdx]),int(down)]])
                                        ID += 1
                                 # TODO  문법 정보 검색하고, 붙일 수 있으면 붙인 다음에 정보 테이블에 저장
                            
                    else :
                        if ' ' in down : # left 한개만 & down 여거래
                            downS = down.split(' ')
                            for downIdx in range(len(downS)):
                                leftQuery = idTable[int(left)]
                                rightQuery = idTable[int(downS[downIdx])]
                                searchKey = leftQuery[0] + ' ' + rightQuery[0]

                                for grammarIdx in range(myGrammar.len):
                                    searchTarget = grammar[grammarIdx, 1]  # 이 부분이 있는지 검사하면 된다.

                                    if searchKey == searchTarget:
                                        if find[i][j] == '':
                                            find[i][j] = str(ID)
                                        elif find[i][j] == []:
                                            find[i][j] = str(ID)

                                        idTable.append([grammar[grammarIdx, 0], [int(left),int(downS[downIdx])]])
                                        ID += 1

                        else : # left 한개만 & down 한개만
                            leftQuery = idTable[int(left)]
                            rightQuery = idTable[int(down)]
                            searchKey = leftQuery[0] + ' ' + rightQuery[0]


                            for grammarIdx in range(myGrammar.len):
                                searchTarget = grammar[grammarIdx, 1]  # 이 부분이 있는지 검사하면 된다.

                                if searchKey == searchTarget:
                                    if find[i][j] == '':
                                        find[i][j] = str(ID)
                                    elif find[i][j] == []:
                                        find[i][j] = str(ID)
                                    idTable.append([grammar[grammarIdx, 0], [int(left),int(down)]])
                                    ID += 1
        # 여기 까지 하면 전부 완료

        for tableIdx in range (len(idTable)):
            if idTable[tableIdx][0] == 'S' :
                completePrint: str = str(idTable[tableIdx])
                condition = True
                while(condition):
                    condition = False
                    i = 0

                    for i in range (len(idTable)):
                        findString = '['+str(i)+','
                        if findString in completePrint :
                            change = str(idTable[i])+','
                            completePrint = completePrint.replace(findString, change)
                            condition = True
                        findString = ', '+str(i)+']'
                        if findString in completePrint :
                            change = ', '+str(idTable[i])
                            completePrint = completePrint.replace(findString, change)
                            condition = True
                        findString = "\'"+str(i)+"\'"
                        if findString in completePrint :
                            change = str(idTable[i])
                            if '[' in change :
                                change = change.replace('[', '')
                            if ']' in change:
                                change = change.replace(']', '')
                            completePrint = completePrint.replace(findString, change)
                            condition = True
                        findString = ''
                print (completePrint)

        with open("data/output.txt", "w") as text_file:
            text_file.write(completePrint)

        # TODO
        #  What I Have Done : 일단 unary 하나 짜리 rewrite 가능한 문법은 전부 표현 완료
        #  양쪽을 보고 합쳐지는지 여부를 판단하는 알고리즘 작성 완료
        #  What I Should Do : 완성된 테이블에서 S 찾고 recursive 하게 트리 출력하기