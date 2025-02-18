CXX = g++
CXXFLAGS = -std=c++11 -Wall

SRC = test_vector.cpp
HEADERS = Vector.h Vector.hpp
EXE = proj2.x

all: $(EXE)

$(EXE): $(SRC)
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f $(EXE)
