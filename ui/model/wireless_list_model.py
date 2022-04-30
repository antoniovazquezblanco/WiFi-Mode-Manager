#!/usr/bin/env python

'''
Model for representing a wireless list in views.
'''

from PySide2.QtCore import QAbstractItemModel, QModelIndex, Qt


class WirelessListModel(QAbstractItemModel):
    def __init__(self, parent=None, *args):
        '''
        Initialize our abstract item model by calling the super class
        initializer and with an empty list of elements.
        '''
        super().__init__(parent, *args)
        self.items = []

    def index(self, row, column, parent=QModelIndex()):
        '''
        This function should return a list of valid indices for every model
        item. Given that our model represents a simple list, if there is a
        valid parent for this row and column return an empty QModelList,
        otherwise, return an index representing the row and column of the item.
        '''
        if not self.hasIndex(row, column, parent) or parent.isValid():
            return QModelIndex()
        return self.createIndex(row, column)

    def parent(self, index):
        '''
        Returns a pointer to the parent item corresponding to the index
        provided. Given that we only show a flat list, we always return an
        empty QModelIndex that represents the root node.
        '''
        return QModelIndex()

    def rowCount(self, parent=QModelIndex()):
        '''
        This function returns the number of rows of the parent item. Given
        that we implement a flat list model, if our parent is valid we always
        return 0 columns because we do not have any child. If the parent is
        the root element, we always return the number of elements of our list.
        '''
        if parent.isValid():
            return 0
        return len(self.items)

    def columnCount(self, parent=QModelIndex()):
        '''
        This function returns the number of columns, we always return 3
        columns for every parent.
        '''
        return 3

    def headerData(self, section, orientation, role):
        '''
        Return header data.
        '''
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return ['Device', 'Chipset', 'Mode'][section]
        return None

    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            item = self.items[index.row()]
            column = ['dev', 'chipset', 'mode'][index.column()]
            return item[column]

    def addItems(self, items):
        self.beginResetModel()
        self.items = items
        self.endResetModel()
