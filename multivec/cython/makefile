all: python

condemned:
	python2 setup.py build
	cp build/lib.linux-x86_64-2*/*.so multivec.so

python:
	python3 setup.py build
	cp build/lib.linux-x86_64-3*/*.so multivec.so

clean:
	rm -rf build multivec.so
