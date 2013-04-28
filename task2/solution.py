import functools
import collections
from collections import defaultdict
from collections import OrderedDict


def comp(f, g):
    return lambda n: f(g(n))


def iterate(func):
    f = lambda n: n
    yield f
    deque_ = collections.deque()
    deque_.appendleft(f)
    while True:
        deque_.appendleft(func)
        yield functools.reduce(comp, deque_)


def groupby(func, seq):
    result = defaultdict(list)
    for elem in seq:
        result[func(elem)].append(elem)
    return result


def zip_with(func, *iterables):
    count_of_iterables = len(iterables)
    if not count_of_iterables:
        return
    else:
        length_ = len(iterables[0])
        for i in range(0, count_of_iterables):
            if len(iterables[i]) < length_:
                length_ = len(iterables[i])
        for j in range(0, length_):
            my_list = []
            for i in range(0, count_of_iterables):
                my_list.append(iterables[i][j])
            yield func(*my_list)


class Function:
    current_size_of_cashe = 0
    max_size = 0
    arguments_and_results = OrderedDict()

    def are_args_called(self, args):
        if args in self.arguments_and_results.keys():
            return self.arguments_and_results[args]
        else:
            return False

    def add_call_with_args(self, args, f_):
        if (self.max_size > self.current_size_of_cashe):
            self.current_size_of_cashe += 1
        else:
            self.arguments_and_results.popitem(last=False)
        self.arguments_and_results[args] = f_(*args)


def cache(func, cache_size):
    f = Function()
    f.current_size_of_cache = 0
    f.arguments_and_results = OrderedDict()
    f.max_size = cache_size

    def cache_func(*args):
        args_used = f.are_args_called(args)
        if args_used:
            return f.arguments_and_results[args]
        else:
            f.add_call_with_args(args, func)
            return f.arguments_and_results[args]
    return cache_func
