from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'lojo'}


@view_config(route_name='test', renderer='templates/mytemplate.pt')
def my_test(request):
    return{'project': 'lojo'}