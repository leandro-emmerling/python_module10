#!/usr/bin/env python3


import time
import random
from functools import wraps
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    """Time execution decorator that measures execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {(end - start):.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball(target: str, power: int) -> str:
    """Function call that points to wrapper function"""
    time.sleep(0.1)
    return f"Fireball hits {target} for {power} damage"


def power_validator(min_power: int) -> Callable:
    """Parameterized validation decorator"""
    def decorator(func: Callable) -> Callable:
        """Decorator Factory that validates power level"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[0] < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


@power_validator(20)
def damage_spell(power: int, target: str) -> str:
    """Cast a damage spell on target"""
    return f"Casts at {target} with {power} power"


def retry_spell(max_attempts: int) -> Callable:
    """Retry decorator that retries failed spells"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@retry_spell(3)
def unstable_spell() -> str:
    """A spell that sometimes fails."""
    if random.random() < 0.7:
        raise RuntimeError("Spell misfired!")
    return "Waaaaagh spelled !"


class MageGuild:
    """Guild of mages with validation and casting abilities."""
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check that name has at least 3 chars and only letters/spaces."""
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell, validated through power_validator."""
        @power_validator(10)
        def do_cast(p: int, name: str) -> str:
            return f"Successfully cast {name} with {p} power"
        return do_cast(power, spell_name)


if __name__ == "__main__":
    print("Testing spell timer...")
    result = fireball("Dragon", 50)
    print(f"Result: {result}")

    print("\nTesting power validator...")
    print(damage_spell(50, "Dragon"))
    print(damage_spell(5, "Goblin"))

    print("\nTesting retrying spell...")
    print(unstable_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Josh"))
    print(MageGuild.validate_mage_name("ET"))
    print(MageGuild.validate_mage_name("John Snow"))
    print(MageGuild.validate_mage_name("John 42"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Blow", 2))
