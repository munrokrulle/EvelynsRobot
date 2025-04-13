input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . . # # .
        . # . . #
        # . . # .
        . # # # #
        `)
    music.play(music.stringPlayable("C5 B A G F E D C ", 120), music.PlaybackMode.UntilDone)
})
music.setVolume(127)
basic.showString("Hello World!")
