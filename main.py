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

    result = []

    # 각 문장별로 파싱하기 위해 for문으로 인덱싱한다.
    for sentenceIdx in range (1):
        word = sentence[sentenceIdx].split(' ') # 공백을 기준으로 문장을 어절 단위로 분리한다.
        numOfWord = len(word) # 어절의 개수를 센다.
        print('Parsing 할 문장 : {}'.format(sentence[sentenceIdx]))
        print('문장의 어절은 {}개 입니다.'.format(numOfWord))

        table = [] # 원본 테이블
        result = [] # 결과를 임시 저장할 테이블
        find = [] # 찾을 문법이 들어있는 테이블, 다 찾으면 없애버린다.

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
            result[i][i] = word[i]
            find[i][i] = word[i]

        changeable = True
        while (changeable):
            changeable = False  # 한번도 안바뀌었으면 이 플래그가 바뀌지 않았고 그대로 루프 종료 !
            for j in range (numOfWord):
                for i in range (j,-1,-1): # 파싱 방향은 이 방향인데... ?
                    # 각 셀 별로 grammar가 존재하는지 검색을 한다.
                # 바꿀게 없을 때 까지 계속 해야해

                    searchKey = find[j][i]
                    find[j][i] = ''# pop

                    if ' ' in searchKey : # 한 칸에 찾을게 여러개 있으면, TODO 마지막 꺼만 봐도 되지 않을까? -> 두개 추가되면 DONE
                        searchKeyS = searchKey.split(' ') # 나눈다.

                        for searchIdx in range (len(searchKeyS)):
                            searchKey = searchKeyS[searchIdx]
                            for grammarIdx in range(myGrammar.len):
                                searchTarget = grammar[grammarIdx,1]
                                if searchKey == searchTarget :
                                    find[j][i] = find[j][i] + ' ' +grammar[grammarIdx,0]
                                    result[j][i] = result[j][i] + ' ' + grammar[grammarIdx, 0] # TODO 이거 대신에 기록할 방법을 찾아보자
                                    changeable = True # 혹시라도 바꿨으면 루프 한번 더돌면서 다시 바꿀게 있는지 확인해야함 !
                    else:  # 하나 있으면
                        for grammarIdx in range(myGrammar.len):
                            searchTarget = grammar[grammarIdx,1] # 두번째 열이 바로 바꿀 대상
                            if searchKey == searchTarget : # grammar 가 있으면 결과를 저장하라
                                find[j][i] = find[j][i] + ' ' +grammar[grammarIdx,0]
                                result[j][i] = result[j][i] + ' ' + grammar[grammarIdx, 0] # TODO 이거 대신에 기록할 방법을 찾아보자
                                changeable = True # 혹시라도 바꿨으면 루프 한번 더돌면서 다시 바꿀게 있는지 확인해야함 !

        print(table) # 원본
        print(result) # 일단 하나짜리 다 한거 !

        # TODO
        #  What I Have Done : 일단 unary 하나 짜리 rewrite 가능한 문법은 전부 표현 완료
        #  What I Should Do : 이제 양쪽을 보고 합쳐지는지 여부를 판단하는 알고리즘을 작성해야 함









