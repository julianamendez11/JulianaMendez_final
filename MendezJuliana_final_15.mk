MendezJuliana_final_15.pdf: datos1.dat plot1.py
	python plot1.py

datos1.dat : a.out
	./a.out 

a.out: final1.cpp
	g++ final1.cpp
