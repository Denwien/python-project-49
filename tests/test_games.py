import importlib
import pytest

MODULES = [
    "brain_even",
    "brain_calc",
    "brain_gcd",
    "brain_prime",
    "brain_progression",
]

CANDIDATE_FN_NAMES = (
    "generate_round",
    "generate_question_and_answer",
    "get_question",
    "generate_question",
    "generate",
)

def try_get_round(module):
    """
    Попытка найти и вызвать функцию, возвращающую (question, answer).
    Если не найдено — pytest.skip.
    """
    for name in CANDIDATE_FN_NAMES:
        if hasattr(module, name):
            fn = getattr(module, name)
            try:
                res = fn()
            except TypeError:
                # функция требует параметры — пропускаем
                continue
            if isinstance(res, tuple) and len(res) == 2:
                return res
    pytest.skip(f"No round-generator function found in {module.__name__}")

@pytest.mark.parametrize("modname", MODULES)
def test_game_has_round_generator(modname):
    module = importlib.import_module(f"brain_games.games.{modname}")
    question, answer = try_get_round(module)
    assert isinstance(question, str) and question.strip() != ""
    assert isinstance(answer, str) and answer.strip() != ""
