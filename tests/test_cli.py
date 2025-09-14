import builtins
import pytest
from brain_games import cli

def test_welcome_user(monkeypatch, capsys):
    # подменяем ввод имени
    monkeypatch.setattr("builtins.input", lambda prompt="": "Tester")
    name = cli.welcome_user()
    captured = capsys.readouterr()
    # проверяем, что приветствие напечатано и функция возвращает имя
    assert "Welcome to the Brain Games!" in captured.out or "May I have your name" in captured.out
    assert name == "Tester"
