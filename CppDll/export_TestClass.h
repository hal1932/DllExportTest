#pragma once

#include "TestClass.h"


DLL_API TestClass* TestClass_New() { return new TestClass(); }
DLL_API void TestClass_Delete(TestClass* self) { delete self; }
DLL_API int TestClass_func1(TestClass* self, int i) { return self->func1(i); }
DLL_API int TestClass_func2(TestClass* self, int (*callback)(int), int i) { return self->func2(callback, i); }
DLL_API int TestClass_func3(TestClass* self, int i) { return self->func3(i); }

