class Purifier(object):
    def __init__(self, app, in_arg):
        print 'init purifier filter'
        self.app = app
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print 'Purifier'
        return self.app(environ, start_response)


def filter_app_factory(app, global_config, in_arg):
    print 'Purifier filter factory'
    return Purifier(app, in_arg)
