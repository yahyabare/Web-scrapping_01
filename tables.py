from tkinter import *
import csv


def create_standard_table(f, window):
    handle = csv.reader(f)
    length = len(next(handle))
    lengths = [0] * length
    for record in handle:

        for p,column in enumerate(record):
            if len(column) > lengths[p]:
                lengths[p] = len(column)+3

    f.seek(0)
    trow = 0
    table = Frame(window)
    for record in handle:
        for w,column in enumerate(record):
            Label(table,text=column,width=lengths[w],borderwidth=2,relief="groove",justify=LEFT,anchor=W, background='white').grid(column=w,row=trow,sticky=W)

        trow+=1

    return table
