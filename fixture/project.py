
from model.project import ProjectData


class ProjectHelper:


    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_overview_page.php") and
                len(wd.find_elements_by_link_text("Manage Projects")) > 0):
            wd.find_elements_by_link_text("Manage").click()

    def open_manage_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and
                len(wd.find_element_by_xpath("//input[@value='Create New Project']")) > 0):
            wd.find_elements_by_link_text("Manage").click()
            wd.find_elements_by_link_text("Manage Project").click()

    def create_new_project(self, project):
        wd = self.app.wd
        self.open_manage_page()
        self.open_manage_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("status").click()
        wd.find_element_by_name("status").clear()
        wd.find_element_by_name("status").send_keys(project.status)
        wd.find_element_by_name("inherit_global").click()
        wd.find_element_by_name("view_state").click()
        wd.find_element_by_name("view_state").clear()
        wd.find_element_by_name("view_state").send_keys(project.view_state)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)


