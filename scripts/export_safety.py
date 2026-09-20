"""Keep spreadsheet applications from interpreting archive prose as formulas."""


def csv_cell(value):
    # csv.writer quotes separators, but quoting alone does not stop formulas.
    # Check past whitespace/control prefixes which spreadsheet importers trim.
    if isinstance(value, str):
        start = 0
        while start < len(value) and (value[start].isspace() or
                                     ord(value[start]) < 32 or value[start] == "\ufeff"):
            start += 1
        probe = value[start:]
        if probe.startswith(("=", "+", "-", "@", "＝", "＋", "－", "＠")):
            return "'" + value
    return value


def csv_row(values):
    return [csv_cell(value) for value in values]
