# Модуль: Δψ_monitor (Сейсмограф Лжи)

## 📘 Назначение

`Δψ_monitor/` — это аналитический модуль мониторинга **напряжения лжи** и **социально-политических искажений**, выявляющий узлы противоречий в инфосреде и строящий модели риска на основе FDL-семантики.

---

## 🔍 Компоненты

### `lie_tension_analyzer.py`

- 🔹 Назначение: анализ плотности противоречий в текстовых/новостных потоках
- 🔹 Ключевые функции:
  - `detect_lie_pressure(text)`
  - `map_systemic_contradictions(text)`
- 💡 Пример:
  ```python
  from delta_psi_monitor.lie_tension_analyzer import detect_lie_pressure
  level = detect_lie_pressure(news_block)
