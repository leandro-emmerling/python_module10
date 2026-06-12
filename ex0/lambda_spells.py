#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by power level, descending."""
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Find mages with power >= min_power"""
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Add '* ' prefix and ' *' suffix to the spell names"""
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate max, min and average power of all mages."""
    return {
        'max_power': max(mages, key=lambda x: x['power'])['power'],
        'min_power': min(mages, key=lambda x: x['power'])['power'],
        'avg_power': round(sum(map(
            lambda x: x['power'], mages)) / len(mages), 2)
    }


if __name__ == "__main__":
    artifacts: list[dict] = [
        {'name': 'Staff', 'power': 89, 'type': 'Fire'},
        {'name': 'Orb', 'power': 97, 'type': 'Crystal'},
        {'name': 'Sword', 'power': 94, 'type': 'Ice'}
    ]
    mages: list[dict] = [
        {'name': 'Peter', 'power': 99, 'element': 'Earth'},
        {'name': 'Tom', 'power': 77, 'element': 'Wind'},
        {'name': 'Alexandra', 'power': 86, 'element': 'Water'},
        {'name': 'Brenda', 'power': 91, 'element': 'Fire'}
    ]
    spells: list[str] = [
        "fireball", "heal", "shield", "watersplash"
    ]

    print("\nTesting artifact sorter...")
    s_a = artifact_sorter(artifacts)
    print(f"{s_a[0]['type']} {s_a[0]['name']} ({s_a[0]['power']} power)"
          f" comes before {s_a[1]['type']} {s_a[1]['name']}"
          f" ({s_a[1]['power']} power)")

    print("\nTesting power filter")
    p_f = power_filter(mages, 90)
    print("The following mages have more/equal power to 90:")
    for mage in p_f:
        print(f"- {mage['name']}")

    print("\nTesting spell transformer")
    s_t = spell_transformer(spells)
    for spell in s_t:
        print(spell, end=" ")
    print()
    print("\nTesting mage stats")
    m_s = mage_stats(mages)
    print(f"Max power: {m_s['max_power']}")
    print(f"Min power: {m_s['min_power']}")
    print(f"Average power: {m_s['avg_power']}")
