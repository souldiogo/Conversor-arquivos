dados <- read.csv("br_anatel_indice_brasileiro_conectividade_municipio.csv", header = TRUE, sep = ";")
head(dados, 10)

# municípios apresentam os maiores e menores índices
library(dplyr)
dados %>%
  group_by(sigla_uf) %>%
  summarise(media_ibc = mean(ibc, na.rm = TRUE)) %>%
  arrange(desc(media_ibc))

# Gráfico de dispersão com linha de tendência:
plot(dados$cobertura_pop_4g5g, dados$ibc, 
     xlab = "Cobertura pop 4G/5G (%)", ylab = "Indice de conectividade (IBC)", 
     main = "Relação entre cobertura 4G/5G e IBC", pch = 19, col = "steelblue")
abline(lm(ibc ~ cobertura_pop_4g5g, data = dados), col = 'red', lwd = 2)

