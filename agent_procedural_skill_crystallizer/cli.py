"""CLI for Skill Crystallizer."""
import argparse
from .core import ProceduralSkillCrystallizer, TrajectoryStep

def main():
    parser = argparse.ArgumentParser(description="Agent Procedural Skill Crystallizer CLI")
    parser.add_argument("--demo", action="store_true", help="Run crystallizer demo")
    args = parser.parse_args()

    c = ProceduralSkillCrystallizer(min_support=2)
    trajectories = [
        [TrajectoryStep("fetch_data", True), TrajectoryStep("clean_json", True), TrajectoryStep("export_csv", True)],
        [TrajectoryStep("fetch_data", True), TrajectoryStep("clean_json", True), TrajectoryStep("export_csv", True)],
    ]
    skills = c.mine_trajectories(trajectories)
    print(f"Discovered {len(skills)} crystallized skills:")
    for s in skills:
        print(f"  {s.skill_name} -> {' -> '.join(s.tool_sequence)} (freq={s.frequency})")

if __name__ == "__main__":
    main()
