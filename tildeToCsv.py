import re


def convertTildeContentsToCsvFormat(tildeContents: list[str]) -> list[str]:
    csvContents: list[str] = []
    commaRegex = re.compile(',')
    quoteRegex = re.compile('"')
    for tildeLine in tildeContents:
        tildeItems = tildeLine.split('~')
        csvItems: list[str] = []
        for tildeItem in tildeItems:
            csvItem = tildeItem
            if commaRegex.search(tildeItem) is not None and (tildeItem[0] != '"' or tildeItem[-1] != '"'):
                if quoteRegex.search(tildeItem) is not None:
                    csvItem = csvItem.replace('"', '""')
                csvItem = f'"{csvItem}"'
            csvItems.append(csvItem)
        csvContents.append(','.join(csvItems))
    
    return csvContents