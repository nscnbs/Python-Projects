// gcc -I/usr/include/python3.10 c_wrapper_rec.c -o c_wrapper_rec -lpython3.10

#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Funkcja pomocnicza do konwersji obiektu Pythona DiofanticResult na strukturę C
typedef struct
{
    int x;
    int y;
} DiofanticResult;

DiofanticResult convert_to_diofantic_result(PyObject *result_obj)
{
    DiofanticResult result;
    PyObject *x_obj = PyObject_GetAttrString(result_obj, "x");
    PyObject *y_obj = PyObject_GetAttrString(result_obj, "y");
    result.x = PyLong_AsLong(x_obj);
    result.y = PyLong_AsLong(y_obj);
    Py_DECREF(x_obj);
    Py_DECREF(y_obj);
    return result;
}

// Wrapper dla funkcji factorial
int factorial_wrapper(int n)
{
    PyObject *pName, *pModule, *pFunc, *pArgs, *pValue;

    // Inicjalizacja interpretera Pythona
    Py_Initialize();

    // Dodanie ścieżki do katalogu zawierającego moduł library_loop.py
    PyObject *sys = PyImport_ImportModule("sys");
    PyObject *path = PyObject_GetAttrString(sys, "path");
    PyList_Append(path, PyUnicode_FromString("/home/nscnbs/jpp/lista1/Python"));
    Py_DECREF(sys);
    Py_DECREF(path);

    // Import modułu library_loop
    pName = PyUnicode_DecodeFSDefault("library_rec");
    pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule != NULL)
    {
        // Odnalezienie funkcji factorial w module
        pFunc = PyObject_GetAttrString(pModule, "factorial");

        if (pFunc && PyCallable_Check(pFunc))
        {
            // Przygotowanie argumentów funkcji
            pArgs = PyTuple_New(1);
            PyTuple_SetItem(pArgs, 0, PyLong_FromLong(n));

            // Wywołanie funkcji factorial
            pValue = PyObject_CallObject(pFunc, pArgs);
            Py_DECREF(pArgs);

            // Konwersja wyniku na wartość typu int
            int result = PyLong_AsLong(pValue);
            Py_DECREF(pValue);
            Py_DECREF(pFunc);
            Py_DECREF(pModule);

            // Zamknięcie interpretera Pythona
            Py_Finalize();

            return result;
        }
        else
        {
            if (PyErr_Occurred())
                PyErr_Print();
            fprintf(stderr, "Cannot find function \"factorial\"\n");
        }
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
    }
    else
    {
        PyErr_Print();
        fprintf(stderr, "Failed to load \"library_rec\" module\n");
    }
    // Zamknięcie interpretera Pythona w przypadku błędu
    Py_Finalize();
    // Zwrócenie wartości domyślnych w przypadku błędu
    return -1;
}

// Wrapper dla funkcji nwd
int nwd_wrapper(int a, int b)
{
    PyObject *pName, *pModule, *pFunc, *pArgs, *pValue;

    // Inicjalizacja interpretera Pythona
    Py_Initialize();

    // Dodanie ścieżki do katalogu zawierającego moduł library_loop.py
    PyObject *sys = PyImport_ImportModule("sys");
    PyObject *path = PyObject_GetAttrString(sys, "path");
    PyList_Append(path, PyUnicode_FromString("/home/nscnbs/jpp/lista1/Python"));
    Py_DECREF(sys);
    Py_DECREF(path);

    // Import modułu library_loop
    pName = PyUnicode_DecodeFSDefault("library_rec");
    pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule != NULL)
    {
        // Odnalezienie funkcji nwd w module
        pFunc = PyObject_GetAttrString(pModule, "nwd");

        if (pFunc && PyCallable_Check(pFunc))
        {
            // Przygotowanie argumentów funkcji
            pArgs = PyTuple_New(2);
            PyTuple_SetItem(pArgs, 0, PyLong_FromLong(a));
            PyTuple_SetItem(pArgs, 1, PyLong_FromLong(b));

            // Wywołanie funkcji nwd
            pValue = PyObject_CallObject(pFunc, pArgs);
            Py_DECREF(pArgs);

            // Konwersja wyniku na wartość typu int
            int result = PyLong_AsLong(pValue);
            Py_DECREF(pValue);
            Py_DECREF(pFunc);
            Py_DECREF(pModule);

            // Zamknięcie interpretera Pythona
            Py_Finalize();
            return result;
        }
        else
        {
            if (PyErr_Occurred())
                PyErr_Print();
            fprintf(stderr, "Cannot find function \"nwd\"\n");
        }
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
    }
    else
    {
        PyErr_Print();
        fprintf(stderr, "Failed to load \"library_rec\" module\n");
    }
    // Zamknięcie interpretera Pythona w przypadku błędu
    Py_Finalize();
    // Zwrócenie wartości domyślnych w przypadku błędu
    return -1;
}

