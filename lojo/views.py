from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'lojo'}


@view_config(route_name='about', renderer='templates/mytemplate.pt')
def my_view2(request):
    return {'project': 'lojo'}