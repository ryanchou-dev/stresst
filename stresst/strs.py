import argparse
import os
import subprocess


def main():
    prser = argparse.ArgumentParser(description="stress test a program with multiple inputs")
    prser.add_argument("file", metavar="prgm.py", type=str, nargs=1, help="program to test")
    prser.add_argument("test", metavar="testdir", type=str, nargs=1, help="directory of test cases")

    args = prser.parse_args()

    wa = True
    if (os.path.exists(os.path.join(os.path.abspath(os.getcwd()), str(args.file[0])))
            and os.path.exists(os.path.join(os.path.abspath(os.getcwd()), str(args.test[0])))):
        wa = False
        for sb, _, f in os.walk(os.path.join(os.path.abspath(os.getcwd()), str(args.test[0]))):
            for i in f:
                pth = sb + os.sep + i
                if pth.endswith(".in"):
                    with open(pth, "r", encoding="utf-8") as fin:
                        p = subprocess.Popen(["python", str(args.file[0])], stdin=fin, stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
                        out, err = p.communicate()
                        if not err:
                            out = out.decode("utf-8").strip()
                            arr = [o for o in os.listdir(str(args.test[0]))]

                            fn = i[:i.index(".")] + ".out"

                            if fn not in arr:
                                print("no output file for", i)
                                break

                            of = open(sb + os.sep + fn, "r", encoding="utf-8")

                            if out != of.read().strip():
                                print("Wrong Answer on", i)
                                wa = True
                                break
                        else:
                            print("Runtime Error on", i)
                            wa = True
                            break
    else:
        print("Files not found")
    if not wa:
        print("All cases passed.")
