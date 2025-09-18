.PHONY: install test lint clean

# Создать/пересоздать виртуальное окружение и установить зависимости через uv
install:
	uv venv --clear || true
	uv sync

# Запустить тесты
test:
	uv run pytest -vv

# Запустить линтер (если настроен в проекте, например ruff/flake8)
lint:
	uv run ruff check . || uv run flake8 .

# Удалить виртуальное окружение
clean:
	rm -rf .venv
