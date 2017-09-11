__version__ = '0.3.6'

from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_velruse')
log = __import__('logging').getLogger(__name__)


def kotti_configure(settings):
    settings['pyramid.includes'] += (
        ' velruse.app'
        ' pyramid_mako'
        ' kotti_velruse.views'
    )
