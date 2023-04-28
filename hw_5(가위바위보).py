import os
import sys
import random

# Example 4
class Play:
	# 초기화
	@classmethod
	def Start(cls, args):

		cls.game(args)

	# 4 - 3
	@classmethod
	def game(cls, args):
		nWinCount = 0
		nDrawCount = 0

		while True:
			"""
			random 모듈이란?
			- Python 에서 제공하는 난수를 생성 할 수 있는 모듈을 의미한다. (즉, 해당 모듈을 활용하면 특정 범위에 있는 숫자 중 랜덤하게
			숫자를 가져오는 것이 가능하다는 것을 알 수 있다.)
			"""
			nSel = int(input("바위(1), 가위(2), 보(3) 선택 : "))
			nSelComputer = random.randint(1, 3)

			"""
			format 메서드란?
			- 문자열 자료형 데이터에 존재하는 메서드로 해당 메서드를 활용하면 서식화 된 문자열을 생성하는 것이 가능하다. (즉, f 문자열 포맷팅과
			동일한 역할을 수행한다.)
			"""
			print("컴퓨터 선택 결과 : {0}\n".format(nSelComputer))

			oResultTable = [
				[ 0, 1, -1 ],
				[ -1, 0, 1 ],
				[ 1, -1, 0 ]
			]

			"""
			oResultTable 는 리스트를 요소로 하는 리스트이기 때문에 리스트의 특정 데이터에 접근하기 위해서는 [ ] (인덱스 연산자) 를 2 번 
			명시해야 한다는 것을 알 수 있다.

			바위 가위 보 게임은 선택에 따른 결과가 이미 정해져있기 때문에 선택에 따른 결과를 미리 테이블 형태로 제작하는 것이 가능하며 이를
			결정 테이블이라고 한다.
			"""
			# 졌을 경우
			if oResultTable[nSel - 1][nSelComputer - 1] < 0:
				print("졌습니다!")
				break
			else:
				nResult = oResultTable[nSel - 1][nSelComputer - 1]
				oResultStr = "이겼습니다!" if nResult > 0 else "비겼습니다!"

				print(oResultStr)

				nWinCount += 1 if nResult > 0 else 0
				nDrawCount += 1 if nResult == 0 else 0

			print("")

		print("결과 : {0} 승 {1} 무".format(nWinCount, nDrawCount))



# 메인 모듈 일 경우
if __name__ == "__main__":
	Play.Start(sys.argv)
	