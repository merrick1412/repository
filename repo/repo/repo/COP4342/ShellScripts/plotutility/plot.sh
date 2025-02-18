#!/bin/bash
if [ $# -ne 2 ]; then
	echo "usage: plot.sh filename fieldname"
	exit 1
fi

filename="$1"
fieldname="$2"

if [ ! -f "$filename" ]; then
	echo "Error: File '$filename' not found."
	exit 1
fi

header=$(head -n 1 "$filename")
field_index=$(echo "$header" | tr ' ' '\n' | nl | grep -w "$fieldname" | awk '{print $1}')

if [ -z "$field_index" ]; then
    echo "Field '$fieldname' not found in the first line of the file '$filename'."
    exit 1
fi

cut -d ' ' -f "$field_index" "$filename" | tail -n +2 > tmp1.dat

sort -n tmp1.dat > tmp2.dat

LOWX=$(head -n 1 tmp2.dat)
HIGHX=$(tail -n 1 tmp2.dat)

uniq -c tmp2.dat | awk '{print $2, $1}' > tmp3.dat

HIGHY=$(awk '{print $2}' tmp3.dat | sort -nr | head -n 1)

cp /home/faculty/whalley/cop4342exec/plot.p plot1.p
sed -i "s/LOWX/$LOWX/" plot1.p
sed -i "s/HIGHX/$HIGHX/" plot1.p
sed -i "s/HIGHY/$HIGHY/" plot1.p
sed -i "s/FILE/tmp3.dat/" plot1.p

gnuplot plot1.p
ps2pdf graph.ps graph.pdf
evince graph.pdf &

rm -f tmp1.dat tmp2.dat tmp3.dat plot1.p graph.ps

echo "$fieldname in the $filename file was successfully plotted."
