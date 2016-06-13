.PHONY: all install deploy

all: index.html

install:
	pip3 install dragonmapper fake-factory
	npm install -g jade

index.html: gen_names.py names_db.py
	python3 gen_names.py
	jade --pretty < iphone_credits.jade > index.html

deploy:
	git push origin master:gh-pages
