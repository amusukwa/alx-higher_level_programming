#include <Python.h>

void print_python_string(PyObject *p);

/**
 * print_python_string - Prints info on Python string objects.
 * @p: A PyObject string object.
 * Return: no return type.
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t size_str;
    PyBytesObject *bytes = (PyBytesObject *)p;

    fflush(stdout);

    printf("[.] string object info\n");
    if (PyUnicode_Check(p))
    {
        printf("  type: compact unicode object\n");
    }
    else if (strcmp(p->ob_type->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    size_str = ((PyVarObject *)p)->ob_size;
    printf("  length: %ld\n", size_str);

    printf("  value: %s\n", PyUnicode_AsUTF8(p));
}
