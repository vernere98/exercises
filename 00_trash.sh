#!/bin/bash


function func1()
{
	read -p "Are you sure you want to empty trash? [y/n]"  input

case $input in 
	[Yy]) 
		rm -r .mytrash/*
   		echo "Emptying trash."
   		echo "Trash is empty."
   		;;
   	[Nn]) 	exit;;
esac
}
	
case $1 in 
	-e)
		func1
		# empty the trash
	    ;;  
 	*)
		for var in $@; 
		do
			mkdir -p ~/.mytrash/
		        mv "$var" ~/.mytrash/
	echo "Moving to trash."
done
	;;
	
esac

exit 0
