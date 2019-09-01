#include "pch.h"
#include "TestClass.h"

int TestClass::func1(int i)
{
	return i;
}

int TestClass::func2(int (*callback)(int), int i)
{
	return callback(i);
}

int TestClass::func3(int i)
{
	auto sum = 0;
	for (auto x = 0; x < i; ++x)
	{
		sum += x;
	}
	return sum;
}
