#!/usr/bin/env python3


from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers with min, max and functools: add, mul"""
    if not spells:
        return 0
    operations: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create partial applications to create multiple versions"""
    fire_enchant = partial(base_enchantment, 50, "Fire")
    ice_enchant = partial(base_enchantment, 50, "Ice")
    air_enchant = partial(base_enchantment, 50, "Air")
    return {"fire": fire_enchant, "ice": ice_enchant, "air": air_enchant}


def base_enchantment(power: int, element: str, target: str) -> str:
    """Helper function for partial_enchanter to return the correct output"""
    return f"{element} enchantment ({power} power) on {target}"


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number with cached recursive computation."""
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable:
    """Handles multiple types from spell input"""
    @singledispatch
    def dispatch(spell) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":

    print("\nTesting spell reducer...")
    spells: list[int] = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")

    print("\nTesting partial enchanter...")
    enchants = partial_enchanter(base_enchantment)
    print(enchants["fire"]("Sword"))
    print(enchants["ice"]("Axe"))
    print(enchants["air"]("Wand"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Fib(20): {memoized_fibonacci(20)}")
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast([1, 2, 3]))
    print(cast(3.14))
