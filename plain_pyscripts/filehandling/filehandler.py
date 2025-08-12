import subprocess
import os

def py_to_txt(py_path: str, delete_original: bool = False) -> None:
    """
    Convert a .py file to a text file with .txt extension.

    Parameters:
        py_path: The path to where the .py file is found
        delete_original: If True, delete the original .py file
    """
    assert isinstance(py_path, str), "py_path is not a string"
    assert type(delete_original) == bool, "delete_original is not a bool"

    pystring = ''

    try:
        with open(py_path, 'r') as pyfile:
            pystring = pyfile.read()
    except Exception as e:
        print(e)
        return
    
    txt_directory = py_path[:py_path.rfind('\\') + 1] + 'demotxt.txt'
    
    with open(txt_directory, 'w') as txtfile:
        txtfile.write(pystring)

    if (delete_original):
        os.remove(py_path)

    print('Py to Txt Conversion is Complete!')

def txt_to_py(txt_path: str, delete_original: bool = False) -> None:
    """
    Convert a .txt file to a text file with .py extension.

    Parameters:
        txt_path: The path to where the .txt file is found
        delete_original: If True, delete the original .txt file
    """
    assert isinstance(txt_path, str), "txt_path is not a string"
    assert type(delete_original) == bool, "delete_original is not a bool"

    txtstring = ''

    try:
        with open(txt_path, 'r') as txtfile:
            txtstring = txtfile.read()
    except Exception as e:
        print(e)
        return
    
    py_directory = txt_path[:txt_path.rfind('\\') + 1] + 'demopy.py'

    with open(py_directory, 'w') as pyfile:
        pyfile.write(txtstring)

    if (delete_original):
        os.remove(txt_path)

    print('Txt to Py Conversion is Complete!')
    
if __name__ == '__main__':
    path = input('Path for Txt to Py: ')
    txt_to_py(path, True)