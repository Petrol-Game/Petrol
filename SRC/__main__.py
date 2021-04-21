#this file handles the launching of the code
#changes should only be made to this if neccesary

DODGY_LAUNCH = False #this launches the code without error prevention, THIS SHOULD ALWAYS BE FALSE IN RELEASE, BETA AND ALPHA VERSIONS


DEBUG = False # adds option to reload scripts when keyboard interrupt given, should be false in all published versions

def DODGY():
    print()
    print("Launching Petrol, DODGY; ALL ERRORS WILL NOT BE RESOLVED")
    print()

    import petrol

def launch():
    try:
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
    except KeyboardInterrupt:
        #catches terminal keybard interupt, so that you dont get an error message

        if DEBUG:
            if input("Do you want to relaunch? ").upper() == "Y":
                launch()
            else:
                print()
                print("Exiting...")
                print()
        else:
            print()
            print("Exiting...")
            print()

launch()
