# -*- coding: utf-8 -*-

from .import models, fields


class CitasJagp(models.Model):
	_name = 'citasjagp.citasjagp'
	autor = fields.Char('Autor', required=True)
	cita = fields.Text('Cita', required=True)
	fecha_visualizacion = fields.Date('Fecha visualización', required=True)
	orden_visualizacion = fields.Integer('Orden visualización', required=True)
