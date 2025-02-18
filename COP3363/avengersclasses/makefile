#makefile Avenger class
Avenger: AvengerApp.o Avenger.o
	g++ AvengerApp.o Avenger.o -o Avenger
AvengerApp.o: AvengerApp.cpp
	g++ -c AvengerApp.cpp
Avenger.o: Avenger.h Avenger.cpp
	g++ -c Avenger.h
	g++ -c Avenger.cpp
clean:
	rm -rf *o Avenger

