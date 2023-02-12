import importlib
import inspect
from os import getcwd
from os.path import join
import argparse


def is_mod_function(mod, func):
    ' checks that func is a function defined in module mod '
    return inspect.isfunction(func) and inspect.getmodule(func) == mod


def is_mod_class(mod, func):
    ' checks that func is a function defined in module mod '
    return inspect.isclass(func) and inspect.getmodule(func) == mod


def is_mod_code(mod, func):
    ' checks that func is a function defined in module mod '
    return inspect.iscode(func) and inspect.getmodule(func) == mod


def list_codes(mod):
    ' list of functions defined in module mod'
    return [func.__name__ for func in mod.__dict__.values()
            if is_mod_code(mod, func)]


def list_functions(mod):
    ' list of functions defined in module mod'
    return [func.__name__ for func in mod.__dict__.values()
            if is_mod_function(mod, func)]


def list_classes(mod):
    ' list of functions defined in module mod'
    return [func.__name__ for func in mod.__dict__.values()
            if is_mod_class(mod, func)]


def get_lists_of_functions(file_paths):
    lists_of_functions = {}
    for file_path in file_paths:
        file_paths
        list_of_functions = list_functions(importlib.import_module(f'test_python.{fi}'))
        fn = file_path.split('\\')[-1]
        lists_of_functions[fn] = list_of_functions
    return lists_of_functions


def get_lists_of_classes(file_paths):
    lists_of_functions = {}
    for file_path in file_paths:
        list_of_functions = list_classes(importlib.import_module(f'test_python.{fi}'))
        fn = file_path.split('\\')[-1]
        lists_of_functions[fn] = list_of_functions
    return lists_of_functions


def get_all_function_info_from_module(file_path, args):
    fn = file_path.split('\\')[-1]
    module_name = fn.split('.')[0]
    list_of_functions = list_functions(importlib.import_module(f'{args.dir}.{module_name}'))

    # list_of_classes = list_classes(importlib.import_module(f'{args.dir}.{module_name}'))

    with open(file_path) as file:
        lines = [line.rstrip() for line in file]

        function_started = False
        class_started = False
        a_class = None
        a_function = []
        current_function = None
        functions = {}
        for line in lines:
            taken = False
            if 'def ' in line:
                if len(a_function) > 0:
                    functions[current_function] = a_function
                a_function = []
                for f in list_of_functions:
                    if f + '(' in line:
                        current_function = f
                if current_function is None:
                    raise ValueError
                if len(a_function) == 0:
                    a_function = [line]
                    a_class = None
                    function_started = True
                    class_started = False
                else:
                    a_function.append(line)
            elif 'def ' not in line and len(a_function) > 0:
                a_function.append(line)
            else:
                if function_started or class_started:
                    a_function.append(line)
                elif class_started:
                    a_class.append(line)

    functions[current_function] = a_function
    return functions


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', help='dir', required=True)
    parser.add_argument('-i', '--input', type=str, nargs='+', action='append', help='list_of_file')
    parser.add_argument('-f', '--fun', type=str, help='function to compare')
    args = parser.parse_args()
    parent_path = join(getcwd(), args.dir)
    file_paths = []
    for i in args.input:
        file_path = join(parent_path, i[0])
        file_paths.append(file_path)

    module_functions = {}
    for file_path in file_paths:
        module_functions[file_path] = get_all_function_info_from_module(file_path, args)

    print(module_functions)



