CXX = g++
CXXFLAGS = -std=c++11 -Wall

SRC = proj1.cpp
HEADERS = Vector.h Vector.hpp
EXE = proj1.x

all: $(EXE)

$(EXE): $(SRC)
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f $(EXE)