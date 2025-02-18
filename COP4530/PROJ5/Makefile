CXX = g++
CXXFLAGS = -std=c++11 -Wall

SRC = myspell.cpp
HEADERS = hashtable.h hashtable.hpp
EXE = proj5.x

all: $(EXE)

$(EXE): $(SRC)
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f $(EXE)
