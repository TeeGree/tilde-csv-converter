def convertCsvContentsToTildeFormat(csvContents: list[str]) -> list[str]:
    tildeContents: list[str] = []
    for csvLine in csvContents:
        csvItems = csvLine.split(',')
        tildeContents.append('~'.join(csvItems))
    
    return tildeContents