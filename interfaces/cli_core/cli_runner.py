# interfaces/cli_core/cli_runner.py

import argparse
from sigma_avatarus import SigmaAvatarus
from fdl_agent_kernel.logic_core import FDLKernel
from modules.Δψ_monitor.lie_tension_analyzer import analyze_tension

def main():
    parser = argparse.ArgumentParser(description="FDL-MetaCore CLI Interface")
    parser.add_argument("phrase", type=str, help="Введите утверждение для анализа")
    args = parser.parse_args()

    avatar = SigmaAvatarus()
    kernel = FDLKernel()

    print("\n🌀 Σ-FDL :: CLI Resonance Interface")
    print("----------------------------------")

    resonance = avatar.resonate(args.phrase)
    synthesis = kernel.analyze(args.phrase, resonance)
    tension = analyze_tension(args.phrase)

    print(f"\n🧠 Резонансный отклик: {resonance}")
    print(f"⚙️ Синтез логики: {synthesis}")
    print(f"💥 Уровень напряжения лжи: {tension}/10\n")

    if tension >= 7:
        print("⚠️ ВНИМАНИЕ: Высокая вероятность дезинформации.")
    elif tension >= 4:
        print("ℹ️ Средний уровень — требуется критический подход.")
    else:
        print("✅ Устойчивое утверждение — логически приемлемо.")

if __name__ == "__main__":
    main()
