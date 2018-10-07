.PHONY: tests

tests:
	@python -m unittest discover tests/ -p 'test*.py'
