"""Simple module to record execution times."""

from time import time


class Clock:
    """Record execution time of function.
    Instance registration by function name.
    Report average of each set of records.
    """

    _known = {}

    @classmethod
    def provide(cls, name):
        """Provide clock for named function.
        If not already registered, create one.
        """
        if name not in cls._known:
            cls._known[name] = cls()
        return cls._known[name]

    def __init__(self):
        self.records = []

    def record(self, value):
        """Append value to record."""
        self.records.append(value)

    @classmethod
    def report(cls):
        """Print mean of each record."""
        records = {}
        for name, instance in cls._known.items():
            record = instance.records
            if record:
                records.update({name: (len(record), sum(record))})
        return records


def chrono(fun):
    """Clock decorator : register 'fun' execution times.
    Closure preserves method identity.
    """
    name = f"{fun.__module__} / {fun.__qualname__}"
    clock = Clock.provide(name)

    def timed(*args, **kwargs):
        before = time()
        value = fun(*args, **kwargs)
        now = time()
        clock.record(now - before)
        return value

    return timed
