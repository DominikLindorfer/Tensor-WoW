import glv
import file1
import file2


def showData():
    print(f"*****initial global variable values*****\n"
          f"glvB={glv.glvB}\n"
          f"glvA={glv.glvA}\n"
          f"glvS={glv.glvS}\n"
          f"glvList={glv.glvList}\n"
          f"glvTuple={glv.glvTuple}\n"
          f"glvDict={glv.glvDict}\n")

def changeData():
    glv.glvB = "Domi"
    glv.glvA = 1
    glv.glvS = "Domi2"
    glv.glvList = [4, 5, 6]
    glv.glvTuple = (2, "Domi3")
    glv.glvDict = {"Name": "bactone", "age": 0}

showData()  # show initial global variable
file1.showData()  # show global variable in sub1
file1.changeData()  # change global variable in sub1
file2.showData()  # show global variable in sub2
file2.changeData()  # change global variable in sub2
file1.showData()  # show global variable in sub1 again

changeData()
showData()  # show initial global variable
