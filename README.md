# cky-parser-with-tree

CKY parser 를 shared-packed tree 구조를 이용하여 구현하였습니다.

결과 예시 

```buildoutcfg
input : I saw a man on the hill with the telescope
result : 
['S', ['NP', ['DT', ['det', 'the']], ['NP', ['n', 'man']]], ['VP', ['VP', ['v', 'saw']], ['NP', ['DT', ['det', 'the']], ['NP', ['NP', ['n', 'man']], ['PP', ['P', ['p', 'with']], ['NP', ['DT', ['det', 'the']], ['NP', ['n', 'telescope']]]]]]]]
```

Dependencies 

```buildoutcfg
python 3.6.x
numpy 
```

이 코드는 최적화가 더 필요합니다. 
