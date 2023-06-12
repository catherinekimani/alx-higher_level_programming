#include <Python.h>
/**
 * print_python_list_info - print some basic info about python lists
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, idx;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (idx = 0; idx < size; idx++)
	{
		printf("Element %d: ", idx);
		obj = PyList_GetItem(p, idx);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
