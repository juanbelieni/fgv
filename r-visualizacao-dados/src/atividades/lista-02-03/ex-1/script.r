library("ggplot2")
library("dplyr")
library("gapminder")

gapminder %>%
  filter(year == 2007) %>%
  group_by(continent) %>%
  summarise(pop = sum(pop)) %>%
  ggplot(aes(continent, pop, fill = continent)) +
  guides(fill = FALSE) +
  labs(x = "Continente", y = "População") +
  geom_col()

ggsave("model-chart.png", width = 8)