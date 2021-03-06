# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:17:11 2020

@author: Korean_Crimson
"""

from token_ import resolution_order_dict
from parser_ import Block

class InterpreterError(Exception):
    def __init__(self, block):
        self.message = f'The following block had no type to be interpreted: {block}!'
        super().__init__(self.message)

class Interpreter:
    def __init__(self):
        self.stack = []
        self.variables = {}

    def interpret(self, block):
        blocks = [statement for statement in block if isinstance(statement, Block)]
        for block_ in blocks:
            self.interpret(block_)
        resolution_order = self.determine_resolution_order(block)
        statements = [block[i] for i in resolution_order]
        for statement in statements:
            if not isinstance(statement, Block):
                statement.run(self)

    def determine_resolution_order(self, block):
        try:
            return resolution_order_dict[block.type]
        except:
            raise InterpreterError(block)
