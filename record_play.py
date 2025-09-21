import os
import subprocess

# Создаем папку recordings, если ее нет
os.makedirs("recordings", exist_ok=True)

# Список игр
games = [
    "brain-even",
    "brain-calc",
    "brain-gcd",
    "brain-progression",
    "brain-prime"
]

def list_games():
    print("Доступные игры:")
    for idx, game in enumerate(games, 1):
        print(f"{idx}. {game}")

def select_game():
    list_games()
    choice = input("Введите номер игры для записи/воспроизведения (или '0' для всех): ")
    if choice == '0':
        return games
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(games):
            return [games[idx]]
    except ValueError:
        pass
    print("Некорректный выбор. Попробуйте снова.")
    return select_game()

def record_games(selected_games):
    for game in selected_games:
        print(f"\nЗапись игры: {game}")
        script_path = f"brain_games/games/{game}.py"
        output_file = f"recordings/{game}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            subprocess.run(["python", script_path], stdout=f, stderr=f)
        print(f"Запись для {game} сохранена в {output_file}")

def play_games(selected_games):
    for game in selected_games:
        print(f"\nВоспроизведение записи: {game}")
        output_file = f"recordings/{game}.txt"
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print(f"Запись для {game} не найдена.")
        print("-" * 40)

def main():
    print("Выберите действие:")
    print("1. Записать игру")
    print("2. Воспроизвести игру")
    action = input("Введите 1 или 2: ")
    
    selected_games = select_game()
    
    if action == '1':
        record_games(selected_games)
    elif action == '2':
        play_games(selected_games)
    else:
        print("Некорректный выбор. Выход.")

if __name__ == "__main__":
    main()

