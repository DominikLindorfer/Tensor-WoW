# sub2.py
import glv

def showData():
    print(f"*****glv in sub2*****\n"
          f"glvB={glv.glvB}\n"
          f"glvA={glv.glvA}\n"
          f"glvS={glv.glvS}\n"
          f"glvList={glv.glvList}\n"
          f"glvTuple={glv.glvTuple}\n"
          f"glvDict={glv.glvDict}\n")


def changeData():
    glv.glvB = True
    glv.glvA = 300
    glv.glvS = "bactone"
    glv.glvList = [7, 8, 9]
    glv.glvTuple = (3, "c")
    glv.glvDict = {"Name": "bactone1", "age": 10}