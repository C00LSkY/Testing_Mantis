from model.projects import ProjectData




def test_del_project_some_id(app, id):
    app.project.open_manage_page()
    app.project.open_manage_project_page()
    old_project_list = app.project.get_project_list()
    app.project.del_project_by_id(ProjectData)
    new_project_list = app.project.get_project_list()
    assert len(new_project_list) == len(old_project_list) +1
