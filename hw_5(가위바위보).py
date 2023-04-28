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

			nSel = int(input("바위(1), 가위(2), 보(3) 선택 : "))
			nSelComputer = random.randint(1, 3)

			print("컴퓨터 선택 결과 : {0}\n".format(nSelComputer))

			oResultTable = [
				[ 0, 1, -1 ],
				[ -1, 0, 1 ],
				[ 1, -1, 0 ]
			]


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
	
