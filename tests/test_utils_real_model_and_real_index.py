"""
Test helper functions about Qt MVC: real_model, real_index
"""

# Import third-party modules
from qtpy import QtCore
from qtpy import QtGui

# Import local modules
from dayu_widgets3 import utils


def test_with_string_list_model():
    """Test when source model is QStringListModel"""
    source_model = QtCore.QStringListModel(["apple", "pear", "orange"])
    sort_filter_model_1 = QtCore.QSortFilterProxyModel()
    sort_filter_model_1.setSourceModel(source_model)
    sort_filter_model_2 = QtCore.QSortFilterProxyModel()
    sort_filter_model_2.setSourceModel(source_model)
    index_1 = source_model.index(0, 0)
    index_2 = source_model.index(1, 0)
    index_3 = sort_filter_model_1.index(0, 0)
    index_4 = sort_filter_model_1.index(1, 0)
    index_5 = sort_filter_model_2.index(1, 0)
    index_6 = sort_filter_model_2.index(1, 0)
    assert utils.real_model(source_model) is source_model
    assert utils.real_model(sort_filter_model_1) is source_model
    assert utils.real_model(sort_filter_model_2) is source_model
    assert utils.real_model(index_1) is source_model
    assert utils.real_model(index_2) is source_model
    assert utils.real_model(index_3) is source_model
    assert utils.real_model(index_4) is source_model
    assert utils.real_model(index_5) is source_model
    assert utils.real_model(index_6) is source_model


def test_with_standard_item_model():
    """Test when source model is QStandardItemModel"""
    source_model = QtGui.QStandardItemModel(2, 2)
    sort_filter_model_1 = QtCore.QSortFilterProxyModel()
    sort_filter_model_1.setSourceModel(source_model)
    sort_filter_model_2 = QtCore.QSortFilterProxyModel()
    sort_filter_model_2.setSourceModel(source_model)
    index_1 = source_model.index(0, 0)
    index_2 = source_model.index(1, 1)
    index_3 = sort_filter_model_1.index(0, 1)
    index_4 = sort_filter_model_1.index(1, 1)
    index_5 = sort_filter_model_2.index(1, 0)
    index_6 = sort_filter_model_2.index(1, 1)
    assert utils.real_model(source_model) is source_model
    assert utils.real_model(sort_filter_model_1) is source_model
    assert utils.real_model(sort_filter_model_2) is source_model
    assert utils.real_model(index_1) is source_model
    assert utils.real_model(index_2) is source_model
    assert utils.real_model(index_3) is source_model
    assert utils.real_model(index_4) is source_model
    assert utils.real_model(index_5) is source_model
    assert utils.real_model(index_6) is source_model


def test_real_index():
    """Test real_index function."""
    source_model = QtGui.QStandardItemModel(2, 2)
    sort_filter_model_1 = QtCore.QSortFilterProxyModel()
    sort_filter_model_1.setSourceModel(source_model)
    sort_filter_model_2 = QtCore.QSortFilterProxyModel()
    sort_filter_model_2.setSourceModel(source_model)

    index_1_source = source_model.index(0, 0)
    index_2_source = source_model.index(1, 1)
    index_3 = sort_filter_model_1.index(0, 0)
    index_4 = sort_filter_model_1.index(1, 1)
    index_5 = sort_filter_model_2.index(0, 0)
    index_6 = sort_filter_model_2.index(1, 1)
    assert utils.real_index(index_1_source) is index_1_source
    assert utils.real_index(index_2_source) is index_2_source

    assert compare_two_model_index(utils.real_index(index_3), index_1_source)
    assert compare_two_model_index(utils.real_index(index_4), index_2_source)
    assert compare_two_model_index(utils.real_index(index_5), index_1_source)
    assert compare_two_model_index(utils.real_index(index_6), index_2_source)


def compare_two_model_index(index_1, index_2):
    """
    If the two input index's row and column and their parent is equal, then they are equal for test.
    """
    return (
        (index_1.row() == index_2.row())
        and (index_1.column() == index_2.column())
        and (index_1.parent() == index_2.parent())
    )
