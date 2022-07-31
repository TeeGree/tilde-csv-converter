# Summary
Simple Python script that supports converting tilde delimited files to csv or vice versa.

# How to run
```
py main.py
```

Provide the full path to the csv or tilde delimited file.
```
Enter full path of file to convert: C:\Path\To\file.csv
```

Enter "TILDE" for converting tilde delimited file to csv.
Enter "COMMA" for converting csv file to tilde delimited file.

This is case insensitive.
```
Is this file tilde delimited or comma delimited (enter TILDE or COMMA): comma
```

The output file will be in the cmd directory in the format: "outputFile-{timestamp}.csv". This will not modify the original file at all.