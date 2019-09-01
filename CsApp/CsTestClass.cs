using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace CsApp
{
    class CsTestClass : IDisposable
    {
        [DllImport("CppDll.dll")]
        static extern IntPtr TestClass_New();

        [DllImport("CppDll.dll")]
        static extern void TestClass_Delete(IntPtr self);

        [DllImport("CppDll.dll")]
        static extern int TestClass_func1(IntPtr self, int i);

        delegate int TestClass_func2_Callback(int i);

        [DllImport("CppDll.dll")]
        static extern int TestClass_func2(IntPtr self, TestClass_func2_Callback callback, int i);

        public CsTestClass()
        {
            _self = TestClass_New();
        }

        ~CsTestClass()
            => Dispose(false);

        public void Dispose()
            => Dispose(true);

        private void Dispose(bool disposing)
        {
            if (_disposed)
            {
                return;
            }
            _disposed = true;

            if (_self != default)
            {
                TestClass_Delete(_self);
                _self = default;
            }

            if (disposing)
            { }
        }

        public int Func1(int i)
            => TestClass_func1(_self, i);

        public int Func2(Func<int, int> callback, int i)
            => TestClass_func2(_self, new TestClass_func2_Callback(callback), i);

        private bool _disposed;

        private IntPtr _self;
    }
}
