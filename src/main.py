import os
 

def main():
    import django.core.handlers.wsgi

    # Google App Engine imports.
    from google.appengine.ext.webapp import util

    app = django.core.handlers.wsgi.WSGIHandler()

    util.run_wsgi_app(app)

#if __name__ == '__main__':
#    main()



