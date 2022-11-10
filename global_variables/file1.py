# sub1.py
import glv

def showData():
    print(f"*****glv in sub1*****\n"
          f"glvB={glv.glvB}\n"
          f"glvA={glv.glvA}\n"
          f"glvS={glv.glvS}\n"
          f"glvList={glv.glvList}\n"
          f"glvTuple={glv.glvTuple}\n"
          f"glvDict={glv.glvDict}\n")


def changeData():
    glv.glvB = False
    glv.glvA = 200
    glv.glvS = "bactone"
    glv.glvList = [4, 5, 6]
    glv.glvTuple = (2, "b")
    glv.glvDict = {"Name": "bactone", "age": 0}