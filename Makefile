run:
	python3.10.12 main.py

test:
	pytest test.py

clean:
	rm -rf __pycache__
	rm -rf venv