#include "model.hxx"
#include <catch.hxx>
#include "board.hxx"

struct Test_access
{
    Board m;
    std::vector< std::vector<Cell> >& board()
    {
        return m.board_;
    }

    void update_(ge211::Position position, int assignment)
    {
        return m.update_(position, assignment);
    }

    bool valid_number_(ge211::Position position,int assignment)
    {
        return m.valid_number_(position, assignment);
    }

    bool game_complete_()
    {
        return m.game_complete_();
    }

    void remove_if_exists_(std::vector<int>& cell, int poss) // how?
    {
        return m.remove_if_exists_(cell, poss);
    }

    ge211::Position most_limited_cell()
    {
        return m.most_limited_cell();
    }

    Position_set sub_grid_function_(ge211::Position position)
    {
        return m.sub_grid_function_(position);
    }

};

TEST_CASE("remove_if_exists")
{
    Board m;
    std::vector<int> list = {1,2,3,4};
    int number = 3;
    m.remove_if_exists_(list, number);
    CHECK(list == std::vector<int> {1,2,4});
    std::vector<int> list2 = {1};
    int number2 = 1;
    m.remove_if_exists_(list2, number2);
    CHECK(list2.empty());
}

TEST_CASE ("Model board working correctly")
{
    Board m;
    std::vector<std::vector<Cell>> test_grid = m.board_vector();
    CHECK(test_grid[0][0].cell_numbers == std::vector<int> {1, 2, 3, 4, 5, 6,
                                                            7, 8, 9});
    CHECK(test_grid[7][8].cell_numbers == std::vector<int> {1, 2, 3, 4, 5, 6,
                                                            7, 8, 9});
    CHECK_FALSE(test_grid[0][0].assigned);
    CHECK_FALSE(test_grid[0][0].assigned);
}

TEST_CASE ("Most Limited Cell")
{
    Test_access m;
    m.board()[0][0].cell_numbers = std::vector<int> {1, 2, 4, 5, 7, 8, 9};
    m.board()[2][3].cell_numbers = std::vector<int> {2, 4, 5, 7};
    m.board()[1][6].cell_numbers = std::vector<int> {2};
    m.board()[1][6].assigned = true;
    m.board()[8][8].cell_numbers = std::vector<int> {2,5};
    CHECK(m.most_limited_cell() == ge211::Position {8,8});
}

TEST_CASE ("Dead end function")
{
    Test_access m;
    m.m.dead_end_f_(); //  runs dead_end_f
    CHECK_FALSE(m.m.dead_end_f_());
    m.board()[5][5].cell_numbers = std::vector<int> {};
    CHECK(m.board()[5][5].cell_numbers.empty());
    m.board()[5][5].assigned = false;
    CHECK(m.m.dead_end_f_()); //accesses private member dead_end_
}

TEST_CASE("Subgrid Function")
{
    Test_access m;
    CHECK(m.sub_grid_function_({3,4}) == Position_set {{3,3}, {3,4}, {3,5},
                                              {4,3}, {4,4}, {4,5},
                                              {5,3}, {5,4}, {5,5}});
}

TEST_CASE("Update Function")
{
    Test_access m;
    m.update_({0,0}, 5);
    CHECK(m.board()[0][0].cell_numbers == std::vector<int> {5});
    CHECK(m.board()[0][0].assigned);
    for (int i = 1; i<9; ++i)
    {
        CHECK(m.board()[0][i].cell_numbers == std::vector<int> {1,2,3,
                                                                4,6,7,
                                                                8,9});
    }
    for (int i = 1; i<9; ++i)
    {
        CHECK(m.board()[i][0].cell_numbers == std::vector<int> {1,2,3,
                                                                4,6,7,
                                                                8,9});
    }
    for (ge211::Position pos : m.sub_grid_function_({0,0}))
    {
        if (pos != ge211::Position {0,0})
        {
            CHECK(m.board()[pos.x][pos.y].cell_numbers ==
                  std::vector<int>{1, 2, 3,
                                   4, 6, 7,
                                   8, 9});
        }
    }
}

TEST_CASE("Update Function #2")
{
    Test_access m;
    for (int i = 0; i<9; ++i) {
        for (int j = 0; j < 9; ++j) {
            m.board()[i][j].cell_numbers = {};
        }
    }
    m.update_({5,6}, 7);
    CHECK_FALSE(m.board()[5][6].cell_numbers == std::vector<int> {7});
}



TEST_CASE("Valid Number Test")
{
    Test_access m;
    m.board()[0][0].cell_numbers = std::vector<int> {1, 2, 4, 5, 7, 8, 9};
    m.board()[2][3].cell_numbers = std::vector<int> {2, 4, 5, 7};
    m.board()[8][8].cell_numbers = std::vector<int> {2,5};
    CHECK(m.valid_number_({0,0}, 4));
    CHECK_FALSE(m.valid_number_({0,0}, 6));
    CHECK(m.valid_number_({2,3}, 7));
    CHECK_FALSE(m.valid_number_({2,3}, 1));
    CHECK(m.valid_number_({1,6}, 8));
    m.update_({1,6}, 2);
    CHECK_FALSE(m.valid_number_({2,6}, 2));
    CHECK_FALSE(m.valid_number_({1,7}, 2));
    CHECK_FALSE(m.valid_number_({2,8}, 2));
}


TEST_CASE("Game Complete Function")
{
    Test_access m;
    for (int i = 0; i<9; ++i) {
        for (int j = 0; j < 9; ++j) {
            m.board()[i][j].assigned = true;
        }
    }
    CHECK(m.game_complete_());
}
//
// TODO: Write preliminary model tests.
//
// These tests should demonstrate at least six of the functional
// requirements.
//

