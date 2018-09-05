# Space Fact
# Programed By Benjamin Park 2018

import sys
import os

version = "v 0.2"

# Clears the console when called
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Displays main menu when called
def main():
    clear()
    print("SPACE FACT    " + version)
    print("")
    print("What category would you like to look at?")
    print("")
    print("Planets (Sol System)")
    print("Stars")
    print("Galaxies")
    print("")
    print("Exit")
    print("")
    selected = input("")
    selected = selected.lower()

    if selected == "exit":
        sys.exit()
    elif selected == "planets":
        info_planet()
    elif selected == "stars":
        info_star()
    elif selected == "galaxies":
        info_galaxy()
    else:
        main()

# Handles Planet Category
def info_planet():
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
    print("Back")
    print("")
    selected = input("")
    selected = selected.lower()

    # Masive ladder of elif statments and mess of print statments
    # Checks input and shows facts of selected planet or calls itself
    if selected == "back":
        main()
    elif selected == "mercury":
        clear()
        print("Name: Mercury")
        print("Type: Planet")
        print("Diameter: 4,880 km")
        print("Moons: 0")
        print("Day Length: 58d 15h 30m")
        print("Fun Fact: Mercury does not have any seasons")
        print("")
        input("<ENTER> to return")
        info_planet()
    elif selected == "venus":
        clear()
        print("Name: Venus")
        print("Type: Planet")
        print("Diameter: 12,104 km")
        print("Moons: 0")
        print("Day Length: 116d 18h 0m")
        print("Fun Fact: Venus is the hottest planet in the solar system")
        print("")
        input("<ENTER> to return")
        info_planet()
    elif selected == "earth":
        clear()
        print("Name: Earth")
        print("Type: Planet (Terrestrial)")
        print("Diameter: 12,104 km")
        print("Moons: 1")
        print("Day Length: 24h")
        print("Fun Fact: 70% of the Earth is covered in water")
        print("")
        input("<ENTER> to return")
        info_planet()
    elif selected == "mars":
        clear()
        print("Name: Mars")
        print("Type: Planet (Terrestrial)")
        print("Diameter: 6,779 km")
        print("Moons: 2")
        print("Day Length: 1d 0h 37m")
        print("Fun Fact: Mars has seasons like Earth, but they last twice as long")
        print("")
        input("<ENTER> to return")
        info_planet()
    elif selected == "jupiter":
        clear()
        print("Name: Jupiter")
        print("Type: Planet (Jovian)")
        print("Diameter: 139,822 km")
        print("Moons: 79")
        print("Day Length: 9h 56m")
        print("Fun Fact: The great red spot is a gaint storm that has been going for over 150 years")
        print("")
        input("<ENTER> to return")
        info_planet()
    elif selected == "saturn":
        clear()
        print("Name: Saturn")
        print("Type: Planet (Jovian)")
        print("Diameter: 116,464 km")
        print("Moons: 62")
        print("Day Length: 10h 42m")
        print("Fun Fact: Saturn's rings are only 20 meters thick")
        print("")
        input("<ENTER> to return")
        info_planet()
    elif selected == "uranus":
        clear()
        print("Name: Uranus")
        print("Type: Planet (Jovian)")
        print("Diameter: 50,724 km")
        print("Moons: 27")
        print("Day Length: 17h 14m")
        print("Fun Fact: Uranus also has rings")
        print("")
        input("<ENTER> to return")
        info_planet()
    elif selected == "neptune":
        clear()
        print("Name: Neptune")
        print("Type: Planet (Jovian)")
        print("Diameter: 49,244 km")
        print("Moons: 14")
        print("Day Length: 16h 6m")
        print("Fun Fact: The surface temperature on Neptune is -214°C")
        print("")
        input("<ENTER> to return")
        info_planet()
    else:
        info_planet()

# Handels Star Category
def info_star ():
    clear()
    print("What Star would you like to look at?")
    print("")
    print("Sol")
    print("LH54-425")
    print("Proxima Centauri")
    print("")
    print("Back")
    print("")
    selected = input("")
    selected = selected.lower()

    # Masive ladder of elif statments and mess of print statments
    # Checks input and shows facts of selected star or calls itself
    if selected == "back":
        main()
    elif selected == "sol":
        clear()
        print("Name: Sol")
        print("Type: Star")
        print("Diameter: 1.39 million km")
        print("Planets: 8")
        print("Star Type: G-Type Main Sequence")
        print("Stars in System: 1")
        print("Fun Fact: Sol is the latin name for the Sun")
        print("")
        input("<ENTER> to return")
        info_star()
    elif selected == "lh54-425":
        clear()
        print("Name: LH54-425")
        print("Type: Binary Star System")
        print("Diameter: 11.12 & 15.29 million km")
        print("Planets: Unknown")
        print("Star Type: O-Type Main Sequences")
        print("Stars in System: 2")
        print("Fun Fact: The system is approaching us at around 300 km/s")
        print("")
        input("<ENTER> to return")
        info_star()
    elif selected == "proxima centauri":
        clear()
        print("Name: Proxima Centauri")
        print("Type: Star")
        print("Diameter: 11.12 & 15.29 million km")
        print("Planets: Unknown")
        print("Star Type: M-Type Main Sequence")
        print("Stars in System: 3")
        print("Fun Fact: Proxima Centauri is the closest known star to the Sun")
        print("")
        input("<ENTER> to return")
        info_star()
    else:
        info_star()

# Handles Galaxies Category
def info_galaxy ():
    clear()
    print("What Galaxy would you like to look at?")
    print("")
    print("Milkyway")
    print("Andromeda")
    print("")
    print("Back")
    print("")
    selected = input("")
    selected = selected.lower()

    # Masive ladder of elif statments and mess of print statments
    # Checks input and shows facts of selected galaxy or calls itself
    if selected == "back":
        main()
    elif selected == "milkyway":
        clear()
        print("Name: Milkyway")
        print("Type: Galaxy (Barred Spiral)")
        print("Diameter: 170,000 ly")
        print("Stars: 100–400 billion")
        print("Age: 13.51 billion years")
        print("Fun Fact: Our solar system is on the Orion Arm")
        print("")
        input("<ENTER> to return")
        info_galaxy()
    elif selected == "andromeda":
        clear()
        print("Name: Andromeda")
        print("Type: Galaxy (Elliptical)")
        print("Diameter: 220,000 ly")
        print("Stars: 1 trillion")
        print("Age: 10.01 billion years")
        print("Fun Fact: Andromeda will collide with the Milkyway in about 4 billion years")
        print("")
        input("<ENTER> to return")
        info_galaxy()

main()
