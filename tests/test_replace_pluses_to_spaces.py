from helpers.format_string import replace_spaces_to_pluses

class TestReplaceSpacesToPluses:

    def test_replace_space_from_string(self):
        query = 'python developer'
        result = replace_spaces_to_pluses(query)
        assert result == 'python+developer'

    def test_replace_spaces_from_string(self):
        query = 'python senior developer'
        result = replace_spaces_to_pluses(query)
        assert result == 'python+senior+developer'

    def test_replace_spaces_in_a_row(self):
        query = 'py  thon'
        result = replace_spaces_to_pluses(query)
        assert result == 'py++thon'