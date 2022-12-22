#include "pygame.cpp"

struct bitmap_image elf = bitmap_read_file("c1.bmp");
struct bitmap_image kings[30];
struct bitmap_image waldo = bitmap_read_file("c2-back.bmp");
struct bitmap_image naruto = bitmap_read_file("naruto.bmp");
int game_over = 0;

void update(struct keyboard* kbd) {
    int diff = 10;
    if (kbd->A)
        elf.r.x += diff;
    if (kbd->D)
        elf.r.x -= diff;
    if (kbd->S)
        elf.r.y += diff;
    if (kbd->W)
        elf.r.y -= diff;

    for (int i = 0; i < 30; i++) {
        if (collide(elf.r, kings[i].r)) {
            play("a.wav");
        }
    }

    if (collide(waldo.r, elf.r)) {
        game_over = 1;
        play("b.wav");
    }
}

void draw(struct screen_buffer* screen) {
    screen_clear(screen, 255 << 16 | 255 << 8 | 255);

    for (int i = 0; i < 30; i++) {
        bitmap_draw(kings[i], screen);
    }

    bitmap_draw(waldo, screen);
    bitmap_draw(elf, screen);

    if (game_over) {
        screen_clear(screen, 0);
        bitmap_draw(naruto, screen);
    }
}

int CALLBACK WinMain(HINSTANCE Instance,
                     HINSTANCE PrevInstance,
                     LPSTR CmdLine,
                     int ShowCmd) {
    srand(time(NULL));

    for (int i = 0; i < 30; i++) {
        kings[i] = bitmap_read_file("c2.bmp");
        kings[i].r.x = 100 + rand() % 600;
        kings[i].r.y = 100 + rand() % 600;
    }
    waldo.r.x = 100 + rand() % 600;
    waldo.r.y = 100 + rand() % 600;

    initialize(Instance, "zero", update, draw);

    return 0;
}
