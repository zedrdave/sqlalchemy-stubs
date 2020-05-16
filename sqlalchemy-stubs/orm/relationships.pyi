from typing import Any, Optional, Generic, TypeVar, Union, overload, Type
from .interfaces import (
    MANYTOMANY as MANYTOMANY,
    MANYTOONE as MANYTOONE,
    ONETOMANY as ONETOMANY,
    StrategizedProperty as StrategizedProperty,
    PropComparator as PropComparator
)

def remote(expr): ...
def foreign(expr): ...


_T_co = TypeVar('_T_co', covariant=True)


# Note: typical use case is where argument is a string, so this will require
# a plugin to infer '_T_co', otherwise a user will need to write an explicit annotation.
# It is not clear whether RelationshipProperty is covariant at this stage since
# many types are still missing.
class RelationshipProperty(StrategizedProperty, Generic[_T_co]):
    strategy_wildcard_key: str = ...
    uselist: Any = ...
    argument: Any = ...
    secondary: Any = ...
    primaryjoin: Any = ...
    secondaryjoin: Any = ...
    post_update: bool = ...
    direction: Any = ...
    viewonly: bool = ...
    lazy: Any = ...
    single_parent: bool = ...
    collection_class: Any = ...
    passive_deletes: bool = ...
    cascade_backrefs: bool = ...
    passive_updates: bool = ...
    remote_side: Any = ...
    enable_typechecks: bool = ...
    query_class: Any = ...
    innerjoin: bool = ...
    distinct_target_key: Any = ...
    doc: Any = ...
    active_history: bool = ...
    join_depth: Any = ...
    local_remote_pairs: Any = ...
    extension: Any = ...
    bake_queries: bool = ...
    load_on_pending: bool = ...
    comparator_factory: Any = ...
    comparator: Any = ...
    info: Any = ...
    strategy_key: Any = ...
    cascade: Any = ...
    order_by: Any = ...
    back_populates: Any = ...
    backref: Any = ...
    def __init__(self, argument: Any, secondary: Optional[Any] = ...,
                 primaryjoin: Optional[Any] = ..., secondaryjoin: Optional[Any] = ...,
                 foreign_keys: Optional[Any] = ..., uselist: Optional[Any] = ...,
                 order_by: Any = ..., backref: Optional[Any] = ...,
                 back_populates: Optional[Any] = ..., post_update: bool = ..., cascade: Union[str, bool] = ...,
                 extension: Optional[Any] = ..., viewonly: bool = ...,
                 lazy: Optional[Union[str, bool]] = ..., collection_class: Optional[Any] = ...,
                 passive_deletes: bool = ..., passive_updates: bool = ...,
                 remote_side: Optional[Any] = ..., enable_typechecks: bool = ...,
                 join_depth: Optional[Any] = ..., comparator_factory: Optional[Any] = ...,
                 single_parent: bool = ..., innerjoin: bool = ..., distinct_target_key: Optional[Any] = ...,
                 doc: Optional[Any] = ..., active_history: bool = ..., cascade_backrefs: bool = ...,
                 load_on_pending: bool = ..., bake_queries: bool = ...,
                 _local_remote_pairs: Optional[Any] = ..., query_class: Optional[Any] = ...,
                 info: Optional[Any] = ..., sync_backref: bool = ...) -> None: ...
    def instrument_class(self, mapper): ...
    class Comparator(PropComparator):
        prop: Any = ...
        def __init__(self, prop, parentmapper, adapt_to_entity: Optional[Any] = ...,
                     of_type: Optional[Any] = ...) -> None: ...
        def adapt_to_entity(self, adapt_to_entity): ...
        def mapper(self): ...
        def __clause_element__(self): ...
        def of_type(self, cls): ...
        def in_(self, other): ...
        __hash__: Any = ...
        def __eq__(self, other): ...
        def any(self, criterion: Optional[Any] = ..., **kwargs): ...
        def has(self, criterion: Optional[Any] = ..., **kwargs): ...
        def contains(self, other, **kwargs): ...
        def __ne__(self, other): ...
        @property
        def property(self): ...
    # This doesn't exist at runtime, and Comparator is used instead, but it is hard to explain to mypy.
    def __eq__(self, other: Any) -> Any: ...
    def merge(self, session, source_state, source_dict, dest_state, dest_dict,
              load, _recursive, _resolve_conflict_map): ...
    def cascade_iterator(self, *args, **kwargs): ...
    @property
    def mapper(self): ...
    def table(self): ...
    def do_init(self): ...
    # This doesn't exist at runtime, but is present here for better typing.
    @overload
    def __get__(self, instance: None, owner: Any) -> RelationshipProperty[_T_co]: ...
    @overload
    def __get__(self, instance: object, owner: Any) -> _T_co: ...

class JoinCondition(object):
    parent_selectable: Any = ...
    parent_local_selectable: Any = ...
    child_selectable: Any = ...
    child_local_selectable: Any = ...
    parent_equivalents: Any = ...
    child_equivalents: Any = ...
    primaryjoin: Any = ...
    secondaryjoin: Any = ...
    secondary: Any = ...
    consider_as_foreign_keys: Any = ...
    prop: Any = ...
    self_referential: Any = ...
    support_sync: Any = ...
    can_be_synced_fn: Any = ...
    def __init__(self, parent_selectable, child_selectable, parent_local_selectable,
                 child_local_selectable, primaryjoin: Optional[Any] = ...,
                 secondary: Optional[Any] = ..., secondaryjoin: Optional[Any] = ...,
                 parent_equivalents: Optional[Any] = ..., child_equivalents: Optional[Any] = ...,
                 consider_as_foreign_keys: Optional[Any] = ..., local_remote_pairs: Optional[Any] = ...,
                 remote_side: Optional[Any] = ..., self_referential: bool = ..., prop: Optional[Any] = ...,
                 support_sync: bool = ..., can_be_synced_fn: Any = ...) -> None: ...
    @property
    def primaryjoin_minus_local(self): ...
    @property
    def secondaryjoin_minus_local(self): ...
    @property
    def primaryjoin_reverse_remote(self): ...
    @property
    def remote_columns(self): ...
    @property
    def local_columns(self): ...
    @property
    def foreign_key_columns(self): ...
    def deannotated_primaryjoin(self): ...
    def deannotated_secondaryjoin(self): ...
    def join_targets(self, source_selectable, dest_selectable, aliased, single_crit: Optional[Any] = ...): ...
    def create_lazy_clause(self, reverse_direction: bool = ...): ...
