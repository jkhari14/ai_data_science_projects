// #include "model.hxx"
// using namespace ge211;
#include "view.hxx"

// Convenient type aliases:
using Dimensions = ge211::Dimensions;
using Position   = ge211::Position;
using Color      = ge211::Color;
using Sprite_set = ge211::Sprite_set;



// You can change this or even determine it some other way:
static int const grid_size = 50; // originally 40

View::View(Model const& model)
        : model_(model)
// You may want to add sprite initialization here
{
    for (int i = 1; i<=9; ++i )
    {
        ge211::Text_sprite::Builder number_builder(sans72);
        number_builder << i;
        number_sprites_.push_back(number_builder.build());
    }
}

void View::draw(Sprite_set& set, ge211::Position selected_pos, Message message)
// ge211::Position mouse_pos
{
    // TODO, PROBABLY


    // BOARD MAKER
    for (int i = 0; i < 360; i += 40) { // i went to 360 because that appears
        // to be size of screen
        for (int j = 0; j < 360; j += 40) {
            set.add_sprite(game_board_, {i,j}, -1);
        }
    }

    // GAME IS OVER STATEMENT
    if ((model_.board_view().game_complete_() && (!model_.game_over())) ||
    message == Message::Easy_Solve)
    {
        set.add_sprite(game_over_, {38, 390}, 3);
        set.add_sprite(game_over_text_, {38, 390,}, 4);
        if (model_.hard_mode())
            set.add_sprite(hard_complete_, {224,390}, 4);
        if (model_.easy_mode())
            set.add_sprite(easy_complete_, {224,390}, 4);
    }

    if (model_.game_over() && message != Message::Easy_Solve)
    {
        set.add_sprite(game_over_, {38, 390}, 3);
        set.add_sprite(game_over_text2_, {38, 390,}, 4);
    }

    // User Input
    if (selected_pos.x != -1)
    {
        set.add_sprite(selected_cell_square_, board_to_screen(selected_pos),0);
    }

    if (message == Message::Pick_Number)
    {
        set.add_sprite(message_, {38, 410}, 3);
        set.add_sprite(what_number_, {38, 390}, 4); // will change pos
    }

    else if (message == Message::Invalid_Input)
    {
        set.add_sprite(message_, {38, 390}, 3);
        set.add_sprite(invalid_input_, {38, 390}, 4); // will change pos
    }

    else if (message == Message::Solving)
    {
        set.add_sprite(message_, {38, 390}, 3);
        set.add_sprite(solving_ts_, {38, 390}, 4);
    }


    if (model_.board_view().dead_end_f_())
    {
        set.add_sprite(game_over_2, {68, 190}, 3);
        set.add_sprite(dead, {68, 190},4);
    }

    // Hint Indicator (Most Limited Cell)
    if (model_.want_hint())
    {
        Position hint = model_.board_view().most_limited_cell();
        Position pos1 = board_to_screen({hint.x, hint.y});
        set.add_sprite(hinted_cell, pos1, 2);
    }

    // Number Placer
    for (int i = 0; i<9; ++i) {
        for (int j = 0; j < 9; ++j) {
            Position pos2 = board_to_screen({i,j});
            if (model_.board_view().board_vector_view()[i][j].assigned)
            {
                int assignment = model_.board_view().board_vector_view()[i][j]
                        .cell_numbers[0];
                set.add_sprite(number_sprites_[assignment-1], pos2, 2);
            }
        }
    }

}

Dimensions View::initial_window_dimensions() const
{
    // You can change this if you want:
    return Dimensions {9*grid_size,9*grid_size};
    //
}

std::string View::initial_window_title() const
{
    // You can change this if you want:
    return "Sudoku";
}

ge211::Position View::board_to_screen(ge211::Position board_pos) const
{
    board_pos.x *= 40;
    board_pos.y *= 40;
    return board_pos;
}

ge211::Position View::screen_to_board(ge211::Position screen_pos) const
{
    screen_pos.x = screen_pos.x / 40;
    screen_pos.y  = screen_pos.y / 40;
    return screen_pos;
}
