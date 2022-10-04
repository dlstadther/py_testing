
docs-init:
	mkdir docs && cd docs && poetry run sphinx-quickstart && cd ..

docs-build:
	poetry run sphinx-apidoc -o docs py_testing/

docs-html: docs-build
	cd docs && make clean html && cd ..
