


from model.project import ProjectData




def test_add_project(app):
    app.project.open_manage_page()
    app.project.open_manage_project_page()
    app.project.create_new_project(ProjectData)
