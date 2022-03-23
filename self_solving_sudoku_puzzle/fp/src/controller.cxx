#include "model.hxx"
#include "iostream"
#include "controller.hxx"
using namespace ge211;

Controller::Controller(int game_mode)
        : model_(game_mode) // how should I change this
        , view_(model_)
{ }

void Controller::draw(ge211::Sprite_set& sprites)
{
    view_.draw(sprites, selected_pos_, message);
}

ge211::Dimensions Controller::initial_window_dimensions() const
{
    return view_.initial_window_dimensions();
}

std::string Controller::initial_window_title() const
{
    return view_.initial_window_title();
}

void Controller::on_mouse_up(ge211::Mouse_button, ge211::Position pos)
{
    pos = view_.screen_to_board(pos);
    if (0 <= pos.x && pos.x <= 8 && 0 <= pos.y && pos.y <= 8)
    {
        if ((!model_.board().board_vector()[pos.x][pos.y].assigned))
        {
            selected_pos_ = pos; // clicked cell equals pos
            message = View::Message::Pick_Number;// prompt user unit valid input
        }
    }
}

void Controller::on_key_down(ge211::Key key)
{
    if (key == ge211::Key::code('q')) {
         // remove last one
        message = View::Message::Solving; // Solving
        model_.solve_();
        model_.game_over();
        message = View::Message::None; // Solved!
    }
    else if (key == ge211::Key::code('o')) {
        model_.give_hint();
    }
    else if (key == ge211::Key::code('i')) {
        model_.stop_hint();
    }
    else if (key == ge211::Key::code('e'))
    {
        model_.solve_();
        message = View::Message::Easy_Solve;
    }
    else if (selected_pos_.x != -1 && '1' <= key.code() && key.code() <= '9')
    {
        int assignment = key.code() - '0';
        if (model_.board().valid_number_(selected_pos_, assignment)) {
            model_.board().update_(selected_pos_, assignment);
            message = View::Message::None;
        }
        else {
            message = View::Message::Invalid_Input; // print invalid message
        }
    }
}

void Controller::on_mouse_move(ge211::Position mouse_pos)
{
    mouse_pos_ = mouse_pos; //added mouse_pos_ = mouse_pos;

}


