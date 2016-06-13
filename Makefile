.PHONY: all install

install:
	pip3 install dragonmapper fake-factory
	npm install -g jade

all: index.html

index.html: gen_names.py names_db.py
	python3 gen_names.py
	jade --pretty < iphone_credits.jade > index.html
