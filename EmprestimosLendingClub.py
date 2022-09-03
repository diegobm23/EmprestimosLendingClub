import pandas as pd
import matplotlib.pyplot as plt

loans = pd.read_csv("/home/diegobm23/projetos-diegobm23/diego-scripts/Datasets/loans_full_schema.csv", low_memory=False)


# Gráfico de pizza com as porcentagens dos propósitos dos empréstimos
def loan_purpose():
    sub_loans = loans.groupby(["loan_purpose"])["loan_purpose"].count()
    sub_loans.plot(kind="pie", autopct='%1.1f%%', figsize=(10, 10), ylabel='', title="Percentual dos motivos para empréstimo")
    plt.show()


# Gráfico de linha com a média de renda anual de professores por tempo de serviço
def annual_income_avg_teacher():
    sub_loans_clean = loans[["emp_title", "emp_length", "annual_income"]].dropna()
    sub_loans = sub_loans_clean[sub_loans_clean.emp_title == "teacher"][["emp_length", "annual_income"]]
    sub_loans = sub_loans.groupby("emp_length").mean()
    sub_loans.plot(figsize=(10, 10), title="Renda anual de professores por tempo de serviço")
    plt.show()


# Gráfico em barras com a média de valores emprestados por renda anual das 25 maiores rendas
def loan_amount_avg_annual_income():
    sub_loans = loans[["annual_income", "loan_amount"]]
    sub_loans = sub_loans.groupby("annual_income").mean()
    sub_loans.tail(25).plot(kind='bar', figsize=(10, 10), title="Valor médio emprestado por renda anual")
    plt.show()


# Gráficos
loan_purpose()
annual_income_avg_teacher()
loan_amount_avg_annual_income()


# Quantos software engineers fizeram empréstimo?
def amount_software_engineer():
    amount_se = loans[loans.emp_title == "software engineer"]["loan_purpose"].count()
    print("\n*************************************************************")
    print("Quantidade de software engineers que fizeram empréstimo: ", amount_se)
    print("*************************************************************")


# Quais profissões mais pagaram taxa de atraso?
def emp_paid_late_fees():
    sub_loans = loans[loans.paid_late_fees > 0]
    sub_loans = sub_loans.groupby(["emp_title"])["emp_title"].count()
    print("\n*************************************************************")
    print("As profissões que mais pagaram taxa de atraso:")
    print(sub_loans.sort_values(ascending=False))
    print("*************************************************************")


# Qual a média de valor emprestado entre as pessoas que não comprovaram renda?
def avg_loan_amount_not_verified():
    avg_value = loans[loans.verified_income == "Not Verified"]["loan_amount"].mean()
    print("\n*************************************************************")
    print("Valor médio emprestado por quem não comprovou renda: ${:,.2f}".format(avg_value))
    print("*************************************************************")


# Qual o valor total dos empréstimos pagos?
def sum_fully_paid_loans():
    sum_value = loans[loans.loan_status == "Fully Paid"]["loan_amount"].sum()
    print("\n*************************************************************")
    print("Valor total dos empréstimos já pagos: ${:,.2f}".format(sum_value))
    print("*************************************************************")


# Quais as 5 profissões que mais efetuaram empréstimos?
def emp_title_top_loan():
    sub_loans = loans.groupby(["emp_title"])["emp_title"].count()
    print("\n*************************************************************")
    print("As 5 profissões que mais efetuaram empréstimos:")
    print(sub_loans.sort_values(ascending=False).head(5))
    print("*************************************************************")


# Perguntas
amount_software_engineer()
emp_paid_late_fees()
avg_loan_amount_not_verified()
sum_fully_paid_loans()
emp_title_top_loan()


# Correlação entre renda anual e valor emprestado
def corr_income_loan():
    sub_loans = loans[["annual_income", "loan_amount"]]
    print("\n*************************************************************")
    print(sub_loans.corr(method="pearson"))
    print("*************************************************************")


# Correlações
corr_income_loan()
