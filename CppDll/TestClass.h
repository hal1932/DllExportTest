#pragma once
class TestClass
{
public:
	int func1(int i);
	int func2(int (*callback)(int), int i);
	int func3(int i);
};

