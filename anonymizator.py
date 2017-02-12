"""
@file anonymizator.py
@author CN
@date jan 2017

Script to update the first few tags in doclines : change author name, version
number and date.

"""

from glob import glob


def get_all_python_files(folder):
    path = "/*.py"
    res = []
    tmp = glob(folder + path)
    while tmp:
        res += tmp
        path = "/*" + path
        tmp = glob(folder + path)
    return res

# fichiers = glob(FOLDER + "/*.py") + glob(FOLDER + "/*/*.py") + glob(FOLDER + "/*/*/*.py")
# print(fichiers)

def refactor(fname, doclines):
    res = ""
    begin_doc = False
    end_doc = False
    with open(fname, 'r') as f:
        lines = f.read().split("\n")
        i = 0
        while i < len(lines):
            # print(lines[i])
            if lines[i].startswith("\"\"\"") and not end_doc:
                begin_doc = True
                # print("Begin doc")
                res += lines[i] + "\n"
            elif begin_doc and not end_doc and lines[i].startswith("@"):
                pass
            elif begin_doc and not lines[i].startswith("@") and not end_doc:
            # elif begin_doc and not end_doc: # and not line.startswith("@"):
                end_doc = True
                # res += "\"\"\"\n"
                if fname.endswith("__init__.py") and len(fname.split("/")) > 1:
                    res += "@package " + fname.split("/")[-2] + "\n"
                else:
                    res += "@file " + fname + "\n"
                for l in doclines:
                    res += l + "\n"
                res += "\n"
            else:
                res += lines[i] + "\n"
            i += 1
    return res



if __name__ == "__main__":
    # print(get_all_python_files(FOLDER))
    # f = get_all_python_files(FOLDER)[1]
    # print(refactor(f, ["@version 1.0", "@author CN", "@author Gudule", "@date dec 2016"]))

    for fname in get_all_python_files("src"):
        ref = refactor(fname, ["@version 1.0", "@author CN", "@author Gudule", "@date fev 2017"])
        with open(fname, 'w') as f:
            f.write(ref)
        print("Rewrote file : " + fname)
    print("Done !")
