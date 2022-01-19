import expyct


def test_instance_type_instanceof():
    """Tests that the Instance matcher can pretend to be an instance of another class."""
    instance = expyct.Instance(type=float)
    assert instance.__class__ == float
    assert isinstance(instance, float)


def test_instance_instance_of_instanceof():
    """Tests that the Instance matcher can pretend to be an instance of another class."""
    instance = expyct.Instance(instance_of=float)
    assert instance.__class__ == float
    assert isinstance(instance, float)
