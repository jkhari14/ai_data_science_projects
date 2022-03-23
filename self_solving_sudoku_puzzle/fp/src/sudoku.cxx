#include "model.hxx"
#include "controller.hxx"
// #include <string>
// #include "view.hxx"
// #include "puzzle_space.hxx"
// #include "board.hxx"

using namespace std;

int main()
{
    for(;;)
    {
        std::cout << "Choose Level: 1 for Easy or 2 for Hard\n";
        int x;
        std::cin >> x;
        if (x == 1) {
            Controller(1).run();
            break;
        } else if (x == 2) {
            Controller(2).run();
            break;
        } else {
            std::cout << "Pick a viable game mode\n";
        }
    }
}
