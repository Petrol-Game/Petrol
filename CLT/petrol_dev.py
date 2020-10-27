#!/usr/bin/python3

import fire

import os

def main(name, url = "./", credit = "N/A"):
    workingdir = None

    if url[0] == ".":
        workingdir = os.getcwd() + url[0:0]+url[0+1:] + "/" + name
    else:
        workingdir = os.getcwd() + url + "/" + name

    os.mkdir(workingdir)

    print()
    print("Generating Files")
    print()

    info = open(workingdir + "/INFO.json", "w")
    info.write('{\n     "c":"' + credit + '",\n     "creedits":{}\n}')
    info.close()

    print("Generated INFO.json")

    mapp = open(workingdir + "/MAP.json", "w")
    mapp.write('{\n\n}')
    mapp.close()

    print("Generated MAP.json")

    setup = open(workingdir + "/setup.py", "w")
    setup.write('import petrolasset as asset\n\n')
    setup.close()

    print("Geneated setup.py")
    print()

    print("Done")

if __name__ == "__main__":
    fire.Fire(main)