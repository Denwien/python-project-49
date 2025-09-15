import subprocess

def test_cli_welcome():
    # Запуск скрипта cli.py и подмена ввода имени "Tester"
    result = subprocess.run(
        ["python", "brain_games/scripts/cli.py"],
        capture_output=True,
        text=True,
        input="Tester\n"
    )
    # Проверяем, что приветствие присутствует в stdout
    assert "Welcome to the Brain Games!" in result.stdout
    # Проверяем, что имя пользователя присутствует в stdout
    assert "Tester" in result.stdout
