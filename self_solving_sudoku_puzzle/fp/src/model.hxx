#pragma once

#include <ge211.hxx>
#include <cstdlib> // added
#include <vector> // added
#include <iostream> // added
// #include "puzzle_space.hxx"
#include "board.hxx"

using Position_set = std::vector<ge211::Position>;
// TODO: Sketch the structure of your model and declare its operations.

class Model
{
    // PRIVATE MEMBER VARIABLES
    Board board_;
    bool game_over_ = false;
    Puzzle game_puzzle_;
    bool game_hard_ = false;
    bool game_easy_ = false;
    bool want_hint_ = false;





    // will be used to move the game along, presumably will be
    // comprised of the helper functions above


    // starts the game on easy mode depending on the player's choice


    //starts the game on hard mode depending on the player's choice


    // algorithm that finds solution
    Board DFS_search_(Board);

    // implements DFS to solve the board


    void clear_board();

    // we dont know if "==" operators() are necessary but if we
    // find that they are we'll include them as we go along

    // Public Functions

public:

    // Constructor
    Model(int); // what does explicit mean?

    // solves board using DFS
    void solve_();

    // returns squares_left_ private member variable

    // returns game_over_ private member variable
    bool game_over(); // for controller

    // solves the game, prob not needed now


    // tells if the game has been reset


    // returns board_ private member variable for model to edit
    Board& board();

    // returns board_vector for view to read
    Board const& board_view() const;

    // changes want_hint_ to true;
    void give_hint();

    // changes want_hint_ back to false;
    void stop_hint();

    // for view determines message for completion on hard mode
    bool hard_mode() const;

    // for view determines message for completion on easy mode
    bool easy_mode() const;

    // for view determines message for when user quits
    bool game_over() const; // for view

    // highlights most limited cell when user asks
    bool want_hint() const;
};
