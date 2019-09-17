#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - prints some info about list
 * @p: pointer to PyObject struct
 */
void print_python_list_info(PyObject *p)
{
	int i;
	long int size = PyList_Size(p);
	long int allocated = ((PyListObject*)(p))->allocated;
	
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", allocated);
	for (i = 0; i < size; i++)
		{
			temp = PyList_GetItem(p, i);
			printf("Element %d: %s\n", i, Py_TYPE(temp)->tp_name);
		}
}
