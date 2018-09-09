# Space Fact
# Programed By Benjamin Park 2018

import sys
import os
import json

version = "v 0.3"
ascii_logo = """
  ____                         _____          _
 / ___| _ __   __ _  ___ ___  |  ___|_ _  ___| |_
 \___ \| '_ \ / _` |/ __/ _ \ | |_ / _` |/ __| __|
  ___) | |_) | (_| | (_|  __/ |  _| (_| | (__| |_
 |____/| .__/ \__,_|\___\___| |_|  \__,_|\___|\__|
       |_|                                        """

# Clears the terminal when called
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Import Data
planets = open("Data/planets.json", "r")
stars = open("Data/stars.json", "r")
galaxies = open("Data/galaxies.json", "r")
spacecraft = open("Data/spacecraft.json", "r")

planet_data = json.load(planets)
star_data = json.load(stars)
galaxy_data = json.load(galaxies)
spacecraft_data = json.load(spacecraft)

planets.close()
stars.close()
galaxies.close()
spacecraft.close()

# Displays main menu when called
def main():
    clear()
    print(ascii_logo + "    " + version)
    print("")
    print(" What category would you like to look at?")
    print("")
    print(" Planets (Sol System)")
    print(" Stars")
    print(" Galaxies")
    print(" Spacecraft")
    print("")
    print("")
    print(" Exit")
    print("")
    selected = input(" ")
    selected = selected.lower()

    if selected == "exit":
        sys.exit()
    elif selected == "planets":
        info_planet()
    elif selected == "stars":
        info_star()
    elif selected == "galaxies":
        info_galaxy()
    elif selected == "spacecraft":
        info_spacecraft()
    else:
        main()

# Handles Planet Category
def info_planet():
    clear()
    print("")
    print(" What Planet would you like to look at?")
    print("")
    print(" Mercury")
    print(" Venus")
    print(" Earth")
    print(" Mars")
    print(" Jupiter")
    print(" Saturn")
    print(" Uranus")
    print(" Neptune")
    print("")
    print("")
    print(" Back")
    print("")
    selected = input(" ")
    selected = selected.lower()

    # Checks input and shows facts of selected planet or calls itself
    if selected == "back":
        main()
    else:
        try:
            clear()
            print("")
            print(" Name: " + planet_data[selected]["name"])
            print(" Type: " + planet_data[selected]["type"])
            print(" Diameter: " + planet_data[selected]["diameter"])
            print(" Moons: " + planet_data[selected]["moons"])
            print(" Fun Fact: " + planet_data[selected]["fun_fact"])
            print("")
            input(" <Enter> to return")
            info_planet()
        except KeyError:
            info_planet()

# Handels Star Category
def info_star ():
    clear()
    print("")
    print(" What Star would you like to look at?")
    print("")
    print(" Sol")
    print(" LH54-425")
    print(" Proxima Centauri")
    print(" Sagittarius A")
    print("")
    print(" Back")
    print("")
    selected = input(" ")
    selected = selected.lower()

    # Checks input and shows facts of selected star or calls itself
    if selected == "back":
        main()
    else:
        try:
            clear()
            print("")
            print(" Name: " + star_data[selected]["name"])
            print(" Type: " + star_data[selected]["type"])
            print(" Diameter: " + star_data[selected]["diameter"])
            print(" Planets: " + star_data[selected]["planets"])
            print(" Star Type: " + star_data[selected]["star_type"])
            print(" Stars in System: " + star_data[selected]["star_system"])
            print(" Fun Fact: " + star_data[selected]["fun_fact"])
            print("")
            input(" <Enter> to return")
            info_star()
        except KeyError:
            info_star()

# Handles Galaxies Category
def info_galaxy ():
    clear()
    print("")
    print(" What Galaxy would you like to look at?")
    print("")
    print(" Milkyway")
    print(" Andromeda")
    print("")
    print("")
    print(" Back")
    print("")
    selected = input(" ")
    selected = selected.lower()

    # Checks input and shows facts of selected galaxy or calls itself
    if selected == "back":
        main()
    else:
        try:
            clear()
            print("")
            print(" Name: " + galaxy_data[selected]["name"])
            print(" Type: " + galaxy_data[selected]["type"])
            print(" Diameter: " + galaxy_data[selected]["diameter"])
            print(" Stars: " + galaxy_data[selected]["stars"])
            print(" Age: " + galaxy_data[selected]["age"])
            print(" Fun Fact: " + galaxy_data[selected]["fun_fact"])
            print("")
            input(" <Enter> to return")
            info_galaxy()
        except KeyError:
            info_galaxy()

# Handles Spacecraft Category
def info_spacecraft ():
    clear()
    print("")
    print(" What Spacecraft would you like to look at?")
    print("")
    print(" Falcon 9")
    print(" Space Shuttle")
    print(" Soyuz")
    print("")
    print("")
    print(" Back")
    print("")
    selected = input(" ")
    selected = selected.lower()

    # Checks input and shows facts of selected galaxy or calls itself
    if selected == "back":
        main()
    else:
        try:
            clear()
            print("")
            print(" Name: " + spacecraft_data[selected]["name"])
            print(" Type: " + spacecraft_data[selected]["type"])
            print(" Crew: " + spacecraft_data[selected]["crew"])
            print(" First Launch: " + spacecraft_data[selected]["first_launch"])
            print(" Fun Fact: " + spacecraft_data[selected]["fun_fact"])
            print("")
            input(" <Enter> to return")
            info_spacecraft()
        except KeyError:
            info_spacecraft()


main()
