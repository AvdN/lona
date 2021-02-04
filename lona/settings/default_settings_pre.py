import os

DEBUG = False

MAX_WORKERS = 10

# routing
ROUTING_TABLE = 'lona.settings.default_routes.routes'

# templating
CORE_TEMPLATE_DIRS = [
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
]

TEMPLATE_DIRS = []

FRONTEND_TEMPLATE = 'lona/frontend.html'
ERROR_404_TEMPLATE = 'lona/404.html'
ERROR_500_TEMPLATE = 'lona/500.html'

TEMPLATE_EXTRA_CONTEXT = {}

# static files
CORE_STATIC_DIRS = [
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'),
]

STATIC_DIRS = []
STATIC_URL_PREFIX = '/static/'
STATIC_FILES_STYLE_TAGS_TEMPLATE = 'lona/style_tags.html'
STATIC_FILES_SCRIPT_TAGS_TEMPLATE = 'lona/script_tags.html'
STATIC_FILES_SYMBOLS_TEMPLATE = 'lona/lona-symbols.js'
STATIC_FILES_ENABLED = []
STATIC_FILES_DISABLED = []

# state
SERVER_STATE_ATOMIC = True

# views
FRONTEND_VIEW = 'lona.views.frontend'
VIEW_CACHING = True

# error handler
ERROR_404_HANDLER = 'lona.views.handle_404'
ERROR_500_HANDLER = 'lona.views.handle_500'
ERROR_404_FALLBACK_HANDLER = 'lona.views.handle_404'
ERROR_500_FALLBACK_HANDLER = 'lona.views.handle_500'

# middlewares
CORE_MIDDLEWARES = [
    'lona.middlewares.LonaMessageMiddleware',
]

MIDDLEWARES = []

# hooks
STARTUP_HOOKS = []
SHUTDOWN_HOOKS = []
