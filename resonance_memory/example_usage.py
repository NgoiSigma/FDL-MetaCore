from resonance_memory.memory_core import ResonanceMemory

memory = ResonanceMemory()
memory.remember("Истина — в балансе.", "Синтез(Истина ∧ Баланс)", 3, tags=["этика", "основы"])
memory.remember("Мир держится на честных людях.", "Синтез(Мир ∧ Честность)", 2, tags=["социум"])

print("🧠 Последние воспоминания:")
for r in memory.latest():
    print(r)
