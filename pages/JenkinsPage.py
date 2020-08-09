'''
@author: wenyihuqingjiu
@project: Pytest_Auto_Test
@file: JenkinsPage
@time: 2020-08-09 20:22
@desc:
'''

from pages.BasePage import BasePage


class JenkinsPage(BasePage):
    input_username = 'id,j_username'
    input_password = 'name,j_password'
    submit = 'name,Submit'

    def username(self, username):
        self.send_key(self.input_username, username)

    def password(self, password):
        self.send_key(self.input_password, password)

    def enter(self):
        self.click(self.submit)

    def login_success(self, username, password):
        self.username(username)
        self.password(password)
        self.enter()