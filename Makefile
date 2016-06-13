.PHONY: all

all: index.html

index.html: gen_names.py
	python3 gen_names.py
	jade --pretty < iphone_credits.jade > index.html
