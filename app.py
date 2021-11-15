from selenium import webdriver
from secrets import pw
from time import sleep

print('start')
print('start')

print('start')


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        print('Accessing URL')
        self.driver.get("https://instagram.com/")
        sleep(2)
        print('Success')
        print()

        print('Attempting login')
        self.driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath(
            '//button[@type="submit"]').click()
        sleep(5)
        print('Success')
        print()

        print('Ignoring notification')
        sleep(5)
        self.driver.find_element_by_class_name('HoLwm').click()
        sleep(1)
        print('Success')
        print()

    def get_unfollowers(self):
        print('Opening Account')
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a').click()
        sleep(5)
        print('Success')
        print()

        print('Accessing following')
        sFollowing = self.driver.find_element_by_partial_link_text('following')
        sFollowing.click()
        following = self._get_names()
        print('Success')
        print()

        print('Accessing followers')
        sFollowers = self.driver.find_element_by_partial_link_text('followers')
        sFollowers.click()
        followers = self._get_names()
        print('Success')
        print()

        print('Fetching non followers')
        not_following_back = [
            user for user in following if user not in followers]
        print('Success')
        print()
        print(not_following_back)

    def _get_names(self):
        sleep(1)
        scroll_box = self.driver.find_element_by_class_name('isgrP')
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script(""" arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/button').click()
        return names


#/html/body/div[6]/div/div/div[1]/div/div[2]/button/div/svg/path

my_bot = InstaBot('', pw)
my_bot.get_unfollowers()
# my_bot.get_unfollowers.unfollow()
