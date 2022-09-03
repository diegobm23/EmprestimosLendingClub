# Empréstimos feitos na Lending Club

Por Diego Moreira.

Este exercício tem como objetivo praticar Python com o uso das bibliotecas `pandas` e `matplotlib`.  Foi carregado um dataset e feito várias análises que estão detalhadas abaixo. 

## Dataset

Este conjunto de dados representa milhares de empréstimos feitos por meio da plataforma Lengding Club, cuja qual permite que indivíduos empreste dinheiro para indivíduos. O *dataset* está versionado neste repositório, mas também pode ser obtido através deste [link](https://vincentarelbundock.github.io/Rdatasets/csv/openintro/loans_full_schema.csv) e a documentação da colunas estão neste [link](https://vincentarelbundock.github.io/Rdatasets/doc/openintro/loans_full_schema.html).

- **Quantidade de Colunas**: 55

- **Quantidade de Linhas**: 10.000

## Gráficos

Gráfico de pizza com as porcentagens dos propósitos dos empréstimos.

![](https://lh3.googleusercontent.com/drive-viewer/AJc5JmRqPbcdHhnYZDG0TO0SqYN2E75P_XsU3IZw2R_lOOdGx70tRx4DIzv4MCK9BDWthB2YyjPvXvs=w1920-h924)

```python
def loan_purpose():
    sub_loans = loans.groupby(["loan_purpose"])["loan_purpose"].count()
    sub_loans.plot(kind="pie", autopct='%1.1f%%', figsize=(10, 10), ylabel='', title="Percentual dos motivos para empréstimo")
    plt.show()
```

---

Gráfico de linha com a média de renda anual de professores por tempo de serviço.

![](https://lh3.googleusercontent.com/drive-viewer/AJc5JmSLfax8_2HQxzH0e5PT7iXIMtfNZKTI2W4MgCvUzrxQj72JtAZTdNUySi_pu7ea8EG2KoICMRM=w1920-h924)

```python
def annual_income_avg_teacher():
    sub_loans_clean = loans[["emp_title", "emp_length", "annual_income"]].dropna()
    sub_loans = sub_loans_clean[sub_loans_clean.emp_title == "teacher"][["emp_length", "annual_income"]]
    sub_loans = sub_loans.groupby("emp_length").mean()
    sub_loans.plot(figsize=(10, 10), title="Renda anual de professores por tempo de serviço")
    plt.show()
```

---

Gráfico em barras com a média de valores emprestados por renda anual das 25 maiores rendas.

![](https://lh3.googleusercontent.com/drive-viewer/AJc5JmQcXYDnL3KHIepjQuzvXtkBF-OEgoOEMBU1fcaGYLIUGo9RX5Becd0D3mnMUjSl2PCkTa2Huk4=w1920-h924)

```python
def loan_amount_avg_annual_income():
    sub_loans = loans[["annual_income", "loan_amount"]]
    sub_loans = sub_loans.groupby("annual_income").mean()
    sub_loans.tail(25).plot(kind='bar', figsize=(10, 10), title="Valor médio emprestado por renda anual")
    plt.show()
```

## Perguntas

**Quantos software engineers fizeram empréstimo?**

![](https://lh3.googleusercontent.com/drive-viewer/AJc5JmR21Nz3rQjBYT7u6K2WCJeR7i2UfX_ikMJIu7LBzIKmonu351OamTfPXZU7ZnKQeyMoM7ddPY4=w1920-h924)

```python
def amount_software_engineer():
    amount_se = loans[loans.emp_title == "software engineer"]["loan_purpose"].count()
    print("\n*************************************************************")
    print("Quantidade de software engineers que fizeram empréstimo: ", amount_se)
    print("*************************************************************")
```

---

**Quais profissões mais pagaram taxa de atraso?**

![](https://lh3.googleusercontent.com/drive-viewer/AJc5JmRnljPyJSvqjVZIx3vgS49zLxn5mPIL0CoQPoDkPWlNue7z4Fh7XnxJHteFkX_qSr9gsQ4rlEs=w1920-h924)

```python
def emp_paid_late_fees():
    sub_loans = loans[loans.paid_late_fees > 0]
    sub_loans = sub_loans.groupby(["emp_title"])["emp_title"].count()
    print("\n*************************************************************")
    print("As profissões que mais pagaram taxa de atraso:")
    print(sub_loans.sort_values(ascending=False))
    print("*************************************************************")
```

---

**Qual a média de valor emprestado entre as pessoas que não comprovaram renda?**

![](https://lh3.googleusercontent.com/drive-viewer/AJc5JmRd1X1-X7GFsMFtbJnKnxNKCRnDPzeXbv9zqjrqDjbwW9rC837aqpxL34ZXGhE_nUlobrgUOkY=w1920-h924)

```python
def avg_loan_amount_not_verified():
    avg_value = loans[loans.verified_income == "Not Verified"]["loan_amount"].mean()
    print("\n*************************************************************")
    print("Valor médio emprestado por quem não comprovou renda: ${:,.2f}".format(avg_value))
    print("*************************************************************")
```

---

**Qual o valor total dos empréstimos pagos?**

![](https://lh3.googleusercontent.com/drive-viewer/AJc5JmRx6U_bO6wV0Yw2W6P3JUctUQ-NwnC-gPd7rfWjf6P9pDArg6Pz8k-W1Rc_vZ-GGE-nAL4GonY=w1920-h924)

```python
def sum_fully_paid_loans():
    sum_value = loans[loans.loan_status == "Fully Paid"]["loan_amount"].sum()
    print("\n*************************************************************")
    print("Valor total dos empréstimos já pagos: ${:,.2f}".format(sum_value))
    print("*************************************************************")
```

----

**Quais as 5 profissões que mais efetuaram empréstimos?**

![](https://lh3.googleusercontent.com/drive-viewer/AJc5JmR0B-eVbhuCh6ZhmihXhMdfilStt5sDbCEQgDDfO91_veSa3OA7N1kIZ3HNMfXCBpF_scJWqUY=w1920-h924)

```python
def emp_title_top_loan():
    sub_loans = loans.groupby(["emp_title"])["emp_title"].count()
    print("\n*************************************************************")
    print("As 5 profissões que mais efetuaram empréstimos:")
    print(sub_loans.sort_values(ascending=False).head(5))
    print("*************************************************************")
```

## Correlações

**Correlação entre renda anual e valor emprestado**

![](https://lh3.googleusercontent.com/drive-viewer/AJc5JmRd1X1-X7GFsMFtbJnKnxNKCRnDPzeXbv9zqjrqDjbwW9rC837aqpxL34ZXGhE_nUlobrgUOkY=w1920-h924)

```python
def corr_income_loan():
    sub_loans = loans[["annual_income", "loan_amount"]]
    print("\n*************************************************************")
    print(sub_loans.corr(method="pearson"))
    print("*************************************************************")
```
