CXX = g++
CXXFLAGS = -std=c++11 -Wall

SRC = proj4_driver.cpp
HEADERS = bst.h bst.hpp
EXE = proj4.x

all: $(EXE)

$(EXE): $(SRC)
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f $(EXE)
