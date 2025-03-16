# https://leetcode.com/problems/design-spreadsheet/description/


class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}
        self.rows = rows
        

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value
        

    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]
        

    def getValue(self, formula: str) -> int:
        if not formula.startswith("="):
            raise ValueError("Invalid formula format")

        # Extract the expression after the '='
        expression = formula[1:]
        
        # Split by '+' to handle addition
        parts = expression.split("+")

        total = 0
        for part in parts:
            part = part.strip()
            if part.isdigit():
                # If the part is a number, add it to the total
                total += int(part)
            else:
                # If the part is a cell reference, look up its value
                total += self.cells.get(part, 0)

        return total

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
