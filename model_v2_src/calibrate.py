# -*- coding: utf-8 -*-
"""Write calib.json = base-case production labour and production D&A (2026E-2030E) from a recalculated build."""
import json, sys, openpyxl
path = sys.argv[1]
reg = json.load(open(path.rsplit('.', 1)[0] + '_reg.json'))
wb = openpyxl.load_workbook(path, data_only=True)
lab = [wb['人员与费用'][f"{c}{reg['人员与费用|cogs_staff']}"].value for c in 'HIJKL']
da = [wb['资本开支与折旧'][f"{c}{reg['资本开支与折旧|da_cogs']}"].value for c in 'HIJKL']
json.dump({'lab': [round(v, 6) for v in lab], 'da': [round(v, 6) for v in da]}, open('calib.json', 'w'))
print('calib', lab, da)
