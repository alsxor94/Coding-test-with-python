DFS%BFS는

stack 과 queue의 구조와  recrusive function에 대하 기본 개념을 필요로 하고 있으며,

많은 양의 데이터를 쉽게 찾으며, 관리하는 방법을 필요로 한다.

DFS는 재귀함수를 이용하며, BFS는 재귀함수를 이용하지 않는다.

Back Tracking에서는 반드시, function을 실행할 때, 현재 상태 혹은 정보를 모두 포함한 채로 실행해야한다. DFS&BFS_4_question.py 참고

fucntion의 argument에서 data를 추가할 때와, 그 전에 data를 추가할 때, 메모리에 저장되는 게 다르다.
function의 argument로 추가하느 경우, 재귀시, 각 node마다 각 node의 이전 값을 가지고 가는 반면, apppend 를 쓰면 변수 값이, 전체적으로 변경된다.


재귀함수는 끝까지 완료를 한 상태에서, queue처럼 하나씩 결과를 내는 구조(DFS와 매우 유사)
