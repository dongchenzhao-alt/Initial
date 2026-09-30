# -*- coding: utf-8 -*-
"""Persistent LibreOffice session for fast what-if recalculation of the model."""
import subprocess, time, os, uno
from com.sun.star.beans import PropertyValue

def _pv(name, value):
    p = PropertyValue(); p.Name = name; p.Value = value; return p

class Calc:
    def __init__(self, path, port=2032):
        self.profile = os.path.join(os.path.dirname(os.path.abspath(path)), '.lo_profile_uno')
        self.proc = subprocess.Popen(['soffice', '--headless', '--norestore', '--nologo', '--nodefault',
                                      f'-env:UserInstallation=file://{self.profile}',
                                      f'--accept=socket,host=127.0.0.1,port={port};urp;'],
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        local = uno.getComponentContext()
        resolver = local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', local)
        for _ in range(120):
            try:
                ctx = resolver.resolve(f'uno:socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext')
                break
            except Exception:
                time.sleep(0.5)
        else:
            raise RuntimeError('LibreOffice did not start')
        self.desktop = ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
        url = uno.systemPathToFileUrl(os.path.abspath(path))
        self.doc = self.desktop.loadComponentFromURL(url, '_blank', 0, (_pv('Hidden', True),))
        self.doc.calculateAll()

    def cell(self, sheet, ref):
        return self.doc.Sheets.getByName(sheet).getCellRangeByName(ref)

    def get(self, sheet, ref):
        c = self.cell(sheet, ref)
        return c.getValue() if c.getType().value in ('VALUE', 'FORMULA') and c.getString() != '' and not c.getFormula().startswith('=') or c.getFormula().startswith('=') else c.getValue()

    def val(self, sheet, ref):
        return self.cell(sheet, ref).getValue()

    def set(self, sheet, ref, v):
        self.cell(sheet, ref).setValue(v)

    def recalc(self):
        self.doc.calculateAll()

    def close(self):
        try:
            self.doc.close(True)
        except Exception:
            pass
        try:
            self.desktop.terminate()
        except Exception:
            pass
        self.proc.terminate()
