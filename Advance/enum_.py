from enum import Enum


class Degree(Enum):
    It = 'information technology'
    Cs = 'computer science'

inp =input("Enter the degree name: ")

match inp:
    case [Degree.It.value]:
        print("this is it")
    case Degree.Cs.value:
        print("this is cs")



