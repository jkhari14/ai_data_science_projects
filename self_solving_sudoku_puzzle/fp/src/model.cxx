#include "model.hxx"
#include <vector> // added
#include <algorithm> // added
using namespace ge211;
using Stack = std::vector<Board>;
Model::Model(int game_mode)
{
    srand(std::time(NULL));
    Puzzle_constant pc;
    if (game_mode == 2)
    {
        game_puzzle_ = pc.hard[rand() % 2];
        game_hard_ = true;
    }
    if (game_mode == 1)
    {
        game_puzzle_ = pc.easy[rand() % 3];
        game_easy_ = true;
    }

    for (std::vector<int> move : game_puzzle_)
    {
        board_.update_({move[0],move[1]}, move[2]);
    }
}

Board& Model::board()
{
    return board_;
}

Board const& Model::board_view() const
{
    return board_;
}

void Model::clear_board()
{
    for (int i = 0; i<9; ++i) {
        for (int j = 0; j < 9; ++j) {
            board_.board_vector()[i][j].assigned = false;
            board_.board_vector()[i][j].cell_numbers = {1,2,3,4,5,6,7,8,9};
        }
    }
}

void Model::solve_() // not yet tested, may change to output board
// original input was Puzzle puzzle
{
    clear_board();
    for (std::vector<int> move : game_puzzle_)
    {
        board_.update_({move[0],move[1]}, move[2]);
    }

    Board solution = DFS_search_(board_);
    board_ = solution;
    game_over_ = true; // moved from top
}

Board Model::DFS_search_(Board state) // not tested yet
{
    Stack stack = {};
    stack.push_back(state);
    while (!(stack.empty()))
    {
        Board curr = stack.back(); // copy/store first board of the stack
        stack.pop_back(); // remove same board from stack
        if (curr.game_complete_())
        {return curr;}
        if (! curr.dead_end_f_())// may be able to put these back together
        {
            Position cc = curr.most_limited_cell();
            for (int num : curr.board_vector()[cc.x][cc.y].cell_numbers)
            {
                Board curr2 = curr; // want to copy board_ without changing og
                curr2.update_(cc, num);
                stack.push_back(curr2);
            }
        }
    }
    return Board {}; // could not return NULL
}


bool Model::game_over()
{
    return game_over_;
}

void Model::give_hint() // 'O'
{
    want_hint_ = true;
}

void Model::stop_hint() // 'I'
{
    want_hint_ = false;
}

bool Model::hard_mode() const
{
    return game_hard_;
}

bool Model::easy_mode() const
{
    return game_easy_;
}

bool Model::game_over() const
{
    return game_over_;
}

bool Model::want_hint() const
{
    return want_hint_;
}



