import pytest

from pageObject.cricbuss_object import CricBuzz_page
from Utilities import XLUties


class Test_Cric_buzz_matches:
    file = "D:\\Python\\CricBuzz\\testdata\\cricket_data.xlsx"
    team_name = XLUties.ReadData(file, 'Sheet1', 2, 2)
    team_no = XLUties.ReadData(file, 'Sheet1', 1, 5)

    @pytest.mark.skip
    def test_cric_001(self, setup):
        self.driver = setup
        self.cr = CricBuzz_page(self.driver)
        text = self.cr.click_on_matches()
        assert text == "Live Cricket Score"

    # @pytest.mark.skip
    def test_recent_tab_002(self, setup):
        self.driver = self.test_cric_001(setup)
        s = self.cr.recent_tab('League')
        t = 3
        for i in s:
            XLUties.WriteData(self.file, "Sheet1", t, 2, i)
            t += 1

    @pytest.mark.skip
    def test_list_of_league_003(self, setup):
        self.driver = self.test_cric_001(setup)
        match_no = self.cr.list_of_matches(self.team_name, self.team_no)
        XLUties.WriteData(self.file, "Sheet1", 1, 5, match_no)
