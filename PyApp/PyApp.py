# coding: utf-8
from typing import *
import ctypes
import multiprocessing.pool
import io
import struct


dll = ctypes.CDLL('CppDll.dll')


class PyTestClass(object):

    func2_callback = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int)

    def __init__(self):
        self.__instance = dll.TestClass_New()

    def __del__(self):
        try:
            dll.TestClass_Delete(self.__instance)
        except OSError as e:  # __del__ がインタプリタ終了中に呼ばれると dll に対する AccessViolation が起きる
            pass

    def func1(self, i):
        # type: (int) -> int
        return dll.TestClass_func1(self.__instance, i)

    def func2(self, callback, i):
        # type: (Callable[[int], int], int) -> int
        return dll.TestClass_func2(self.__instance, PyTestClass.func2_callback(callback), i)

    def func3(self, i):
        return dll.TestClass_func3(self.__instance, i)


class TestBase(ctypes.Structure):

    _fields_ = [
        ('x', ctypes.c_int32),
        ('y', ctypes.c_int32),
        ]


def main():
    dst_buffer = bytearray(ctypes.sizeof(TestBase))
    dll.test.argtypes = (ctypes.c_void_p, ctypes.c_int32, ctypes.c_int32)

    dst_type = ctypes.c_char * ctypes.sizeof(TestBase)
    dll.test(dst_type.from_buffer(dst_buffer), 0, ctypes.sizeof(TestBase))

    dst = TestBase.from_buffer(dst_buffer)
    print '====='
    print dst.x, dst.y
    print '====='

    obj = PyTestClass()
    print(obj.func1(1))
    print(obj.func2(lambda x: x + 2, 1))

    #thread_count=multiprocessing.cpu_count()
    #tasks = []
    #pool = multiprocessing.pool.ThreadPool(processes=thread_count)
    #for i in range(10000):
    #    task = pool.apply_async(obj.func3, [100000000])
    #    tasks.append(task)

    #for task in tasks:
    #    task.wait()

if __name__ == '__main__':
    main()
    ctypes.windll.kernel32.FreeLibrary.argtypes = [ctypes.wintypes.HMODULE]
    ctypes.windll.kernel32.FreeLibrary(dll._handle)
