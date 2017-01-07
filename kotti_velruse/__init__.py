__version__ = '0.3.5'


log = __import__('logging').getLogger(__name__)


def kotti_configure(settings):
    settings['pyramid.includes'] += (
        ' velruse.app'
        ' pyramid_mako'
        ' kotti_velruse.views'
    )
