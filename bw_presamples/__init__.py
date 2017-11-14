__all__ = [
    'create_presamples_package',
    'FORMATTERS',
    'IrregularPresamplesArray',
    'MatrixPresamples',
	'Campaign'
]


__version__ = (0, 0, 'dev')

from .array import IrregularPresamplesArray
from .packaging import create_presamples_package, FORMATTERS
from .matrix_presamples import MatrixPresamples
from .campaigns import Campaign
