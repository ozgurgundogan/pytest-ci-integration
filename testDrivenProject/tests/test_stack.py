from src.stack import Stack


def test_constructor():
    s = Stack()
    assert isinstance(s, Stack), "Stack can not be constructed."


def test_push():
    s = Stack()
    s.push(4)
    assert len(s) == 1, "Value can not be pushed."


def test_push_string():
    s = Stack()
    s.push("str")
    assert len(s) == 0, "Value can not be pushed."


def test_push_float():
    s = Stack()
    s.push(float(31.1))
    assert len(s) == 0, "Value can not be pushed."


def test_pop():
    s = Stack()
    v = 4
    s.push(v)
    assert s.pop() == v, "Value can not be pushed or popped."