// Wrapper dla funkcji diofantic
DiofanticResult diofantic_wrapper(int a, int b, int c)
{
    PyObject *pName, *pModule, *pFunc, *pArgs, *pValue;

    // Inicjalizacja interpretera Pythona
    Py_Initialize();

    // Dodanie ścieżki do katalogu zawierającego moduł library_loop.py
    PyObject *sys = PyImport_ImportModule("sys");
    PyObject *path = PyObject_GetAttrString(sys, "path");
    PyList_Append(path, PyUnicode_FromString("/home/nscnbs/jpp/lista1/Python"));
    Py_DECREF(sys);
    Py_DECREF(path);

    // Import modułu library_loop
    pName = PyUnicode_DecodeFSDefault("library_rec");
    pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule != NULL)
    {
        // Odnalezienie funkcji diofantic w module
        pFunc = PyObject_GetAttrString(pModule, "diofantic");

        if (pFunc && PyCallable_Check(pFunc))
        {
            // Przygotowanie argumentów funkcji
            pArgs = PyTuple_New(3);
            PyTuple_SetItem(pArgs, 0, PyLong_FromLong(a));
            PyTuple_SetItem(pArgs, 1, PyLong_FromLong(b));
            PyTuple_SetItem(pArgs, 2, PyLong_FromLong(c));

            // Wywołanie funkcji diofantic
            pValue = PyObject_CallObject(pFunc, pArgs);
            Py_DECREF(pArgs);

            // Konwersja wyniku na strukturę DiofanticResult
            DiofanticResult result = convert_to_diofantic_result(pValue);
            Py_DECREF(pValue);
            Py_DECREF(pFunc);
            Py_DECREF(pModule);

            // Zamknięcie interpretera Pythona
            Py_Finalize();

            return result;
        }
        else
        {
            if (PyErr_Occurred())
                PyErr_Print();
            fprintf(stderr, "Cannot find function \"diofantic\"\n");
        }
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
    }
    else
    {
        PyErr_Print();
        fprintf(stderr, "Failed to load \"library_rec\" module\n");
    }
    // Zamknięcie interpretera Pythona w przypadku błędu
    Py_Finalize();
    // Zwrócenie wartości domyślnych w przypadku błędu
    return (DiofanticResult){-1, -1};
}

int main()
{
    printf("C WRAPPER PYTHON REKURSJA");
    // Przykładowe użycie wrappera dla funkcji factorial
    int n = 5;
    printf("%d! = %d\n", n, factorial_wrapper(n));

    // Przykładowe użycie wrappera dla funkcji nwd
    int num1 = 36, num2 = 48;
    printf("NWD: %d i %d = %d\n", num1, num2, nwd_wrapper(num1, num2));

    // Przykładowe użycie wrappera dla funkcji diofantic
    int a = 120, b = 144, c = 72;
    DiofanticResult result = diofantic_wrapper(a, b, c);
    if (result.x != -1 && result.y != -1)
    {
        printf("Rozwiązanie równania %dx + %dy = %d to x = %d, y = %d\n", a, b, c, result.x, result.y);
    }
    else
    {
        printf("Brak rozwiązania dla równania %dx + %dy = %d\n", a, b, c);
    }
    return 0;
}