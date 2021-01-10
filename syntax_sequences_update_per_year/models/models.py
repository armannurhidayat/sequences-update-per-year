# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
import calendar


class Sequence(models.Model):
	_inherit = 'ir.sequence'

	def update_sequences_per_year(self):
		cr = self.env.cr
		cr.execute('select id from ir_sequence where use_date_range=true')
		for rec in cr.fetchall():
			# Delete data yang sudah ada
			cr.execute('delete from ir_sequence_date_range where sequence_id={}'.format(rec[0]))

			# Insert data
			for i in range(1, 13):
				now 		= datetime.datetime.now()
				date_from	= datetime.datetime.strptime("{}-{}-{}".format(1, i, now.year+1), '%d-%m-%Y').date()
				date_to		= datetime.datetime.strptime("{}-{}-{}".format(calendar.monthrange(now.year+1, i)[1], i, now.year+1), '%d-%m-%Y').date()
				sql = """insert into ir_sequence_date_range (date_from, date_to, sequence_id, number_next) 
							values('{}', '{}', {}, 1)""".format(date_from, date_to, rec[0])
				cr.execute(sql)
