#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


# This is only needed for Python v2 but is harmless for Python v3.
import sip
sip.setapi('QVariant', 2)

from PyQt4 import QtCore, QtGui


class RegExpDialog(QtGui.QDialog):
    MaxCaptures = 6

    def __init__(self, parent=None):
        super(RegExpDialog, self).__init__(parent)

        self.patternComboBox = QtGui.QComboBox()
        self.patternComboBox.setEditable(True)
        self.patternComboBox.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)

        patternLabel = QtGui.QLabel("&Pattern:")
        patternLabel.setBuddy(self.patternComboBox)

        self.escapedPatternLineEdit = QtGui.QLineEdit()
        self.escapedPatternLineEdit.setReadOnly(True)
        palette = self.escapedPatternLineEdit.palette()
        palette.setBrush(QtGui.QPalette.Base,
                palette.brush(QtGui.QPalette.Disabled, QtGui.QPalette.Base))
        self.escapedPatternLineEdit.setPalette(palette)

        escapedPatternLabel = QtGui.QLabel("&Escaped Pattern:")
        escapedPatternLabel.setBuddy(self.escapedPatternLineEdit)

        self.syntaxComboBox = QtGui.QComboBox()
        self.syntaxComboBox.addItem("Regular expression v1",
                QtCore.QRegExp.RegExp)
        self.syntaxComboBox.addItem("Regular expression v2",
                QtCore.QRegExp.RegExp2)
        self.syntaxComboBox.addItem("Wildcard", QtCore.QRegExp.Wildcard)
        self.syntaxComboBox.addItem("Fixed string",
                QtCore.QRegExp.FixedString)

        syntaxLabel = QtGui.QLabel("&Pattern Syntax:")
        syntaxLabel.setBuddy(self.syntaxComboBox)

        self.textComboBox = QtGui.QComboBox()
        self.textComboBox.setEditable(True)
        self.textComboBox.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)

        textLabel = QtGui.QLabel("&Text:")
        textLabel.setBuddy(self.textComboBox)

        self.caseSensitiveCheckBox = QtGui.QCheckBox("Case &Sensitive")
        self.caseSensitiveCheckBox.setChecked(True)
        self.minimalCheckBox = QtGui.QCheckBox("&Minimal")

        indexLabel = QtGui.QLabel("Index of Match:")
        self.indexEdit = QtGui.QLineEdit()
        self.indexEdit.setReadOnly(True)

        matchedLengthLabel = QtGui.QLabel("Matched Length:")
        self.matchedLengthEdit = QtGui.QLineEdit()
        self.matchedLengthEdit.setReadOnly(True)

        self.captureLabels = []
        self.captureEdits = []
        for i in range(self.MaxCaptures):
            self.captureLabels.append(QtGui.QLabel("Capture %d:" % i))
            self.captureEdits.append(QtGui.QLineEdit())
            self.captureEdits[i].setReadOnly(True)
        self.captureLabels[0].setText("Match:")

        checkBoxLayout = QtGui.QHBoxLayout()
        checkBoxLayout.addWidget(self.caseSensitiveCheckBox)
        checkBoxLayout.addWidget(self.minimalCheckBox)
        checkBoxLayout.addStretch(1)

        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(patternLabel, 0, 0)
        mainLayout.addWidget(self.patternComboBox, 0, 1)
        mainLayout.addWidget(escapedPatternLabel, 1, 0)
        mainLayout.addWidget(self.escapedPatternLineEdit, 1, 1)
        mainLayout.addWidget(syntaxLabel, 2, 0)
        mainLayout.addWidget(self.syntaxComboBox, 2, 1)
        mainLayout.addLayout(checkBoxLayout, 3, 0, 1, 2)
        mainLayout.addWidget(textLabel, 4, 0)
        mainLayout.addWidget(self.textComboBox, 4, 1)
        mainLayout.addWidget(indexLabel, 5, 0)
        mainLayout.addWidget(self.indexEdit, 5, 1)
        mainLayout.addWidget(matchedLengthLabel, 6, 0)
        mainLayout.addWidget(self.matchedLengthEdit, 6, 1)

        for i in range(self.MaxCaptures):
            mainLayout.addWidget(self.captureLabels[i], 7 + i, 0)
            mainLayout.addWidget(self.captureEdits[i], 7 + i, 1)
        self.setLayout(mainLayout)

        self.patternComboBox.editTextChanged.connect(self.refresh)
        self.textComboBox.editTextChanged.connect(self.refresh)
        self.caseSensitiveCheckBox.toggled.connect(self.refresh)
        self.minimalCheckBox.toggled.connect(self.refresh)
        self.syntaxComboBox.currentIndexChanged.connect(self.refresh)

        self.patternComboBox.addItem("[A-Za-z_]+([A-Za-z_0-9]*)")
        self.textComboBox.addItem("(10 + delta4)* 32")

        self.setWindowTitle("RegExp")
        self.setFixedHeight(self.sizeHint().height())
        self.refresh()

    def refresh(self):
        self.setUpdatesEnabled(False)

        pattern = self.patternComboBox.currentText()
        text = self.textComboBox.currentText()

        escaped = str(pattern)
        escaped.replace('\\', '\\\\')
        escaped.replace('"', '\\"')
        self.escapedPatternLineEdit.setText('"' + escaped + '"')

        rx = QtCore.QRegExp(pattern)
        cs = QtCore.Qt.CaseInsensitive
        if self.caseSensitiveCheckBox.isChecked():
            cs = QtCore.Qt.CaseSensitive
        rx.setCaseSensitivity(cs)
        rx.setMinimal(self.minimalCheckBox.isChecked())
        syntax = self.syntaxComboBox.itemData(self.syntaxComboBox.currentIndex())
        rx.setPatternSyntax(syntax)

        palette = self.patternComboBox.palette()
        if rx.isValid():
            palette.setColor(QtGui.QPalette.Text,
                    self.textComboBox.palette().color(QtGui.QPalette.Text))
        else:
            palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
        self.patternComboBox.setPalette(palette)

        self.indexEdit.setText(str(rx.indexIn(text)))
        self.matchedLengthEdit.setText(str(rx.matchedLength()))

        for i in range(self.MaxCaptures):
            self.captureLabels[i].setEnabled(i <= rx.numCaptures())
            self.captureEdits[i].setEnabled(i <= rx.numCaptures())
            self.captureEdits[i].setText(rx.cap(i))

        self.setUpdatesEnabled(True)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = RegExpDialog()
    sys.exit(dialog.exec_())
