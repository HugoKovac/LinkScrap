OUTPUT=json

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	PATH=~/.local/bin/ playwright install

part1:
	python3 main.py -o ${OUTPUT} -u https://news.ycombinator.com

part2:
	docker build -t mydocker .
	docker run -it mydocker -o ${OUTPUT} -u https://news.ycombinator.com
