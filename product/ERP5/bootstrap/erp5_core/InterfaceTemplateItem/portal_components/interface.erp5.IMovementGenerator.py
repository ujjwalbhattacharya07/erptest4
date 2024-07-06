# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2009 Nexedi SA and Contributors. All Rights Reserved.
#                    Jean-Paul Smets-Solanes <jp@nexedi.com>
#                    Lukasz Nowak <luke@nexedi.com>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsibility of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# guarantees and support are strongly advised to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
##############################################################################
"""
erp5.component.interface.IMovementGenerator
"""

from zope.interface import Interface

class IMovementGenerator(Interface):
  """Movement Generator interface specification

  Documents which implement IMovementGenerator
  can be used to generate an IMovementList from
  an existing IMovementCollection, IMovementList or
  IMovement. Typical IMovementGenerator are Rules
  and Trade Conditions.
  """

  def getAggregatedMovementList(movement_list=None, rounding=False):
    """
    Returns an IMovementList generated by a model applied to the context
    and aggregated according to the context divergence testers.

    movement_list - optional IMovementList which can be passed explicitely
                    whenever context is an IMovementCollection and whenever
                    we want to filter context.getMovementList

    rounding - boolean argument, which controls if rounding shall be applied on
               generated movements or not

    NOTE:
      - implement rounding appropriately (True or False seems
        simplistic)
      - define how to retrieve divergence testers in the context
    """

  def getGeneratedMovementList(movement_list=None, rounding=False):
    """
    Returns an IMovementList generated by a model applied to the context

    movement_list - optional IMovementList which can be passed explicitely
                    whenever context is an IMovementCollection and whenever
                    we want to filter context.getMovementList

    rounding - boolean argument, which controls if rounding shall be applied on
               generated movements or not

    NOTE:
      - implement rounding appropriately (True or False seems
        simplistic)
    """
