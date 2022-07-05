from garpixcms.settings import *  # noqa

INSTALLED_APPS += [ # noqa
    'home',
    'cases',
    'blocks',
]

MENU_TYPE_HEADER_MENU = 'header_menu'
MENU_TYPE_EXTENDED_MENU = 'extended_menu'
MENU_TYPE_EXTENDED_SUBMENU = 'extended_submenu'

MENU_TYPES = {
    MENU_TYPE_HEADER_MENU: {
        'title': 'Верхнее меню',
    },
    MENU_TYPE_EXTENDED_MENU: {
        'title': 'Развёрнутое меню',
    },
    MENU_TYPE_EXTENDED_SUBMENU: {
        'title': 'Развёрнутое подменю',
    },
}

CHOICE_MENU_TYPES = [(k, v['title']) for k, v in MENU_TYPES.items()]
