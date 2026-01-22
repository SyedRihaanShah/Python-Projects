#The winsound module provides access to the basic sound-playing machinery provided by Windows platforms.
# It includes functions and several constants.
import winsound

winsound.Beep(150, 500) # Syntax - winsound.Beep(frequency in Hz, time in milliseconds)

winsound.PlaySound("alarm.wav", winsound.SND_FILENAME) # SYNTAX - winsound.PlaySound(sound, flags)
# | Flag                    | Meaning                                       |
# | ----------------------- | --------------------------------------------- |
# | `winsound.SND_FILENAME` | Play a `.wav` file                            |
# | `winsound.SND_ALIAS`    | Use a Windows system sound                    |
# | `winsound.SND_ASYNC`    | Play asynchronously (don’t block the program) |
# | `winsound.SND_LOOP`     | Loop sound (must be combined with ASYNC)      |
# | `winsound.SND_PURGE`    | Stop currently playing sound                  |

winsound.MessageBeep(winsound.MB_ICONHAND) #syntax - winsound.MessageBeep(winsound.MB_OK)
# | Constant                      | Sound             |
# | ----------------------------- | ----------------- |
# | `winsound.MB_ICONHAND`        | Error sound       |
# | `winsound.MB_ICONQUESTION`    | Question sound    |
# | `winsound.MB_ICONEXCLAMATION` | Warning sound     |
# | `winsound.MB_ICONASTERISK`    | Information sound |

