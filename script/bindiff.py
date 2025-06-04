import idc
import idaapi
import os

idaapi.auto_wait()
idaapi.save_database(None, 0)

input_path = idaapi.get_input_file_path()
base_name = os.path.splitext(os.path.basename(input_path))[0]
export_filename = f"{base_name}.BinExport"

idaapi.ida_expr.eval_idc_expr(None, ida_idaapi.BADADDR,
  f'BinExportBinary("{export_filename}");')



idaapi.qexit(0)
