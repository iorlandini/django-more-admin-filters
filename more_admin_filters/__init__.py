VERSION = (1, 4)
__version__ = ".".join(map(str, VERSION))


from .filters import (
    MultiSelectFilter, MultiSelectRelatedFilter, MultiSelectDropdownFilter,
    MultiSelectRelatedDropdownFilter, DropdownFilter, ChoicesDropdownFilter,
    RelatedDropdownFilter, BooleanAnnotationFilter
)
