#!/bin/bash
#
# Order Program
# Excelsior College
# Kyle Davis, 2023
# Sample script to display a menu to user to execute a simple command
# To execute, type  ./order.sh
#
food="" # variables are used to store the user's order
drink="" # variables are used to store the user's order
toys="" # variables are used to store the user's order
clothing="" # variables are used to store the user's order
echo "Welcome to the Order Program, please select an option from the menu below."
# the select statement contains a list of options to be expected in the reply variable
select order in "food" "drink" "toys" "clothes" "order summary" "exit"

do
    case $order in # case statement is used to compare the reply variable to a list of strings
        "food")
            echo "What food would you like to order?"
                select food in "pizza" "burger" "hot dog" "taco" "exit"
                    do
                        case $food in
                            "pizza")
                                echo "You have ordered a pizza."
                                echo "Thank you for your order! Press enter to go back to the main menu."
                                break
                                ;;
                            "burger")
                                echo "You have ordered a burger."
                                echo "Thank you for your order! Press enter to go back to the main menu."
                                break
                                ;;
                            "hot dog")
                                echo "You have ordered a hot dog."
                                echo "Thank you for your order! Press enter to go back to the main menu."
                                break
                                ;;
                            "taco")
                                echo "You have ordered a taco."
                                echo "Thank you for your order! Press enter to go back to the main menu."
                                break
                                ;;
                            "exit")
                                echo "Press enter to go back to the main menu."
                                
                                break
                                ;;
                            *) # default case
                                echo "Invalid option, please try again." # error message
                                echo "What food would you like to order?"
                                echo "1. Pizza 2. Burger 3. Hot Dog 4. Taco 5. Exit"
                                ;;
                        esac

                    done
                    ;;            
        "drink")
            echo "What drink would you like to order?"
                select drink in "coke" "pepsi" "sprite" "dr. pepper" "exit"
                        do
                            case $drink in
                                "coke")
                                    echo "You have ordered a coke."
                                    echo "Thank you for your order! Press enter to go back to the main menu."
                                    break
                                    ;;
                                "pepsi")
                                    echo "You have ordered a pepsi."
                                    echo "Thank you for your order! Press enter to go back to the main menu."
                                    break
                                    ;;
                                "sprite")
                                    echo "You have ordered a sprite."
                                    echo "Thank you for your order! Press enter to go back to the main menu."
                                    break
                                    ;;
                                "dr. pepper")
                                    echo "You have ordered a dr. pepper."
                                    echo "Thank you for your order! Press enter to go back to the main menu."
                                    break
                                    ;;
                                "exit")
                                    echo "Press enter to go back to the main menu."
                                    
                                    break
                                    ;;
                                *)
                                    echo "Invalid option, please try again."
                                    echo "What food would you like to order?"
                                    echo "1. coke 2. pepsi 3. sprite 4. Dr. Pepper 5. Exit"
                                    ;;
                            esac
                        done
                        ;;
        "toys")
            echo "What toy would you like to order?"
                select toys in "lego" "barbie" "hot wheels" "nerf gun" "exit"
                        do
                            case $toys in
                                "lego")
                                    echo "You have ordered a lego."
                                    echo "Thank you for your order! Press enter to go back to the main menu."
                                    break
                                    ;;
                                "barbie")
                                    echo "You have ordered a barbie."
                                    echo "Thank you for your order! Press enter to go back to the main menu."
                                    break
                                    ;;
                                "hot wheels")
                                    echo "You have ordered a hot wheels."
                                    echo "Thank you for your order! Press enter to go back to the main menu."
                                    break
                                    ;;
                                "nerf gun")
                                    echo "You have ordered a nerf gun."
                                    echo "Thank you for your order! Press enter to go back to the main menu."
                                    break
                                    ;;
                                "exit")
                                    echo "Press enter to go back to the main menu."
                                    
                                    break
                                    ;;
                                *)
                                    echo "Invalid option, please try again."
                                    echo "What food would you like to order?"
                                    echo "1. lego 2. barbie 3. hot wheels 4. nerf gun 5. Exit"
                                    ;;
                            esac
                        done
                        ;;
        "clothes")
            echo "What clothing item would you like to order?"
                select clothes in "shirt" "pants" "shoes" "socks" "exit"
                        do
                            case $clothes in
                                "shirt")
                                    echo "You have ordered a shirt."
                                    echo "Thank you for your order! Press enter to go back to the main menu."
                                    break
                                    ;;
                                "pants")
                                    echo "You have ordered a pants."
                                    echo "Thank you for your order! Press enter to go back to the main menu."
                                    break
                                    ;;
                                "shoes")
                                    echo "You have ordered a shoes."
                                    echo "Thank you for your order! Press enter to go back to the main menu."
                                    break
                                    ;;
                                "socks")
                                    echo "You have ordered a socks."
                                    echo "Thank you for your order! Press enter to go back to the main menu."
                                    break
                                    ;;
                                "exit")
                                    echo "Press enter to go back to the main menu."
                                    
                                    break
                                    ;;
                                *)
                                    echo "Invalid option, please try again."
                                    echo "What food would you like to order?"
                                    echo "1. shirt 2. pants 3. shoes 4. socks 5. Exit"
                                    ;;
                            esac
                        done
                        ;;
        "order summary") # order summary
            echo "Your order summary is as follows:"
            if [[ -n $food ]] && [[ $food != "exit" ]]; then # if the variable is not empty and the variable is not equal to exit then print the variable
                echo "Food: $food"
            fi
            if [[ -n $drink ]] && [[ $drink != "exit" ]]; then
                echo "Drink: $drink"
            fi
            if [[ -n $toys ]] && [[ $toys != "exit" ]]; then
                echo "Toys: $toys"
            fi
            if [[ -n $clothes ]] && [[ $clothes != "exit" ]]; then
                echo "Clothes: $clothes"
            fi
            read -p "Press enter to send order." # read the input and store it in the variable
            echo "Order sent"
            exit
            break
            ;;
        "exit")
            echo "Thank you for using the Order Program."
            break
            ;;
        *) # default case
            echo "Invalid option, please try again."
            echo "Welcome to the Order Program, please select an option from the menu below."
            ;;

esac
done
