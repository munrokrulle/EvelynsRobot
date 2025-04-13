def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . . # # .
        . # . . #
        # . # # .
        . # # # #
        """)
    music.play(music.string_playable("E C A E D A E C ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

music.set_volume(127)
basic.show_string("Hello World!")