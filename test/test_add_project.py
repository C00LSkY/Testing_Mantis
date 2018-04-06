
from model.projects import ProjectData




def test_add_project(app):
    app.project.open_manage_page()
    app.project.open_manage_project_page()
    old_project_list = app.project.get_project_list()
    app.project.create_new_project(ProjectData)
    new_project_list = app.project.get_project_list()
    assert len(new_project_list) - 1 == len(old_project_list)

