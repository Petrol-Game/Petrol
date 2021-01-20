#this file handles the launching of the code
#changes should only be made to this if neccesary

DODGY_LAUNCH = True #this launches the code without error prevention, THIS SHOULD ALWAYS BE FALSE IN RELEASE, BETA AND ALPHA VERSIONS

def DODGY():
    print()
    print("Launching Petrol, DODGY")
    print()

    import petrol

if DODGY_LAUNCH:
    DODGY()
else:
    load = "Y"

    while load.upper() == "Y":
        try:
            print()
            print("Launching Petrol")
            print()

            import petrol

            load = "N"
        except Exception as e:
            print("ERROR")
            print()

            print(e.__str__())

            print()
            print("If this is an ongoing issue, please reinstall the software, then if it still happens report it on the Github repository. Thank you")
            print()

            print("Do you want to reload? [Y/N]")
            print()

            load = input("? ")

            print()

    if load.upper() == "DODGY":
        DODGY()
