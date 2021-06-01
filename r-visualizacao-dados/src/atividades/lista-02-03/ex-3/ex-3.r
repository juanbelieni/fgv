library('jsonlite')
library('tidyverse')
library('viridis')
library('hrbrthemes')

raw_data <- fromJSON('wakatime.json') %>%
  .$days

data <- raw_data %>%
  select(date, languages) %>%
  unnest(languages) %>%
  mutate(time = hours + minutes / 60) %>%
  select(date, time, language = name)


# raw_data <- read_file('wakatime.json') %>%
#   enter_object(days) %>%
#   gather_array() %>%
#   spread_all() %>%
#   enter_object(languages) %>%
#   select(date) %>%
#   mutate(languages = ..JSON) %>%
#   unnest(languages)
#
# dates <- raw_data %>% .$date
# languages <- raw_data %>%
#   .$languages %>%
#   map_dfr(~as.tibble(.))
#
# data <- merge(dates, languages) %>%
#   mutate(date = x, time = hours * 60 + minutes) %>%
#   select(date, time, name)

# data %>%
#   group_by(date, name) %>%
#   summarise(time = sum(time)) %>%
#   mutate(name = fct_lump(name, 3, w = time)) %>%
#   ggplot(aes(as.Date(date), time, fill = name)) +
#   geom_bar(stat = "identity", position = "dodge")

# data %>%
#   mutate(language = fct_lump(language, 5, w = time)) %>%
#   group_by(date, language) %>%
#   summarise(time = sum(time)) %>%
#   ggplot(aes(as.Date(date), time, fill = language)) +
#   geom_bar(stat = 'identity') +
#   scale_fill_viridis(discrete = TRUE)
  # guides(fill = FALSE)

theme_set(theme_ipsum_rc())

data %>%
  mutate(language = fct_lump(language, 5, w = time)) %>%
  group_by(date, language) %>%
  summarise(time = sum(time)) %>%
  ggplot(aes(as.Date(date), time, fill = reorder(language, time))) +
  geom_bar(stat = 'identity') +
  scale_fill_ipsum()

times <- data %>%
  mutate(language = fct_lump(language, 5, w = time)) %>%
  group_by(date, language) %>%
  summarise(time = sum(time)) %>%
  arrange(date, time)
