# THIS CODE IS PROPERTY OF Fortis Gimian
# http://stackoverflow.com/questions/14315466/separation-of-static-files-assets-with-django-compressor-usage-of-collectsta

from compressor.storage import CompressorFileStorage
from compressor.finders import CompressorFinder
from compressor.conf import settings


class CompressorFileAltStorage(CompressorFileStorage):
    """
    This alternative django-compressor storage class is utilised
    specifically for CompressorAltFinder which allows an independent
    find path.

    The default for ``location`` is ``COMPRESS_SOURCE_ROOT``.
    """
    def __init__(self, location=None, base_url=None, *args, **kwargs):
        if location is None:
            location = settings.COMPRESS_SOURCE_ROOT
        # The base_url is not used by the Finder class so it's irrelevant
        base_url = None
        super(CompressorFileAltStorage, self).__init__(location, base_url,
                                                       *args, **kwargs)

class CompressorAltFinder(CompressorFinder):
    """
    A staticfiles finder that looks in COMPRESS_SOURCE_ROOT
    for compressed files, to be used during development
    with staticfiles development file server or during
    deployment.
    """
    storage = CompressorFileAltStorage