from selenium.webdriver.common.by import By

from StudyNotes.TestDevelopHomework.PhaseFourHomework.po.base_page import BasePage


class ContactPage(BasePage):

    # 企业微信通讯录地址链接
    _contactPage = "https://work.weixin.qq.com/wework_admin/frame#contacts"
    _base_url = _contactPage

    _contact_addmember = (By.CLASS_NAME, "member_colRight_cnt_operation")

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        from StudyNotes.TestDevelopHomework.PhaseFourHomework.po.add_member_page import AddMemberPage

        #点击添加成员按钮跳转至添加成员页面
        self.find(self._contact_addmember)

        return AddMemberPage(self.driver)

    def get_member_list(self):
        """
        获取成员列表
        :return:
        """

        get_member_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # get_member_list = self.contactsPage.get_members_list()
        print(get_member_list)
        member_name = [i.text for i in get_member_list]
        print(member_name)
        return member_name