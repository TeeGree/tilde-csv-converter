

from os import path
from tildeToCsv import convertTildeContentsToCsvFormat
from csvToTilde import convertCsvContentsToTildeFormat
from datetime import datetime

def getInitialFileContents():
    filename = input('Enter full path of file to convert: ')
    while not path.exists(filename):
        print('invalid file!')
        filename = input('Enter full path of file to convert: ')

    with open(filename, 'r') as initialFile:
        return initialFile.readlines()

initialFileContents = getInitialFileContents()

TILDE = 'TILDE'
COMMA = 'COMMA'

initialFileType = input(F'Is this file tilde delimited or comma delimited (enter {TILDE} or {COMMA}): ').upper()
while initialFileType != TILDE and initialFileType != COMMA:
    print('Invalid file type!')
    initialFileType = input(F'Is this file tilde delimited or comma delimited (enter {TILDE} or {COMMA}): ').upper()

if initialFileType == TILDE:
    resultFileContents = convertTildeContentsToCsvFormat(initialFileContents)
else:
    resultFileContents = convertCsvContentsToTildeFormat(initialFileContents)


timestamp = datetime.now().strftime("%m%d%Y%H%M%S")
with open(f'outputFile-{timestamp}.csv', 'w') as outputFile:
    outputFile.writelines(resultFileContents)