#!/usr/bin/env python3


from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total: int = initial_power

    def accumulate(add_power: int) -> int:
        nonlocal total
        total += add_power
        return total
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:

    def factory(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return factory


def memory_vault() -> dict[str, Callable]:
    storage: dict = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        if key in storage:
            return storage[key]
        return "Memory not found"
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()
    print("Testing spell accumulator...")
    counter_c = spell_accumulator(100)
    print(f"Base 100, add 20: {counter_c(20)}")
    print(f"Base 100, add 30: {counter_c(30)}")
    print()
    print("Testing enchantment factory...")
    item_1 = enchantment_factory("Flaming")
    item_2 = enchantment_factory("Frozen")
    print(item_1("Sword"))
    print(item_2("Shield"))
    print()
    print("Testing memory vault...")
    memory_1 = memory_vault()
    print("Store 'secret' = 42")
    memory_1["store"]("secret", 42)
    print(f"Recall 'secret': {memory_1['recall']('secret')}")
    print(f"Recall 'unknown': {memory_1['recall']('unknown')}")
