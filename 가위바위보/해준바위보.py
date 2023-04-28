import random

def get_choice():
    choice = input("가위, 바위, 보, 그만 중 하나를 선택하세요: ")
    while choice not in ['가위', '바위', '보', '그만']:
        print("잘못된 입력입니다.")
        choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "무승부"
    elif user_choice == "가위" and computer_choice == "보":
        return "승리"
    elif user_choice == "바위" and computer_choice == "가위":
        return "승리"
    elif user_choice == "보" and computer_choice == "바위":
        return "승리"
    else:
        return "패배"

def play_game():
    wins, draws, losses = 0, 0, 0
    while True:
        user_choice = get_choice()
        if user_choice == "그만":
            break
        computer_choice = random.choice(['가위', '바위', '보'])
        print("사용자 선택:", user_choice)
        print("컴퓨터 선택:", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        if result == "승리":
            wins += 1
        elif result == "무승부":
            draws += 1
        else:
            losses += 1
        print(result)
    return wins, draws, losses 

total_wins, total_draws, total_losses = 0, 0, 0
while True:
    print("새로운 게임을 시작합니다.")
    wins, draws, losses = play_game()
    total_wins += wins
    total_draws += draws
    total_losses += losses
    print(f"게임 결과: {wins}승 {draws}무 {losses}패")
    play_again = input("새 게임을 시작하시겠습니까? (예/아니오): ")
    if play_again == "아니오":
        break

print("전체 게임 결과")
print(f"전체: {total_wins + total_draws + total_losses}게임, {total_wins}승 {total_draws}무 {total_losses}패")
