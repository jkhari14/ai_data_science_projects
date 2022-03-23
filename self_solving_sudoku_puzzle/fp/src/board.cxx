#include "board.hxx"
#include <vector> // added
#include <algorithm> // added
Board::Board()
{
    for (int i = 0; i<9; ++i)
    {
        std::vector<Cell> row; // trying to declare a vector
        // that contains a list of cells
        for (int j = 0; j<9; ++j)
        {
            Cell cell;
            cell.cell_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9};
            row.push_back(cell);
        }
        board_.push_back(row);
    }
}

void Board::remove_if_exists_(std::vector<int> &possibilities, int x)
// the first input will need to be a cell
{
    if ( (std::find(possibilities.begin(), possibilities.end(), x)
    != possibilities.end() ))
    {
        possibilities.erase( std::find(possibilities.begin(),
                                       possibilities.end(), x) );
    }
}

ge211::Position Board::most_limited_cell() const
{
    int row = 0;
    int col = 0;
    size_t shortest_len = 9;
    for (int i = 0; i<9; ++i)
    {
        for (int j = 0; j<9; ++j)
        {
            if (! board_[i][j].assigned)
            {
                size_t current_length = board_[i][j].cell_numbers.size();
                if (current_length < shortest_len)
                {
                    row = i;
                    col = j;
                }
            }
        }
    }
    return ge211::Position {row, col};
}

bool Board::dead_end_f_() const
{
    for (int i = 0; i<9; ++i)
    {
        for (int j = 0; j<9; ++j)
        {
            if ((!board_[i][j].assigned) && board_[i][j].cell_numbers.empty())
                return true;
        }
    }
    return false;
}

bool Board::game_complete_() const
{
    bool complete = true;
    for (int i = 0; i<9; ++i)
    {
        for (int j = 0; j<9; ++j)
        {
            if ( (!board_[i][j].assigned) )
            {
                return false;
            }
        }
    }
    return complete;
}

Position_set Board::sub_grid_function_(ge211::Position position)
{
    Position_set p_set = {};
    for ( int row : sub_grids_[floor(position.x / 3)] )
    {
        for (int col : sub_grids_[floor(position.y / 3)])
        {
            p_set.push_back(ge211::Position {row, col});
        }
    }
    return p_set;
}

void Board::update_(ge211::Position position, int assignment)
{
    if ((std::find(board_vector()[position.x][position.y].cell_numbers.begin(),
                    board_vector()[position.x][position.y].cell_numbers.end()
                    , assignment)
                    != board_vector()[position.x][position.y].cell_numbers.end()
                    ))
    {
        board_[position.x][position.y].cell_numbers = {assignment};
        board_[position.x][position.y].assigned     = true;

        for (int             i = 0; i < 9; ++i) {
            if (!board_[position.x][i].assigned)
                remove_if_exists_(board_[position.x][i].cell_numbers,
                                  assignment);
        }
        for (int             i = 0; i < 9; ++i) {
            if (!board_[i][position.y].assigned)
                remove_if_exists_(board_[i][position.y].cell_numbers,
                                  assignment);
        }
        for (ge211::Position pos : sub_grid_function_(position)) {
            if (!board_[pos.x][pos.y].assigned)
                remove_if_exists_(board_[pos.x][pos.y].cell_numbers,
                                  assignment);

        }
    }

}


std::vector<std::vector<Cell>>& Board::board_vector()// & because
// warning
// appeared
{
    return board_;
}

std::vector<std::vector<Cell>>const& Board::board_vector_view() const
{
    return board_;
}

bool Board::valid_number_(ge211::Position position,int assignment) const
// if assignment is in cell number of given cell then the number is valid
{

    return std::find(board_[position.x][position.y].cell_numbers.begin(),
                     board_[position.x][position.y].cell_numbers.end(),
                     assignment) !=
           board_[position.x][position.y].cell_numbers.end();
}