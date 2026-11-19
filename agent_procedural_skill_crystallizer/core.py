"""Core Procedural Skill Crystallizer."""
from typing import List, Dict, Tuple, Optional
from collections import Counter

class TrajectoryStep:
    def __init__(self, tool_name: str, success: bool):
        self.tool_name = tool_name
        self.success = success

class CrystallizedSkill:
    def __init__(self, skill_name: str, tool_sequence: List[str], frequency: int):
        self.skill_name = skill_name
        self.tool_sequence = tool_sequence
        self.frequency = frequency

class ProceduralSkillCrystallizer:
    def __init__(self, min_support: int = 2):
        self.min_support = min_support
        self.crystallized_skills: Dict[str, CrystallizedSkill] = {}

    def mine_trajectories(self, trajectories: List[List[TrajectoryStep]]) -> List[CrystallizedSkill]:
        # Extract successful 2-step and 3-step tool sequences
        seq_counts = Counter()
        for traj in trajectories:
            successful_tools = [s.tool_name for s in traj if s.success]
            for n in (2, 3):
                for i in range(len(successful_tools) - n + 1):
                    sub = tuple(successful_tools[i:i + n])
                    seq_counts[sub] += 1

        discovered = []
        for seq, count in seq_counts.items():
            if count >= self.min_support:
                name = "macro_" + "_".join(seq)
                skill = CrystallizedSkill(name, list(seq), count)
                self.crystallized_skills[name] = skill
                discovered.append(skill)
        return discovered
