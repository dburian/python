#!/usr/bin/env python3
"""
    Size decorator
"""

class ForEach:
    def __init__(self, func, all_instances):
        super().__init__()
        self.func = func
        self.all_instances = all_instances
        #print(f'Func: {func}, All Inst: {all_instances}')

    def __get__(self, instance, owner):
        #print(f'Instance: {instance}, Owner: {owner}')
        if instance is None:
            return sum([self.func(inst) for inst in self.all_instances()])
        else:
            return self.func(instance)

def size(*, all_instances):
    def _size(func):
        return ForEach(func, all_instances)
    return _size

class Cache:
    def __init__(self):
        Cache._all_caches.append(self)
        self._storage = dict()

    _all_caches = []

    def set(self, key, value):
        self._storage[key] = value

    def get(self, key):
        self._storage[key]

    def _all_instances():
        return Cache._all_caches

    @size(all_instances = _all_instances)
    def entries_count(self):
        return len(self._storage)

a = Cache()
b = Cache()

a.set('a', 1)
a.set('b', 2)
b.set('c', 3)

print(a.entries_count)
print(b.entries_count)
print(Cache.entries_count)
