import time

from selenium.webdriver.common.by import By


class CricBuzz_page:
    matches_tab_id = (By.ID, "live-scores-link")
    live_score_text_xpath = (By.XPATH, "//*[@id='page-wrapper']/div[5]/div[1]/h1")
    recent_tab_id = (By.ID, "recent-tab")
    upcoming_tab_id = (By.ID, "upcoming-tab")
    match_tab_xpath = (By.XPATH, "//*[@id='page-wrapper']/div[4]/div[2]/div/nav")
    international_tab_id = (By.ID, "international-tab")
    league_tab_id = (By.ID, "league-tab")
    # scorecard_xpath = (By.XPATH, "//*[@id='page-wrapper']/div[4]/div[2]/div/div[7]/div[1]/nav/a[2]")
    match_xpath = (By.XPATH, "//a[@title='Chennai Super Kings vs Sunrisers Hyderabad']")
    squad_xpath = (By.XPATH, "//a[@title='Sunrisers Hyderabad vs Chennai Super Kings, 18th Match Squads']")

    # list_of_matches
    click_on_IPL_link_tab_xpath = (By.XPATH, "//*[@id='page-wrapper']/div[4]/div[2]/div/div[4]/h2/a")
    click_on_points_table_xpath = (By.XPATH, "//*[@id='page-wrapper']/div[3]/nav/a[5]")

    def __init__(self, driver):
        self.driver = driver

    def click_on_matches(self):
        self.driver.find_element(*CricBuzz_page.matches_tab_id).click()
        text = self.driver.find_element(*CricBuzz_page.live_score_text_xpath).text
        return text

    def live_tab(self):
        pass

    def recent_tab(self, tab):
        self.driver.find_element(*CricBuzz_page.recent_tab_id).click()
        match_return = self.driver.find_element(*CricBuzz_page.match_tab_xpath).text
        s = match_return.find('L')
        t = match_return.find(" ", s)
        if tab == match_return[s:t]:
            self.driver.find_element(*CricBuzz_page.league_tab_id).click()
            time.sleep(5)
            # element = self.driver.find_element(*CricBuzz_page.match_tab_xpath)
            # self.driver.execute_script("window.scrollBy(0,900)", '')
            # time.sleep(5)
            self.driver.find_element(*CricBuzz_page.match_xpath).click()
            time.sleep(3)
            self.driver.find_element(*CricBuzz_page.squad_xpath).click()
            time.sleep(5)
            ls = []
            for i in range(1, 12):
                s = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[3]/div[2]/div[3]/div["
                                                       "" + str(i) + "]/a/div[2]/div").text
                t = s.find("\n")
                ls.append(s[0:t])
                time.sleep(1)
            return ls
        else:
            return 'fail'

    def list_of_matches(self, team_name, match_no):
        self.driver.find_element(*CricBuzz_page.recent_tab_id).click()
        self.driver.find_element(*CricBuzz_page.league_tab_id).click()
        self.driver.find_element(*CricBuzz_page.click_on_IPL_link_tab_xpath).click()
        self.driver.find_element(*CricBuzz_page.click_on_points_table_xpath).click()
        for i in range(1, 20, 2):
            list_of_team = self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[4]/div[1]/table/tbody/tr["
                                                              "" + str(i) + "]/td[1]").text
            if team_name == list_of_team:
                self.driver.execute_script("arguments[0].scrollIntoView();",
                                           self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[4]/div["
                                                                              "1]/table/tbody/tr[" + str(i) + "]/td[1]"))
                time.sleep(3)
                self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div[4]/div[1]/table/tbody/tr["
                                                   "" + str(i) + "]/td[9]/a").click()
                time.sleep(3)
                for s in range(2, 14):
                    description = self.driver.find_element(By.XPATH, "//*[@id='team_62']/table/tbody/tr["
                                                                     "" + str(s) + "]/td[2]").text
                    print(description)
                    if match_no == "":
                        self.driver.find_element(By.XPATH, "//*[@id='team_62']/table/tbody/tr[2]/td[4]/a").click()
                        time.sleep(10)
                        return description

                    else:
                        pass
            else:
                continue

    # def league_tab(self):
    #     self.driver.find_element(*CricBuzz_page.league_tab_id).click()
    #     time.sleep(5)
