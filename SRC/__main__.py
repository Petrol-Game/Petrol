#this launches the code without error prevention, THIS SHOULD ALWAYS BE FALSE IN RELEASE, BETA AND ALPHA VERSIONS
DODGY_LAUNCH = False

if DODGY_LAUNCH:
    print()
    print("Loading Petrol, Dodgy")
    print()

    import petrol
else:
    load = "Y"

    while load.upper() == "Y":
        try:
            print()
            print("Loading Petrol")
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