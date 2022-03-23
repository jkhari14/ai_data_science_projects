#pragma once

#include <ge211.hxx>
#include <cstdlib> // added
#include <vector> // added
#include <iostream> // added
#include "model.hxx"
#include <string>



class View
{
public:
    explicit View(Model const&);

    enum class Message
    {
        Invalid_Input,
        Pick_Number,
        Solving,
        Easy_Solve,
        None
    };

    // You will probably want to add arguments here so that the
    // controller can communicate UI state (such as a mouse or
    // cursor position):
    void draw(ge211::Sprite_set& set, ge211::Position, Message);

    ge211::Dimensions initial_window_dimensions() const;

    std::string initial_window_title() const;

    ge211::Position board_to_screen(ge211::Position) const ;

    ge211::Position screen_to_board(ge211::Position) const ;

private:
    Model const& model_;

    // TODO: Add any private members you need, such as helper functions

    //SPRITES

    ge211::Rectangle_sprite const
                game_board_ {{38, 38}, ge211::Color(210, 180, 140)};
    ge211::Rectangle_sprite const
            selected_cell_square_ {{38,38}, ge211::Color(255, 0, 0)};
    ge211::Rectangle_sprite const
                hinted_cell {{38, 38}, ge211::Color(0, 255, 0)};
    ge211::Rectangle_sprite const
                game_over_ {{128, 30}, ge211::Color(250, 0, 0)};
    ge211::Rectangle_sprite const
            game_over_2 {{264, 30}, ge211::Color(250, 0, 0)};
    ge211::Rectangle_sprite const
                message_ {{128, 30}, ge211::Color(0, 0, 0)};
    ge211::Font sans72 {"sans.ttf", 20};
    ge211::Text_sprite const
                game_over_text_ {"You Solved it!", sans72 };
    ge211::Text_sprite const
                game_over_text2_ {"The Solution!", sans72 };
    ge211::Text_sprite const
                easy_complete_ {"Good Job!", sans72 };
    ge211::Text_sprite const
                hard_complete_ {"Fantastic!", sans72 };
    ge211::Text_sprite const
                what_number_ {"Press the Number you want", sans72 };
    ge211::Text_sprite const
                invalid_input_ {"Invalid Input, try again.", sans72 };
    ge211::Text_sprite const
            solving_ts_ {"Check your Phone while this Solves", sans72 };
    ge211::Text_sprite const
            dead {"You've hit a dead end :( ", sans72 };
    std::vector<ge211::Text_sprite>
            number_sprites_;
    /*
    ge211::Text_sprite const
                choose_level_{"Choose Level: 1 for Easy or 2 for Hard",
                              sans72 };

    ge211::Text_sprite const
                choose_level_error_{"Pick a viable game mode",sans72 };
                */
};
