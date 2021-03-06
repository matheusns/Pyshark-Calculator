// qprinterinfo.sip generated by MetaSIP
//
// This file is part of the QtGui Python extension module.
//
// Copyright (c) 2016 Riverbank Computing Limited <info@riverbankcomputing.com>
// 
// This file is part of PyQt4.
// 
// This file may be used under the terms of the GNU General Public License
// version 3.0 as published by the Free Software Foundation and appearing in
// the file LICENSE included in the packaging of this file.  Please review the
// following information to ensure the GNU General Public License version 3.0
// requirements will be met: http://www.gnu.org/copyleft/gpl.html.
// 
// If you do not wish to use this file under the terms of the GPL version 3.0
// then you may purchase a commercial license.  For more information contact
// info@riverbankcomputing.com.
// 
// This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
// WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


%If (Qt_4_4_0 -)
%If (PyQt_Printer)

class QPrinterInfo
{
%TypeHeaderCode
#include <qprinterinfo.h>
%End

public:
    QPrinterInfo();
    QPrinterInfo(const QPrinterInfo &src);
%If (Qt_5_0_0 -)
    explicit QPrinterInfo(const QPrinter &printer);
%End
%If (- Qt_5_0_0)
    QPrinterInfo(const QPrinter &printer);
%End
    ~QPrinterInfo();
    QString printerName() const;
    bool isNull() const;
    bool isDefault() const;
%If (Qt_5_0_0 -)
    QList<QPagedPaintDevice::PageSize> supportedPaperSizes() const;
%End
%If (- Qt_5_0_0)
    QList<QPrinter::PageSize> supportedPaperSizes() const;
%End
    static QList<QPrinterInfo> availablePrinters();
    static QPrinterInfo defaultPrinter();
%If (Qt_5_0_0 -)
    QString description() const;
%End
%If (Qt_5_0_0 -)
    QString location() const;
%End
%If (Qt_5_0_0 -)
    QString makeAndModel() const;
%End
%If (Qt_5_0_0 -)
    static QPrinterInfo printerInfo(const QString &printerName);
%End
};

%End
%End
%If (Qt_5_0_0 -)
// Mapped type for QList<QPagedPaintDevice::PageSize>.
%If (PyQt_Printer)

%MappedType QList<QPagedPaintDevice::PageSize> /TypeHintOut="List[QPagedPaintDevice.PageSize]", TypeHintValue="[]"/
{
%TypeHeaderCode
#include <qlist.h>
%End

%ConvertFromTypeCode
    // Create the list.
    PyObject *l = PyList_New(sipCpp->size());

    if (!l)
        return 0;

    // Set the list elements.
    for (int i = 0; i < sipCpp->size(); ++i)
    {
        PyObject *obj = sipConvertFromEnum(sipCpp->at(i), sipType_QPagedPaintDevice_PageSize);

        if (!obj)
        {
            Py_DECREF(l);
            return 0;
        }

        PyList_SET_ITEM(l, i, obj);
    }

    return l;
%End

%ConvertToTypeCode
    if (sipIsErr == NULL)
    {
        // We don't support passing the type as an argument as it isn't
        // currently needed.
        PyErr_SetString(PyExc_NotImplementedError, "converting to QList<QPagedPaintDevice::PageSize> is unsupported");

        return 0;
    }

    // Keep the compiler quiet.
    sipPy = NULL;
    return 0;
%End
};

%End
%End
%If (Qt_4_4_0 - Qt_5_0_0)
// Mapped type for QList<QPrinter::PageSize>.
%If (PyQt_Printer)

%MappedType QList<QPrinter::PageSize> /TypeHintOut="List[QPrinter.PageSize]", TypeHintValue="[]"/
{
%TypeHeaderCode
#include <qlist.h>
%End

%ConvertFromTypeCode
    // Create the list.
    PyObject *l = PyList_New(sipCpp->size());

    if (!l)
        return 0;

    // Set the list elements.
    for (int i = 0; i < sipCpp->size(); ++i)
    {
        PyObject *obj = sipConvertFromEnum(sipCpp->at(i), sipType_QPrinter_PageSize);

        if (!obj)
        {
            Py_DECREF(l);
            return 0;
        }

        PyList_SET_ITEM(l, i, obj);
    }

    return l;
%End

%ConvertToTypeCode
    if (sipIsErr == NULL)
    {
        // We don't support passing the type as an argument as it isn't
        // currently needed.
        PyErr_SetString(PyExc_NotImplementedError, "converting to QList<QPrinter::PageSize> is unsupported");

        return 0;
    }

    // Keep the compiler quiet.
    sipPy = NULL;
    return 0;
%End
};

%End
%End
