def is_attribute(cls: object, attribute: str) -> bool:
    return attribute in cls.__dict__
