from odoo_csv_tools.lib import mapper
from odoo_csv_tools.lib.transform import Processor
from datetime import datetime


processor = Processor('client_file.csv', delimiter=';')
res_partner_mapping = {
    'id': mapper.m2o_map('my_import_res_partner', mapper.concat('_', 'Firstname', 'Lastname', 'Birthdate')),
    'name': mapper.concat(' ', 'Firstname', 'Lastname'),
    'birthdate': mapper.val('Birthdate', postprocess=lambda x: datetime.strptime(x, "%d/%m/%y").strftime("%Y-%m-%d 00:00:00")),
}
processor.process(res_partner_mapping, 'res.partner.csv', {'model': 'res.partner', 'context': "{'tracking_disable': True}", 'worker': 2, 'batch_size': 20})
processor.write_to_file("res_partner.sh", python_exe='', path='')
