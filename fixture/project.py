
from model.project import ProjectData


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_overview_page.php") and
                len(wd.find_elements_by_link_text("Manage Projects")) > 0):
            wd.find_element_by_link_text("Manage").click()

    def open_manage_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and
                len(wd.find_elements_by_xpath("//input[@value='Create New Project']")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create_new_project(self, project):
        wd = self.app.wd
        self.open_manage_page()
        self.open_manage_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        if not wd.find_element_by_xpath("//table[@class='width75']/tbody/tr[3]/td[2]/select//option[3]").is_selected():
            wd.find_element_by_xpath("//table[@class='width75']/tbody/tr[3]/td[2]/select//option[3]").click()
        if wd.find_element_by_name("inherit_global").is_selected():
            wd.find_element_by_name("inherit_global").click()
        if not wd.find_element_by_name("inherit_global").is_selected():
            wd.find_element_by_name("inherit_global").click()
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_css_selector("input.button").click()
        self.open_manage_project_page()

    project_cashe = None

    def get_project_list(self):
        if self.project_cashe is None:
            wd = self.app.wd
            self.open_manage_project_page()
            self.project_cashe = []
            for element in wd.find_elements_by_xpath("//tr[td/a[contains(@href, 'manage_proj_edit_page.php?project_id=')]]"):
                cell = element.find_elements_by_tag_name("td")
                link_id = cell[0].element.find_element_by_tag_name("a").get_attribute("href")
                id = link_id[36:]
                print(id)
                name = cell[0].text
                status = cell[1].text
                if cell[2].text == "X":
                    ennabled = "yes"
                else:
                    ennabled = "no"
                view_status = cell[3].text
                description = cell[4].text
                self.project_cashe.append(ProjectData(id=id, name=name, status=status, enabled=ennabled,
                                                      view_status=view_status, description=description))
        return list(self.project_cashe)

    def open_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s' )]" % id).click()

    def count_project(self):
        wd = self.app.wd
        self.open_manage_project_page()
        count = len(wd.find_elements_by_xpath("//tr[td/a[contains(@href, 'manage_proj_edit_page.php?project_id=')]]"))
        return count

