# -*- coding: utf-8 -*-

# pyKol - Gestion de colles en CPGE
# Copyright (c) 2018 Florian Hatat
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from django import template
register = template.Library()

@register.filter(expects_localtime=True)
def heure_pour_colloscope(value):
	if value.minute == 0:
		return "{:%H}".format(value)
	else:
		return "{:%H:%M}".format(value)

@register.filter
def position_tableur(pos):
	ligne = pos[0]
	colonne = pos[1]
	if colonne == 0:
		colonne_alpha = 'A'
	else:
		colonne_alpha = ''
		while colonne > 0:
			colonne, reste = divmod(colonne, 26)
			colonne_alpha = chr(ord('A') + reste) + colonne_alpha

	return "{colonne}{ligne}".format(
			ligne=ligne + 1,
			colonne=colonne_alpha)
