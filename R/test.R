# SALVA O AQRUIVO EM XLSX (EXCEL)
library(writexl)
write_xlsx(dados, path = 'Cliente.xlsx')

# ADICIONA MAIS UM REGISTRO
dados[nrow(dados) + 1, ] <- list('Guilherme', 35, 'M', 'TI', '')
print(dados)

# ATUALIZAR O ID DA COLUNA
dados[6, "salario"] <- 12327

# UMA NOVA COLUNA
dados['ano_contrado'] <- c(2017, 2018, 2017, 2023, 2024, 2025)

