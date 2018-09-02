# Space Fact
# Programed By Benjamin Park 2018

import sys
import os

version = "v 0.1"

# Clears the console when called
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Displays main menu when called (also handels displaying planet info)
def main():
    clear()
    print("SPACE FACT    " + version)
    print("")
    print("What Planet would you like to look at?")
    print("")
    print("Mercury")
    print("Venus")
    print("Earth")
    print("Mars")
    print("Jupiter")
    print("Saturn")
    print("Uranus")
    print("Neptune")
    print("")
    selected = input("")

    # Make input string lowercase
    selected = selected.lower()

    # Masive ladder of elif statments and mess of print statments
    # Checks input and shows facts of selected planet or calls main function
    if selected == "exit":
        sys.exit()
    elif selected == "mercury":
        clear()
        print("Name: Mercury")
        print("Type: Planet")
        print("Diameter: 4,880 km")
        print("Day Length: 58d 15h 30m")
        print("")
        input("<ENTER> to return")
        main()
    elif selected == "venus":
        clear()
        print("Name: Venus")
        print("Type: Planet")
        print("Diameter: 12,104 km")
        print("Day Length: 116d 18h 0m")
        print("")
        input("<ENTER> to return")
        main()
    elif selected == "earth":
        clear()
        print("Name: Earth")
        print("Type: Planet (Terrestrial)")
        print("Diameter: 12,104 km")
        print("Day Length: 24h")
        print("")
        input("<ENTER> to return")
        main()
    elif selected == "mars":
        clear()
        print("Name: Mars")
        print("Type: Planet (Terrestrial)")
        print("Diameter: 6,779 km")
        print("Day Length: 1d 0h 37m")
        print("")
        input("<ENTER> to return")
        main()
    elif selected == "jupiter":
        clear()
        print("Name: Jupiter")
        print("Type: Planet (Jovian)")
        print("Diameter: 139,822 km")
        print("Day Length: 9h 56m")
        print("")
        input("<ENTER> to return")
        main()
    elif selected == "saturn":
        clear()
        print("Name: Saturn")
        print("Type: Planet (Jovian)")
        print("Diameter: 116,464 km")
        print("Day Length: 10h 42m")
        print("")
        input("<ENTER> to return")
        main()
    elif selected == "uranus":
        clear()
        print("Name: Uranus")
        print("Type: Planet (Jovian)")
        print("Diameter: 50,724 km")
        print("Day Length: 17h 14m")
        print("")
        input("<ENTER> to return")
        main()
    elif selected == "neptune":
        clear()
        print("Name: Neptune")
        print("Type: Planet (Jovian)")
        print("Diameter: 49,244 km")
        print("Day Length: 16h 6m")
        print("")
        input("<ENTER> to return")
        main()
    else:
        main()

main()
