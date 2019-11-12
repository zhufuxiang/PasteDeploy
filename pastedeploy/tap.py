class Tap(object):
    def __init__(self, in_arg):
        print('init tap!!!!!!!!!')
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print 'Tap'
        start_response('200 ok', [('Content-Type', 'text/plain')])
        return ['%s, %s!\n' % (self.in_arg, 'Tap')]


def app_factory(global_config, in_arg):
    print 'tap factory'
    return Tap(in_arg)
