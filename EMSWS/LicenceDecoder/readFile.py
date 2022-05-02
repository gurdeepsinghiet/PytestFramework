from ctypes import POINTER, Structure, py_object, pythonapi, cdll
import sys, string, os
# give location of dll
#https://nullprogram.com/blog/2021/05/31/
def lrsvrcDecoder():
    mydll = cdll.LoadLibrary("filedecoder.dll")
    result1= mydll.fileDecode()
    return result1

lrsvrcDecoder()






