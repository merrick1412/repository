
delete_entry(){

	if [ $# -ne 2 ]; then
	    echo "Usage: phonebook.sh -d <last name> <first name>"
	    exit 1
	fi

	#first arg is last name, 2nd is first
	last_name="$1"
	first_name="$2"

	#checking if the entry is in the file
	if ! grep -q "^$last_name $first_name " phonebook.dat; then
	    echo "Error: Entry not found"
	    exit 1
	fi

	#remove the entry and save it to a temp file
	grep -v "^$last_name $first_name " phonebook.dat > phonebook.dat.tmp
	mv phonebook.dat.tmp phonebook.dat


	echo "Entry for $first_name $last_name deleted."
}

modify_entry() {
	if [ $# -lt 3 ]; then
	    echo "Usage: phonebook.sh -m <last name> <first name> <address>"
	    exit 1
	fi

	last_name="$1"
	first_name="$2"
	shift 2 #goest to 3rd arg, remaining input is address
	new_address="$*"

	#check if it exists
	if ! grep -q "^$last_name $first_name " phonebook.dat; then
	    echo "Error: Entry not found"
	    exit 1
	fi

	#modify address field
	awk -v ln="$last_name" -v fn="$first_name" -v new_addr="$new_address" '
	{
		if ($1 == ln && $2 == fn) {
			print $1, $2, $3, new_addr; #checks if first name and last name match the entry
			found=1;
		} else {
		    print $0;
		}
	}
	END { if (!found) print "Error: Entry not found" > "/dev/stderr"; exit !found }
	' phonebook.dat > phonebook.dat.tmp && mv phonebook.dat.tmp phonebook.dat

	echo "Entry for $first_name $last_name modified."
}

print_entries() {
    if [ $# -ne 1 ]; then
	echo "Usage: phonebook.sh -p \"<pattern>\""
	exit 1
    fi

    pattern="$1"

    #looking for entries that match
    matches=$(grep "$pattern" phonebook.dat)

    if [ -z "$matches" ]; then
	echo "Error: No entries match the pattern."
	exit 1
    fi

    #print output
    echo "$matches" | awk '{
	printf "%-15s %-15s %-12s %s\n", $1, $2, $3, $4
    }'
}

insert_entry() {
    if [ $# -lt 4 ]; then
        echo "Usage: phonebook.sh -i <last name> <first name> <phone number> <address>"
        exit 1
    fi

    last_name="$1"
    first_name="$2"
    phone_number="$3"
    shift 3  # Move to the address argument
    address="$*"

    # Validate phone number
    if ! [[ "$phone_number" =~ ^[0-9]{3}-[0-9]{3}-[0-9]{4}$ ]]; then
        echo "Error: Invalid phone number format. Use ###-###-####"
        exit 1
    fi

    # check if the entry already exists
    if grep -q "^$last_name $first_name " phonebook.dat; then
        echo "Error: Entry already exists."
        exit 1
    fi

    # insert the new entry
    echo "$last_name $first_name $phone_number $address" >> phonebook.dat
    sort -k1,1 -k2,2 phonebook.dat -o phonebook.dat

    echo "Entry for $first_name $last_name added successfully."
}

case "$1" in
	-i) shift; insert_entry "$@";;
	-d) shift; delete_entry "$@";;
	-m) shift; modify_entry "$@";;
	-p) shift; print_entries "$1";;
	*) echo "Invalid option"; exit 1;;
esac
