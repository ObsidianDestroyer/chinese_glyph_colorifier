import pytest

from glypher.structures.radicals import Human, Heart, Sun, Fire


class TestGlyphRadicals(object):

    @pytest.mark.only
    def test_radical_human(self):
        testing_glyphs = ['亼', '众', '任']
        human_radical = Human()

        for glyph in testing_glyphs:
            assert human_radical.radical == '人'
            assert human_radical.alt_radical == '亻'
            assert human_radical.inspect_radical(glyph)

    @pytest.mark.skip
    def test_radical_heart(self):
        testing_glyphs = ['必', '忆', '忉', '志', '忆']
        heart_radical = Heart()

        for glyph in testing_glyphs:
            assert heart_radical.radical == '忄'
            assert heart_radical.alt_radical == '心'
            assert heart_radical.inspect_radical(glyph)

    def test_radical_sun(self):
        testing_glyphs = list('旦旧旨早旪旰旱旴时旺明昤暎')
        sun_radical = Sun()

        for glyph in testing_glyphs:
            assert sun_radical.radical == '日'
            assert sun_radical.inspect_radical(glyph)

    def test_radical_fire(self):
        testing_glyphs = list('灭灮灺灼災灾灿灴灶灵烈烋烝')
        fire_radical = Fire()

        for glyph in testing_glyphs:
            assert fire_radical.radical == '火'
            assert fire_radical.alt_radical == '灬'
            assert fire_radical.inspect_radical(glyph)
