"""Tests for Skill Crystallizer."""
import unittest
from agent_procedural_skill_crystallizer.core import ProceduralSkillCrystallizer, TrajectoryStep

class TestProceduralSkillCrystallizer(unittest.TestCase):
    def test_skill_mining(self):
        c = ProceduralSkillCrystallizer(min_support=2)
        t = [TrajectoryStep("a", True), TrajectoryStep("b", True)]
        skills = c.mine_trajectories([t, t])
        self.assertTrue(any(s.tool_sequence == ["a", "b"] for s in skills))
