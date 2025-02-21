#!/bin/bash

#grab month and year
current_month=$(date +"%m")
current_year=$(date +"%Y")

#function to format the month

convert_month() {
	case "$(echo "$1" | tr '[:upper:]' '[:lower:]')" in
		jan) echo 1 ;;
		feb) echo 2 ;;
		mar) echo 3 ;;
    apr) echo 4 ;;
    may) echo 5 ;;
    jun) echo 6 ;;
    jul) echo 7 ;;
    aug) echo 8 ;;
    sep) echo 9 ;;
    oct) echo 10 ;;
    nov) echo 11 ;;
    dec) echo 12 ;;
    *) echo "Invalid" ;; 
  esac
}


#main logic

if [ "$#" -eq 0 ]; then
 #if theres no args
	cal "$current_month" "$current_year"
elif [ "$#" -eq 1 ]; then
#one arg
	arg1="$1"
	if [[ "$arg1" =~ ^[0-9]+$ ]]; then
		if [ "$arg1" -ge 1 ] && [ "$arg1" -le 12 ]; then
			#month num
			cal "$arg1" "$current_year"
		elif [ "$arg1" -gt 12 ]; then
		#year
			cal "$arg1"
		else
			echo "Error: $arg1 is not a valid month or year."
		fi
	else
	 #non num month, check for abbreviation
		month=$(convert_month "$arg1")
		if [ "$month" != "Invalid" ]; then
			cal "$month" "$current_year"
		else
			echo "Error: $arg1 is not a valid month"
		fi
	fi
elif [ "$#" -eq 2 ]; then
# 2 args, month and yr
	month_arg="$1"
	year_arg="$2"
	if [[ "$year_arg" =~ ^[0-9]+$ ]]; then
	if [[ "$month_arg" =~ ^[0-9]+$ ]]; then
      # Num month
      if [ "$month_arg" -ge 1 ] && [ "$month_arg" -le 12 ]; then
        cal "$month_arg" "$year_arg"
      else
        echo "Error: $month_arg is not a valid month."
      fi
    else
      # Non-numeric: Check for month abbreviation
      month=$(convert_month "$month_arg")
      if [ "$month" != "Invalid" ]; then
        cal "$month" "$year_arg"
      else
        echo "Error: $month_arg is not a valid month."
      fi
    fi
  else
    echo "Error: $year_arg is not a valid year."
  fi
else
  # Invalid number of arguments
  echo "Usage: cal.sh [month] [year]"
fi
	 