#pragma once

#include <ge211.hxx>
#include <cstdlib> // added
#include <vector> // added
#include <iostream> // added
#include "puzzle_space.hxx"

using Position_set = std::vector<ge211::Position>;

struct Cell
{
    std::vector<int> cell_numbers;
    bool assigned = false;
};

class Board
{
    friend struct Test_access;

    std::vector< std::vector<Cell> > board_;
    std::vector<std::vector<int>> sub_grids_ = {{0,1,2},{3,4,5},{6,7,8}};


public:

    Board();
    // this function will inspect to see if the user has entered a valid number
    // based on the rules of sudoku
    // we are considering moving this function to our main file
    bool valid_number_(ge211::Position, int) const;
    // will be a position type

    // this function will return true if every cell in the
    // sudoku board has a valid number
    bool game_complete_() const;

    // this function will return the a list of all cells that belong
    // in the sub_grid of the given position
    Position_set sub_grid_function_(ge211::Position);

    // this function will remove a number from a given cell's possibilities
    // according to the rules of sudoku
    void remove_if_exists_(std::vector<int>&, int); // supposed to be private

    // this function will tell you if a cell has no possible
    // numbers place when it has no more possibilities
    // and no valid number, it will be used as a helper
    // function to game_complete_() presumably
    bool dead_end_f_() const;

    // will be used to set the given cell after each move by the player
    void update_(ge211::Position, int);

    // will find the cell with the least possibilities in it.
    // may possibly be used to give players a hint on where to move
    ge211::Position most_limited_cell() const;

    // returns board_vector for board to access
    std::vector< std::vector<Cell> >& board_vector();

    // returns board_vector for board to read
    std::vector<std::vector<Cell>>const& board_vector_view() const;
};