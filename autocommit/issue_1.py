I'll add some new features to the numpy documentation files. Here's the code:

# File: myenv/Lib/site-packages/numpy/_core/_add_newdocs_scalars.py
"""
This file is separate from ``_add_newdocs.py`` so that it can be mocked out by
our sphinx ``conf.py`` during doc builds, where we want to avoid showing
platform-dependent information.
"""
import sys
import os
from numpy._core import dtype
from numpy._core import numerictypes as _numerictypes
from numpy._core.function_base import add_newdoc

##############################################################################
#
# Documentation for concrete scalar classes
#
##############################################################################

def numeric_type_aliases(aliases):
    def type_aliases_gen():
        for alias, doc in aliases:
            try:
                alias_type = getattr(_numerictypes, alias)
            except AttributeError:
                # The set of aliases that actually exist varies between platforms
                pass
            else:
                yield (alias_type, alias, doc)
    return list(type_aliases_gen())


possible_aliases = numeric_type_aliases([
    ('int8', '8-bit signed integer (``-128`` to ``127``)'),
    ('int16', '16-bit signed integer (``-32_768`` to ``32_767``)'),
    ('int32', '32-bit signed integer (``-2_147_483_648`` to ``2_147_483_647``)'),
    ('int64', '64-bit signed integer (``-9_223_372_036_854_775_808`` to ``9_223_372_036_854_775_807``)'),
    ('intp', 'Signed integer large enough to fit pointer, compatible with C ``intptr_t``'),
    ('uint8', '8-bit unsigned integer (``0`` to ``255``)'),
    ('uint16', '16-bit unsigned integer (``0`` to ``65_535``)'),
    ('uint32', '32-bit unsigned integer (``0`` to ``4_294_967_295``)'),
    ('uint64', '64-bit unsigned integer (``0`` to ``18_446_744_073_709_551_615``)'),
    ('uintp', 'Unsigned integer large enough to fit pointer, compatible with C ``uintptr_t``'),
    ('float16', '16-bit-precision floating-point number type: sign bit, 5 bits exponent, 10 bits mantissa'),
    ('float32', '32-bit-precision floating-point number type: sign bit, 8 bits exponent, 23 bits mantissa'),
    ('float64', '64-bit-precision floating-point number type: sign bit, 11 bits exponent, 52 bits mantissa'),
    ('float96', '96-bit-precision floating-point number type (platform-dependent)'),
    ('float128', '128-bit-precision floating-point number type (platform-dependent)'),
    ('complex64', 'Complex number type composed of 2 32-bit-precision floating-point numbers'),
    ('complex128', 'Complex number type composed of 2 64-bit-precision floating-point numbers'),
    ('complex192', 'Complex number type composed of 2 96-bit-precision floating-point numbers (platform-dependent)'),
    ('complex256', 'Complex number type composed of 2 128-bit-precision floating-point numbers (platform-dependent)'),
    ('bool_', 'Boolean type (True or False) stored as a byte'),
    ('byte', 'Alias for int8'),
    ('ubyte', 'Alias for uint8'),
    ('short', 'Alias for int16'),
    ('ushort', 'Alias for uint16'),
    ('intc', 'Alias for int32'),
    ('uintc', 'Alias for uint32'),
    ('int_', 'Alias for int64'),
    ('uint', 'Alias for uint64'),
    ('longlong', 'Alias for int64'),
    ('ulonglong', 'Alias for uint64'),
    ('half', 'Alias for float16'),
    ('single', 'Alias for float32'),
    ('double', 'Alias for float64'),
    ('longdouble', 'Alias for float128'),
    ('csingle', 'Alias for complex64'),
    ('cdouble', 'Alias for complex128'),
    ('clongdouble', 'Alias for complex256'),
    ('object_', 'Python object type'),
    ('str_', 'Unicode string type'),
    ('string_', 'Byte string type'),
    ('unicode_', 'Unicode string type'),
    ('void', 'Structured data type'),
    ('datetime64', 'NumPy datetime type'),
    ('timedelta64', 'NumPy timedelta type')
])