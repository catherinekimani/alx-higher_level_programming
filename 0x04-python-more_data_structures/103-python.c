#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - print python bytes
 * @p: object
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int length, idx, limits;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Objects \n");
		return;
	}
	length = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf(" size: %ld\n", length);
	printf(" trying string: %s\n", str);

	if (length >= 10)
		limits = 10;
	else
		limits = length + 1;
	printf(" first %ld bytes:", limits);
	for (idx = 0; idx < limits; idx++)
	{
		if (str[idx] >= 0)
			printf(" %02x", str[idx]);
		else
			printf(" %02x", 256 + str[idx]);
	}
	printf("\n");
}

/**
 * print_python_list - print python list
 * @p: object
 */
void print_python_list(PyObject *p)
{
	long int length, idx;
	PyObject *obj;
	PyListObject *list;

	length = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (idx = 0; idx < length; idx++)
	{
		obj = ((PyListObject *)p)->ob_item[idx];
		printf("Element %ld: %s\n", idx, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
