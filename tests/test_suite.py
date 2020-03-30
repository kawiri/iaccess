# test/test_suite.py

# noinspection PyUnresolvedReferences
import pytest
from sqlalchemy.testing.suite import *


class CTETest(CTETest):
    @pytest.mark.xfail(reason="ctes not allowed in insert statements on db2 for iseries")
    def test_insert_from_select_round_trip(self):
        super().test_insert_from_select_round_trip()


class ComponentReflectionTest(ComponentReflectionTest):
    @pytest.mark.xfail(reason="unique constraints with duplicate column sets unsupported on db2 for iseries")
    def test_get_unique_constraints(self):
        return super().test_get_unique_constraints()


class ExpandingBoundInTest(ExpandingBoundInTest):
    @pytest.mark.xfail(reason="search condition where null in set not unsupported on db2 for iseries")
    def test_null_in_empty_set_is_false(self):
        return super().test_null_in_empty_set_is_false()


class InsertBehaviorTest(InsertBehaviorTest):
    @pytest.mark.xfail(reason="iaccess odbc driver is not able to infer some data types")
    def test_insert_from_select_with_defaults(self):
        return super().test_insert_from_select_with_defaults()


class NumericTest(NumericTest):
    @pytest.mark.xfail(reason="iaccess odbc driver is not able to infer some data types")
    def test_float_coerce_round_trip(self):
        return super().test_float_coerce_round_trip()
