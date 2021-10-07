import pytest

from StudyNotes.TestDevelopHomework.PhaseFourHomework.po.main_page import MainPage


class TestAddMember:

    def setup(self):
        self.main_page = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name",["123"])
    def test_add_member(self,name):
        #1.跳转到add member 页面
        #2.跳转成员操作，点击保存跳转到通讯录页面
        #3.在通讯录页面获取成员信息，作为断言
        assert "name" in self.main_page.goto_add_member().add_member(name).get_member_list()