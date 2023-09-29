# all rule to build executable
NAME = mysqlite
SRC = *.c
CC = gcc
OBJ = $(SRC:.c=.o)
CFLAGS = -Wall -Werror -pedantic -Wextra

all: $(NAME)

%.o: %.c
	$(CC) $(OBJ) -c -o $@ $<

$(NAME): $(OBJ)
	$(CC) $(SRC) -o $(NAME)
