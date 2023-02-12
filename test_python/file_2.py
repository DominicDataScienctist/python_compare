import numpy as np
import pandas as pd


def function_1(param_1, param_2):
    var1 = param_1 + 3
    var2 = param_2 * 4
    var3 = var1 / var2
    return var3


def function_4(param_1, param_2):

    var1 = param_1 + 3
    var2 = param_2 * 5
    var3 = var1 / var2
    return var3


def function_3(param_1, param_2, param4):
    var1 = param_1 + 3
    var2 = param_2 * 5
    var3 = var1 / var2
    var4 = var3 - param4
    return var3, var4
