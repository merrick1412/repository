CXX = g++
CXXFLAGS = -std=c++11 -Wall

SRC = test_stack.cpp
HEADERS = Stack.h Stack.hpp
EXE = proj3.x

all: $(EXE)

$(EXE): $(SRC)
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f $(EXE)
