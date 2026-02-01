// Simple C extension module for testing MSVC builds

#include <Python.h>

static PyObject* add(PyObject *self, PyObject *args) {
    int a, b;

    if (!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;

    return PyLong_FromLong(a + b);
}

static PyMethodDef module_methods[] = {
    {"add", add, METH_VARARGS, "Add two integers and return the result."},
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef module_def = {
    PyModuleDef_HEAD_INIT,
    "module",
    "Test module for MSVC builds",
    -1,
    module_methods,
};

PyMODINIT_FUNC PyInit_module(void) {
    return PyModule_Create(&module_def);
}
