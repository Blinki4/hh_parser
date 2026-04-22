import pytest

from parsers.jobs_parser import SkillsSorter

class TestSkillSorter:
    @pytest.fixture
    def skill_sorter(self):
        return SkillsSorter()


    def test_sort_skills(self, skill_sorter):
        unsorted_skills = [
            'python',
            'java',
            'c++',
            'python',
            'python',
            'c++'
        ]

        result = skill_sorter._sort_skills(unsorted_skills)
        assert result == [
            ('python', 3),
            ('c++', 2),
            ('java', 1)
        ]