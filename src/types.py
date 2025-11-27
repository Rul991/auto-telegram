from typing import List, Literal

CommandArgNames = Literal['str', 'int']
CommandArgTypes = int | str | float
CommandArgs = List[CommandArgNames]