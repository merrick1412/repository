# Makefile for cpretty.l

LEX = lex
CC = gcc
TARGET = cpretty
SOURCE = cpretty.l
CFILE = lex.yy.c

.PHONY: all clean run pdf

all: $(TARGET)

$(TARGET): $(SOURCE)
	$(LEX) $(SOURCE)
	$(CC) -o $(TARGET) $(CFILE) -ll

run: $(TARGET)
	./$(TARGET) < test.c > test.tr

pdf: run
	groff -me test.tr > test.ps
	ps2pdf test.ps test.pdf
	evince test.pdf &

clean:
	rm -f $(TARGET) $(CFILE) test.tr test.ps test.pdf
