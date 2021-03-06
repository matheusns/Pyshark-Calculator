// qprintdialog.sip generated by MetaSIP
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


%If (PyQt_PrintDialog)

class QPrintDialog : QAbstractPrintDialog
{
%TypeHeaderCode
#include <qprintdialog.h>
%End

public:
    QPrintDialog(QPrinter *printer, QWidget *parent /TransferThis/ = 0);
%If (Qt_4_5_0 -)
    explicit QPrintDialog(QWidget *parent /TransferThis/ = 0);
%End
    virtual ~QPrintDialog();
    virtual int exec() /PostHook=__pyQtPostEventLoopHook__,PreHook=__pyQtPreEventLoopHook__,PyName=exec_,ReleaseGIL/;
%MethodCode
        // Transfer ownership back to Python (a modal dialog will probably have the
        // main window as it's parent).  This means the Qt dialog will be deleted when
        // the Python wrapper is garbage collected.  Although this is a little
        // inconsistent, it saves having to code it explicitly to avoid the memory
        // leak.
        sipTransferBack(sipSelf);
        
        Py_BEGIN_ALLOW_THREADS
        sipRes = sipSelfWasArg ? sipCpp->QPrintDialog::exec()
                               : sipCpp->exec();
        Py_END_ALLOW_THREADS
%End

%If (Py_v3)
    virtual int exec() /PostHook=__pyQtPostEventLoopHook__,PreHook=__pyQtPreEventLoopHook__,ReleaseGIL/;
%MethodCode
        // Transfer ownership back to Python (a modal dialog will probably have the
        // main window as it's parent).  This means the Qt dialog will be deleted when
        // the Python wrapper is garbage collected.  Although this is a little
        // inconsistent, it saves having to code it explicitly to avoid the memory
        // leak.
        sipTransferBack(sipSelf);
        
        Py_BEGIN_ALLOW_THREADS
        sipRes = sipSelfWasArg ? sipCpp->QPrintDialog::exec()
                               : sipCpp->exec();
        Py_END_ALLOW_THREADS
%End

%End
%If (Qt_4_4_0 -)
%If (WS_X11)
    virtual void accept();
%End
%End
%If (Qt_4_5_0 -)
    virtual void done(int result);
%End
%If (Qt_4_5_0 -)
    void setOption(QAbstractPrintDialog::PrintDialogOption option, bool on = true);
%End
%If (Qt_4_5_0 -)
    bool testOption(QAbstractPrintDialog::PrintDialogOption option) const;
%End
%If (Qt_4_5_0 -)
    void setOptions(QFlags<QAbstractPrintDialog::PrintDialogOption> options);
%End
%If (Qt_4_5_0 -)
    QFlags<QAbstractPrintDialog::PrintDialogOption> options() const;
%End
%If (Qt_4_5_0 -)
    virtual void setVisible(bool visible);
%End
%If (Qt_5_0_0 -)
    virtual void open();
%End
%If (Qt_4_5_0 - Qt_5_0_0)
    void open();
%End
%If (Qt_4_5_0 -)
    void open(QObject *receiver, SIP_PYOBJECT member /TypeHint="QT_SLOT"/);
%MethodCode
        const char *slot = pyqt4_qtgui_get_slot(a1);
        
        if (slot)
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->open(a0, slot);
            Py_END_ALLOW_THREADS
        }
        else
        {
            sipError = sipBadCallableArg(1, a1);
        }
%End

%End
%If (Qt_4_5_0 -)
    void open(SIP_PYOBJECT slot /TypeHint="PYQT_SLOT"/);
%MethodCode
        QObject *receiver;
        QByteArray slot_signature;
        
        if ((sipError = pyqt4_qtgui_get_connection_parts(a0, 0, "()", false, &receiver, slot_signature)) == sipErrorNone)
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->open(receiver, slot_signature.constData());
            Py_END_ALLOW_THREADS
        }
        else if (sipError == sipErrorContinue)
        {
            sipError = sipBadCallableArg(0, a0);
        }
%End

%End
%If (Qt_4_5_0 -)
    void accepted();
%End

signals:
%If (Qt_4_5_0 -)
    void accepted(QPrinter *printer);
%End

private:
%If (- Qt_4_2_0)
    QPrintDialog(const QPrintDialog &);
%End
};

%End
