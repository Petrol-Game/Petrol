print()
print("Loading Petrol")
print()

try:
    import petrol
except Exception as e:
    print("ERROR")
    print()
    print(e.__str__())
    print()
    print("If this is an ongoing issue, please reinstall the software, then if it still happens report it on the Github repository. Thank you")