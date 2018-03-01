from enum import Enum
import pandas as pd

class DataType(Enum):
    Numeric = 1,
    QualitativeOrdered = 2
    QualitativeUnordered = 3


DataTypes = [DataType.QualitativeOrdered, #1. Status of existing checking account
            DataType.Numeric, #2. Duration in month
            DataType.QualitativeOrdered, #3. Credit history
            DataType.QualitativeUnordered, #4. Purpose
            DataType.Numeric, #5. Credit amount
            DataType.QualitativeOrdered, #6. Savings account/bonds
            DataType.QualitativeOrdered, #7. Present employment since
            DataType.Numeric, #8. Installment rate in percentage of disposable income
            DataType.QualitativeUnordered, #9. Personal status and sex
            DataType.QualitativeOrdered, #10. Other debtors / guarantors
            DataType.Numeric, #11. Present residence since
            DataType.QualitativeUnordered, #12. Property
            DataType.Numeric, #13. Age in years
            DataType.QualitativeUnordered, #14. Other installment plans
            DataType.QualitativeUnordered, #15. Housing
            DataType.Numeric, #16. Number of existing credits at this bank
            DataType.QualitativeOrdered, #17. Job
            DataType.Numeric, #18. Number of people being liable to provide maintenance for
            DataType.QualitativeOrdered, #19. Telephone
            DataType.QualitativeUnordered,
            DataType.QualitativeUnordered] #20. Foreign worker
data = []
with open('../german.data', 'r') as f:
    while(True):
        line = f.readline()
        if line == '':
            break
        data.append([int(c if DataTypes[i] == DataType.Numeric else c.replace('\n', '')[-1])
                     for i, c in enumerate(line.split(' '))])



dataset = pd.read_csv('../german.csv', index_col=0, parse_dates=True)
print(dataset.groupby(['Job'])['risk'].mean())