#!/bin/bash
#
# Shell Script
# Excelsior College
# Kyle Davis, 2023
# Sample script to display a menu to user to execute a simple command
# To execute, type  ./shellscript.sh
#

#echo displays a string to the user
echo "Command Menu by Kyle Davis"

# the select statement contains a list of options to be expected in the reply variable
echo "what command do you want to run?"

select reply in "df - disk free" "top - top processes" "free - memory free" "lscpu - cpu info" "cat/proc/cpuinfo - cpu info" "exit - exit the program"

# do is a loop that will execute until the break statement is reached
do 
  # case statement is used to compare the reply variable to a list of strings
  case $reply in
    "df - disk free")
            df -h
            echo "what command do you want to run?
                1. df - disk free
                2. top - top processes
                3. free - memory free
                4. lscpu - cpu info
                5. cat/proc/cpuinfo - cpu info
                6. exit - exit the program
                Select the number of the command you want to run."
            ;;

        "top - top processes")
            top -b -n 1
            echo "what command do you want to run?
                1. df - disk free
                2. top - top processes
                3. free - memory free
                4. lscpu - cpu info
                5. cat/proc/cpuinfo - cpu info
                6. exit - exit the program
                Select the number of the command you want to run."
            ;;
        "free - memory free")
            free -m
            echo "what command do you want to run?
                1. df - disk free
                2. top - top processes
                3. free - memory free
                4. lscpu - cpu info
                5. cat/proc/cpuinfo - cpu info
                6. exit - exit the program
                Select the number of the command you want to run."
            ;;
        "lscpu - cpu info")
            lscpu
            echo "what command do you want to run?
                1. df - disk free
                2. top - top processes
                3. free - memory free
                4. lscpu - cpu info
                5. cat/proc/cpuinfo - cpu info
                6. exit - exit the program
                Select the number of the command you want to run."
            ;;
        "cat/proc/cpuinfo - cpu info")
            cat /proc/cpuinfo
            echo "what command do you want to run?
                1. df - disk free
                2. top - top processes
                3. free - memory free
                4. lscpu - cpu info
                5. cat/proc/cpuinfo - cpu info
                6. exit - exit the program
                Select the number of the command you want to run."
            ;;
        "exit - exit the program")
            exit
            break
            ;;
        *)
            echo Illegal Choice Selected. Please reenter
            echo "what command do you want to run?"
            ;;
    esac

done