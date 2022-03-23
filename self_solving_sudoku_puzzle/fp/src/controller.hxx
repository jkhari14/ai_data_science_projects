#pragma once

// #include <ge211.hxx> // added
// #include <cstdlib> // added
// #include <vector> // added
// #include <iostream> // added
#include "model.hxx"
#include "view.hxx"

// The main game class for Sudoku
class Controller : public ge211::Abstract_game
{
public:

    // Constructs a game

    Controller(int);


// `protected` means that GE211 (via base class `ge211::Abstract_game`)
// can access these members, but arbitrary other code cannot:
protected:
    //
    // Controller operations called by GE211
    //

    // TODO: Add any input handlers you need, e.g.:
    //  - on_mouse_up for mouse clicks,
    //  - on_mouse_move for mouse tracking, or
    //  - on_frame for animation (?).

    void on_mouse_up(ge211::Mouse_button, ge211::Position) override;
    void on_mouse_move(ge211::Position) override;
    void on_key_down(ge211::Key) override;
    // These three delegate to the view:
    void draw(ge211::Sprite_set&) override; //added
    // ge211::Position
    ge211::Dimensions initial_window_dimensions() const override;
    std::string initial_window_title() const override;

private:
    Model           model_;
    View            view_;
    ge211::Position mouse_pos_    = {0,0}; // just leave here
    ge211::Position selected_pos_ = {-1, -1}; // sentinel value pos

    View::Message message = View::Message::None;



    // TODO: Add any UI state you need, e.g.:
    //  - the position of the mouse, or
    //  - the position of a keyboard-controller cursor.
};