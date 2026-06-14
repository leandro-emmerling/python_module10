#!/usr/bin/env python3


from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Combine two spells into one that calls both."""
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a new spell where power is multiplied before casting."""
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Cast spell only if condition returns True."""
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """Cast all spells in order with the same arguments."""
    def sequence(target: str, power: int) -> list:
        return [s(target, power) for s in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    """Cast a fireball spell."""
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    """Cast a heal spell."""
    return f"Heal restores {target} for {power} HP"


if __name__ == "__main__":
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 50)
    print(result)

    print("\nTesting power amplifier...")
    mega = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega('Dragon', 10)}")

    print("\nTesting conditional caster...")
    strong_only = conditional_caster(lambda t, p: p >= 20, fireball)
    print(strong_only("Dragon", 50))
    print(strong_only("Dragon", 5))

    print("\n Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 30))
