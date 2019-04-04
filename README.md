# cky-parser-with-tree

CKY parser 를 shared-packed tree 구조를 이용하여 구현하였습니다.



실행 방법
main.py 파일이 존재하는 디렉토리에서 다음 명령어를 실행합니다.
```sh
$ python3 main.py
```

결과 예시 
각 문장이 순서대로 parsing된 결과가 result 폴더에 저장됩니다.
```sh
문법 정보를 불러왔습니다.
문법의 개수는 31개 입니다
문장을 불러왔습니다. (utf-8 인코딩)
불러온 문장은 3개 입니다.
Parsing 할 문장 : I saw a man on the hill with the telescope
문장의 어절은 10개 입니다.
['S', ['NP', ['n', 'I']], ['VP', ['v', 'saw']]]
['S', ['NP', ['n', 'I']], ['VP', ['VP', ['v', 'saw']], ['NP', ['DT', ['det', 'a']], ['NP', ['n', 'man']]]]]
['S', ['NP', ['n', 'I']], ['VP', ['VP', ['v', 'saw']], ['NP', ['DT', ['det', 'a']], ['NP', ['NP', ['n', 'man']], ['PP', ['P', ['p', 'on']], ['NP', ['DT', ['det', 'the']], ['NP', ['n', 'hill']]]]]]]]
['S', ['NP', ['n', 'I']], ['VP', ['VP', ['v', 'saw']], ['NP', ['DT', ['det', 'a']], ['NP', ['NP', ['n', 'man']], ['PP', ['P', ['p', 'on']], ['NP', ['DT', ['det', 'the']], ['NP', ['NP', ['n', 'hill']], ['PP', ['P', ['p', 'with']], ['NP', ['DT', ['det', 'the']], ['NP', ['n', 'telescope']]]]]]]]]]]
Parsing 할 문장 : time flies like an arrow
문장의 어절은 5개 입니다.
['S', ['NP', ['n', 'time']], ['VP', ['v', 'flies']]]
['S', ['NP', ['n', 'flies']], ['VP', ['v', 'like']]]
Parsing 할 문장 : the man saw the man with the telescope
문장의 어절은 8개 입니다.
['S', ['NP', ['n', 'man']], ['VP', ['v', 'saw']]]
['S', ['NP', ['DT', ['det', 'the']], ['NP', ['n', 'man']]], ['VP', ['v', 'saw']]]
['S', ['NP', ['n', 'man']], ['VP', ['VP', ['v', 'saw']], ['NP', ['DT', ['det', 'the']], ['NP', ['n', 'man']]]]]
['S', ['NP', ['DT', ['det', 'the']], ['NP', ['n', 'man']]], ['VP', ['VP', ['v', 'saw']], ['NP', ['DT', ['det', 'the']], ['NP', ['n', 'man']]]]]
['S', ['NP', ['n', 'man']], ['VP', ['VP', ['v', 'saw']], ['NP', ['DT', ['det', 'the']], ['NP', ['NP', ['n', 'man']], ['PP', ['P', ['p', 'with']], ['NP', ['DT', ['det', 'the']], ['NP', ['n', 'telescope']]]]]]]]
['S', ['NP', ['DT', ['det', 'the']], ['NP', ['n', 'man']]], ['VP', ['VP', ['v', 'saw']], ['NP', ['DT', ['det', 'the']], ['NP', ['NP', ['n', 'man']], ['PP', ['P', ['p', 'with']], ['NP', ['DT', ['det', 'the']], ['NP', ['n', 'telescope']]]]]]]]
```

Parsing 결과는 result 폴더에 문장 순서대로 저장됩니다. 첫번째 문장의 경우 output_0.txt에 저장됩니다. 
```buildoutcfg
// 결과 저장 예시
result/output_1.txt

1. ['S', ['NP', ['n', 'time']], ['VP', ['v', 'flies']]]
2. ['S', ['NP', ['n', 'flies']], ['VP', ['v', 'like']]]

```

분석 과정에서 사용된 grammar 는 result 폴더에 문장 순서대로 저장됩니다. 첫번째 문장의 경우 used_grammar_0.txt에 저장됩니다.
```buildoutcfg
// 결과 저장 예시
result/used_grammar_1.txt

1. ['n', ['time']]
2. ['v', ['time']]
3. ['n', ['flies']]
4. ['v', ['flies']]
5. ['p', ['like']]
6. ['v', ['like']]
7. ['det', ['an']]
8. ['n', ['arrow']]
9. ['NP', ['0']]
10. ['VP', ['1']]
11. ['NP', ['2']]
12. ['VP', ['3']]
13. ['P', ['4']]
14. ['VP', ['5']]
15. ['DT', ['6']]
16. ['NP', ['7']]
17. ['S', [8, 11]]
18. ['NP', [8, 11]]
19. ['VP', [9, 10]]
20. ['S', [10, 13]]
21. ['NP', [10, 13]]
22. ['NP', [14, 15]]
23. ['PP', [12, 21]]
24. ['VP', [13, 21]]
25. ['NP', [10, 22]]
26. ['VP', [11, 22]]
27. ['VP', [11, 22]]
28. ['VP', [9, 24]]

```
Dependencies 

```buildoutcfg
python 3.6.x
numpy 
```

이 코드는 최적화가 더 필요합니다. 
